# from venv import logger
import traceback
import logging
import internal.file_reader as reader
import internal.record_type as record_type
import internal.ticker_conversion as ticker_conversion
import internal.trade_detail as trade
# import internal.db_operations_market as quote_operations
# import internal.db_operations_trade as trade_operations
from internal.asset_price import price_to_dollars_cents, price_to_dollars_eighths
from internal.date_time import string_to_datetime
from internal.expiration_month import get_expiration_date
from models.record import Record
from models.trade_record import Trade
from models.quote_record import Quote
from models.tertiary_record import tertiary_record as TertiaryRecord
from internal.db_operations_pg_quotes import db_operations_pg_quotes as quotes_pg
from internal.db_operations_pg_trades import db_operations_pg_trades as trades_pg
from internal.db_operations_pg_tertiary import db_operations_pg_tertiary as tertiary_pg
from datetime import datetime
# import psycopg2  # POSTGRES
import os
from multiprocessing import Pool
from functools import partial

from models.record import OptionType


def process_line(line_tuple):
    line, line_number, file_name = line_tuple
    log = logging.getLogger()

    if len(line) != 40:
        return None

    try:
        line_type = record_type.get_record_type(line[0:2])
        record = extractor.construct_record(line)
        if record is None:
            return None

        record.fingerprint = f"{file_name}:{line_number}"

        if line_type in ("Trade", "Quote"):
            return line_type, record
        else:
            return ("Tertiary", TertiaryRecord(
                record_type=line_type,
                timestamp=record.timestamp,
                ticker=record.ticker,
                raw_line=line,
                fingerprint=record.fingerprint
            ))
    except Exception as e:
        log.warning(f'Error processing line #{line_number}: {repr(e)}')
        return None

def construct_record(line: str) -> Record:
    try:
        type = record_type.get_record_type(line[0:2])
    except ValueError as e:
        logging.error(f"Failed to extract record type: {e}")
        return None

    ticker_symbol = ticker_conversion.get_ticker_details(line[2:5])
    date_time = string_to_datetime(line[5:17])
    expiration_date = get_expiration_date(line[17:19], date_time)
    option_type = OptionType.call if line[20] != '-' else OptionType.put
    strike_price = price_to_dollars_cents(line[21:25])

    jan_1986 = datetime(1986, 1, 1)
    if date_time < jan_1986:
        underlying_price = price_to_dollars_cents(line[35:40])
    else:
        underlying_price = price_to_dollars_eighths(line[35:40])

    result = Record(date_time, expiration_date, ticker_symbol, option_type, strike_price, underlying_price)

    try:
        if type == "Trade":
            price = price_to_dollars_cents(line[25:30])
            volume = trade.get_volume(line[30:35])
            return Trade(result, volume, price)
        elif type == "Quote":
            bid = price_to_dollars_cents(line[25:30])
            ask = price_to_dollars_cents(line[30:35])
            return Quote(result, bid, ask)
        else:
            return result
    except Exception as e:
        logging.getLogger().error(f'Error in construction Quote or Trade: {repr(e)}')
        raise e

