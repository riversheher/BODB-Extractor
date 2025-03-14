
from datetime import datetime
from models.record import Record
from models.record import OptionType

import psycopg2


class Quote(Record):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS quotes (
        id BIGSERIAL PRIMARY KEY,
        timestamp TIMESTAMP NOT NULL,
        expiration_date TIMESTAMP NOT NULL,
        ticker VARCHAR(5) NOT NULL,
        strike_price REAL NOT NULL,
        underlying_price REAL NOT NULL,
        option_type optiontype NOT NULL,
        bid REAL NOT NULL,
        ask REAL NOT NULL,
        fingerprint TEXT UNIQUE
    )
    """
    
    insert_query = """
    INSERT INTO quotes
    (timestamp, expiration_date, ticker, strike_price, underlying_price, option_type, bid, ask, fingerprint)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
        
    def __init__(self, record: Record, bid: float, ask: float, id: int = None, fingerprint: str = None):
        """Initializes a new Quote object from the given Record object and bid and ask prices.
        This creates a new record object and does not utilize the input record object to avoid side effects.

        Args:
            record (Record): the record object to create the quote from
            bid (float): the bid price of the option
            ask (float): the ask price of the option
            id (int): the unique identifier for the record
            fingerprint (str): the fingerprint of the record, this is the file name and line number, used to identify the source of the record
        """
        Record.__init__(self, record.timestamp, record.expiration_date, record.ticker, record.option_type, record.strike_price, record.underlying_price, id, fingerprint)
        self.bid = bid
        self.ask = ask
        
    def to_tuple(self) -> tuple:
        """Converts the Quote object to a tuple for the purpose of inserting into the database.

        Returns:
            tuple: a tuple representation of the Quote object
        """
        return (self.timestamp.strftime('%Y-%m-%d %H:%M:%S'), self.expiration_date.strftime('%Y-%m-%d %H:%M:%S'), self.ticker, self.strike_price, self.underlying_price, self.option_type.name, self.bid, self.ask, self.fingerprint)
        
    def insert(self, conn) -> Exception:
        """Inserts the quote record into the database.

        Args:
            conn: the connection to the database

        Returns:
            Exception: an exception is returned if an error occurs, otherwise None is returned
        """        
        try:
            cursor = conn.cursor()
            cursor.execute(Quote.insert_query, self.to_tuple())
            conn.commit()
            return None
        except psycopg2.DatabaseError as error:
            conn.rollback()
            return error
