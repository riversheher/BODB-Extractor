
from datetime import datetime
from models.record import Record
from models.record import OptionType

class Trade(Record):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS trades (
        id BIGSERIAL PRIMARY KEY,
        timestamp TIMESTAMP NOT NULL,
        expiration_date TIMESTAMP NOT NULL,
        ticker VARCHAR(5) NOT NULL,
        strike_price REAL NOT NULL,
        underlying_price REAL NOT NULL,
        option_type optiontype NOT NULL,
        volume INTEGER NOT NULL,
        price REAL NOT NULL,
        fingerprint TEXT NOT NULL
    )
    """
    
    
    def __init__(self, timestamp: datetime, expiration_date: datetime, ticker: str, option_type: OptionType, strike_price: float, underlying_price: float, volume: int, price: float,  id: int = None, fingerprint: str = None):
        """Initializes a new Trade object from the given parameters.

        Args:
            timestamp (datetime): the time at which the quote was recorded
            expiration_date (datetime): the expiration date of the option
            ticker (str): the option ticker
            option_type (OptionType): Call or Put
            strike_price (float): the strike price of the option
            underlying_price (float): the price of the underlying asset
            volume (int): the volume of the trade
            price (float): the price of the trade
            id (int): the unique identifier for the record
            fingerprint (str): the fingerprint of the record, this is the file name and line number, used to identify the source of the record
        """
        Record.__init__(self, timestamp, expiration_date, ticker, option_type, strike_price, underlying_price, id, fingerprint)
        self.volume = volume
        self.price = price
        
        
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