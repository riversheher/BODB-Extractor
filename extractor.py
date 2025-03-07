from venv import logger
import logging
import internal.file_reader as reader
import internal.record_type as record_type
import internal.ticker_conversion as ticker_conversion
import internal.trade_detail as trade
from internal.asset_price import price_to_dollars_cents, price_to_dollars_eighths
from internal.date_time import string_to_datetime
from internal.expiration_month import get_expiration_date
from models.record import Record
from models.trade_record import Trade
from models.quote_record import Quote
from datetime import datetime
import psycopg2
import os

from models.record import OptionType
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
    
    def __init__(self, db_config: dict):
        self.db_config = db_config
        self.conn = None
        logging.basicConfig(filename=f'{datetime.now().year}.log',format='%(asctime)s %(message)s', filemode='w', level=logging.INFO)
        self.log = logging.getLogger()
        
    def connect(self):
        """
        connects to the database
        """
        try:
            # connecting to the PGSQL Server
            with psycopg2.connect(
                host = self.db_config['host'],
                database = self.db_config['database'],
                user = self.db_config['user'],
                password = self.db_config['password'],
                ) as conn:
                print("Connected to the database")
                self.conn = conn
                return True
        except (psycopg2.DatabaseError, Exception) as error:
            self.log.critical("error connecting to the database!")
            return False
        
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
        
        self.log.info(f'STARTING EXTRACTION FOR {file_name}')
        
        for line in file_reader:
            line_number += 1
            # check if line has 40 characters
            if len(line) != 40:
                pass
            try:
                record = self.construct_record(line)
            except Exception as e:
                self.log.warning(f'Error extracting record: {str(record)}: \n{repr(e)}\n skipping...')
                continue
            
            if record is not None:
                record.fingerprint = f"{file_name}:{line_number}"
                try:
                    record.insert(self.conn)
                    successes += 1
                except Exception as e:
                    errors += 1
                    self.log.warning(f'Error extracting record: {str(record)}: \n{repr(e)}\n skipping...')
                    continue
        
        self.log.info(f'Finished extracting {file_name}, with successes: {successes}, and errors: {errors}')
            
            
            
            
    def construct_record(self, line: str) -> Record:
        """construct_record constructs a record object from a line of BODB data
        If the line is not a valid BODB record, None is returned
        If the line is a valid BODB record, a Record object is returned,
        it could be of type Quote or Trade

        Args:
            line (str): The line extracted from the BODB file

        Returns:
            Record: A Record object representing the BODB data,
            or None if the line is not a valid BODB record.  This is of child type Quote or Trade
        """
        
        # TODO: Error Handling
        
        # Extract the record type
        type = None
        try:
            type = record_type.get_record_type(line[0:2])
        except ValueError as e:
            logger.error(f"Failed to extract record type: {e}")
            return None
            
        # Extract the ticker details
        ticker_symbol = ticker_conversion.get_ticker_details(line[2:5])
        
        # Extract the date and time
        date_time = string_to_datetime(line[5:17])
        
        # Extract the expiration date
        expiration_date = get_expiration_date(line[17:19], date_time)
        
        # Extract the call/put flag
        option_type = OptionType.call
        if line[19] == '-':
            option_type = OptionType.put
        
        # Extract the strike price
        strike_price = price_to_dollars_cents(line[20:25])
        
        # Extract the underlying price
        # Create a datetime object for January 1986
        jan_1986 = datetime(1986, 1, 1)
        if date_time < jan_1986:
            underlying_price = price_to_dollars_cents(line[35:40])
        else:
            underlying_price = price_to_dollars_eighths(line[35:40])
            
        # Create a record object
        result = Record(date_time, expiration_date, ticker_symbol, option_type, strike_price, underlying_price)
        
        
        # Based on the record type, construct the child record type (quote or trade)
        if type == None:
            raise Exception("No type was extracted")
        try:
            if type == "Trade":
                price = price_to_dollars_cents(line[25:30])
                volume = trade.get_volume(line[30:35])
                trade_record = Trade(result, volume, price)
                return trade_record
            elif type == "Quote":
                bid = price_to_dollars_cents(line[25:30])
                ask = price_to_dollars_cents(line[30:35])
                quote_record = Quote(result, bid, ask)
                return quote_record
            else:
                raise Exception(f'Extraction for record type: {type} not implemented')
        except Exception as e:
            raise Exception(f'Error in construction Quote or Trade: {repr(e)}')
            
        
        return result