class extractor:
    """
    Extractor is a class that handles the extraction of BODB data from a file,
    and inserts the data into the provided database.

    The extractor orchestrates the extraction of data from the BODB file, and the
    database connection.

    To use the extractor, create an instance of the class, and call the extract() method
    with the path to the BODB file you wish to extract.

    When creating the instance of the extractor, you can pass in the database configuration
    as a dictionary.  This dictionary should contain the following
    TODO: Add the database configuration dictionary keys here.
    """

    # db_config: dict removed from initial parameters, add back in to use local postgres
    def __init__(self):
        #self.db_config = db_config
        #self.conn = None
        log_dir = "/scratch/nabbasey/logs"
        os.makedirs(log_dir, exist_ok=True)
        timestamp_log = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_path = os.path.join(log_dir, f"{timestamp_log}.log")
        logging.basicConfig(filename=log_path, format='%(asctime)s %(message)s', filemode='w',
                            level=logging.INFO)
        self.log = logging.getLogger()

    # def connect(self):  # POSTGRES
    #     """
    #     connects to the database
    #     """
    #     try:
    #         # connecting to the PGSQL Server
    #         with psycopg2.connect(
    #             host=self.db_config['host'],
    #             database=self.db_config['database'],
    #             user=self.db_config['user'],
    #             password=self.db_config['password'],
    #         ) as conn:
    #             print("Connected to the database")
    #             self.conn = conn
    #             return True
    #     except (psycopg2.DatabaseError, Exception) as error:
    #         self.log.critical("error connecting to the database!")
    #         return False

    def disconnect(self):
        """
        Disconnects from the database
        """
        if self.conn is not None:
            self.conn.close()
            self.conn = None
            self.log.info("disconnected from database")

    def is_connected(self):
        """
        Returns True if the connection to the database is open, False otherwise
        """
        return self.conn is not None

    def get_connection(self):
        """
        Returns the connection object to the database
        """
        return self.conn

    def extract(self, filepath):
        # Call the file reader to read the file line by line
        file_reader = reader.read_file(filepath)
        # Keep track of line number and file name
        line_number = 0
        errors = 0
        successes = 0
        file_name = os.path.basename(filepath)
        item_type = 0
        trade_records = []
        quote_records = []
        tertiary_records = []

        self.log.info(f'STARTING EXTRACTION FOR {file_name}')

        pool_input = [(line, i + 1, file_name) for i, line in enumerate(file_reader)]

        with Pool(processes=4) as pool:
            results = pool.map(extractor.process_line, pool_input)

        for result in results:
            if result is None:
                errors += 1
                continue
            try:
                line_type, record = result
                if line_type == "Trade":
                    trade_records.append(record)
                elif line_type == "Quote":
                    quote_records.append(record)
                elif line_type == "Tertiary":
                    tertiary_records.append(record)
                successes += 1
            except Exception as e:
                errors += 1
                self.log.warning(f'Error extracting record: {str(result)}: \n{repr(e)}\nSkipping...')
                continue

        try:
            if trade_records:
                trades_pg.insert_many(trade_records)
            if quote_records:
                quotes_pg.insert_many(quote_records)
            if tertiary_records:
                tertiary_pg.insert_many(tertiary_records)
        except Exception as e:
            self.log.critical(f'Critical failure during batch inserts: {repr(e)}')

        self.log.info(f'FINISHED extracting {file_name} with {successes} successes and {errors} errors')






"""
    def extract(self, filepath):
        # Call the file reader to read the file line by line
        file_reader = reader.read_file(filepath)
        # Keep track of line number and file name
        line_number = 0
        errors = 0
        successes = 0
        file_name = os.path.basename(filepath)
        item_type = 0

        self.log.info(f'STARTING EXTRACTION FOR {file_name}')

        for line in file_reader:
            line_number += 1
            # check if line has 40 characters
            if len(line) != 40:
                pass
            try:
                line_type = record_type.get_record_type(line[0:2])
                record = self.construct_record(line)
            except Exception as e:
                self.log.warning(f'Error extracting record on line number: #{line_number} text: {line}: \n{repr(e)}\n skipping...')
                continue

            if record is not None:
                record.fingerprint = f"{file_name}:{line_number}"
                try:
                    # record.insert(self.conn)  # POSTGRES
                    if line_type == "Trade":
                        trades_pg.insert(record)
                        # trade_operations.insert_trade(record) #DYNAMO
                    elif line_type == "Quote":
                        quotes_pg.insert(record)
                        # quote_operations.insert_quote(record) #DYNAMO
                    else:
                         self.log.info(f'File {file_name}, Line {line_number}: Unknown Record type "{line_type}" for record: {record}')
                         tertiary_pg.insert(line_type, record.timestamp, record.ticker, line, record.fingerprint)
                    successes += 1
                except Exception as e:
                    errors += 1
                    self.log.warning(f'Error extracting record: {str(record)}: \n{repr(e)}\n')
                    traceback.print_exception(type(e), e, e.__traceback__)
                    self.log.warning(f'skipping...')
                    continue

        self.log.info(f'Finished extracting {file_name}, with successes: {successes}, and errors: {errors}')
"""


