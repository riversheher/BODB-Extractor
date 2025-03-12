
from datetime import datetime
from enum import Enum

class OptionType(Enum):
    call = 1
    put = 2

class Record():
    
    option_type_query = """
    CREATE TYPE optiontype AS ENUM('call', 'put');
    """
    
    
    def __init__(self, timestamp: datetime, expiration_date: datetime, ticker: str, option_type: OptionType, strike_price: float, underlying_price: float, id: int = None, fingerprint: str = None):
        """Initializes a new Record object from the given parameters.

        Args:
            timestamp (datetime): the time at which the record was recorded
            expiration_date (datetime): the expiration date of the option
            ticker (str): the option ticker
            option_type (OptionType): Call or Put
            strike_price (float): the strike price of the option
            underlying_price (float): the price of the underlying asset
            id (int): the unique identifier for the record
            fingerprint (str): the fingerprint of the record, this is the file name and line number, used to identify the source of the record
        """
        self.id = id
        self.timestamp = timestamp
        self.expiration_date = expiration_date
        self.ticker = ticker
        self.option_type = option_type
        self.strike_price = strike_price
        self.underlying_price = underlying_price
        self.fingerprint = fingerprint
        