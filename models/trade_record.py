
from datetime import datetime
from models.record import Record
from models.record import OptionType

class Trade(Record):
    #create_table_query = """
    #CREATE TABLE IF NOT EXISTS trades (
    #    id BIGSERIAL PRIMARY KEY,
    #    timestamp TIMESTAMP NOT NULL,
    #    expiration_date TIMESTAMP NOT NULL,
    #    ticker VARCHAR(5) NOT NULL,
    #    strike_price REAL NOT NULL,
    #    underlying_price REAL NOT NULL,
    #    option_type optiontype NOT NULL,
    #    volume INTEGER NOT NULL,
    #    price REAL NOT NULL,
    #    fingerprint TEXT UNIQUE
    #)
    """
    
    insert_query = """
    #INSERT INTO trades
    #(timestamp, expiration_date, ticker, strike_price, underlying_price, option_type, volume, price, fingerprint)
    #VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
       
    def __init__(self, record: Record, volume: int, price: float, id: int = None, fingerprint: str = None):
        """Initializes a new Trade object from the given Record object and trade details.
        This creates a new record object and does not utilize the input record object to avoid side effects.

        Args:
            record (Record): the record object to create the trade from
            volume (int): the volume of the trade
            price (float): the price of the trade
            id (int): the unique identifier for the record
            fingerprint (str): the fingerprint of the record, this is the file name and line number, used to identify the source of the record
        """
        Record.__init__(self, record.timestamp, record.expiration_date, record.ticker, record.option_type, record.strike_price, record.underlying_price, id, fingerprint)
        self.volume = volume
        self.price = price
        
    def __str__(self):
        return f'Trade: ID: {self.id}, FINGERPRINT: {self.fingerprint},  {self.timestamp}, {self.expiration_date}, {self.ticker}, {self.strike_price}, {self.underlying_price}, {self.price}, {self.volume}'
        
    def to_tuple(self) -> tuple:
        """Returns the trade object as a tuple for the purpose of inserting into the database.

        Returns:
            tuple: a tuple representation of the Trade object
        """
        return (self.timestamp.strftime('%Y-%m-%d %H:%M:%S'), self.expiration_date.strftime('%Y-%m-%d %H:%M:%S'), self.ticker, self.strike_price, self.underlying_price, self.volume, self.price, self.fingerprint)
    
    def insert(self, conn) -> Exception:
        """Inserts the trade object into the database.

        Args:
            conn: the connection to the database

        Returns:
            Exception: an exception is returned if an error occurs, otherwise None is returned
        """
        try:
            cursor = conn.cursor()
            cursor.execute(Trade.insert_query, self.to_tuple())
            conn.commit()
            return None
        except Exception as e:
            conn.rollback()
            return e