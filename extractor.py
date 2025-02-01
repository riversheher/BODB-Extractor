from venv import logger
import internal.file_reader as reader
import internal.record_type as record_type
import internal.ticker_conversion as ticker_conversion
from internal.asset_price import price_to_dollars_cents, price_to_dollars_eighths
from internal.date_time import string_to_datetime
from internal.expiration_month import get_expiration_date
from models.record import Record
from datetime import datetime
import psycopg2

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
            print(f"Error connecting to the database: {error}")
            return False
        
    def disconnect(self):
        """
        Disconnects from the database
        """
        if self.conn is not None:
            self.conn.close()
            self.conn = None
            print("Disconnected from the database")
        
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
        for line in file_reader:
            # check if line has 40 characters
            if len(line) != 40:
                pass
            
            record = self.construct_record(line)
            
            # TODO: Insert the record into the database
            
            # TODO: Logging
            
            
    def construct_record(self, line: str) -> Record:
        
        # TODO: Error Handling
        
        # Extract the record type
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
        option_type = OptionType.Call
        if line[19] == '-':
            option_type = OptionType.Put
            
        
        
        
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
        
        
        # TODO: Based on the record type, construct the child record type (quote or trade)
        
        
        return result