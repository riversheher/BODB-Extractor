
from datetime import datetime
from models import Record
from enum import Enum

class OptionType(Enum):
    Call = 1
    Put = 2

class Trade(Record):
    def __init__(self, timestamp: datetime, expiration_date: datetime, ticker: str, strike_price: float, underlying_price: float, option_type: OptionType, volume: int, price: float):
        """Initializes a new Trade object from the given parameters.

        Args:
            timestamp (datetime): the time at which the quote was recorded
            expiration_date (datetime): the expiration date of the option
            ticker (str): the option ticker
            strike_price (float): the strike price of the option
            underlying_price (float): the price of the underlying asset
            option_type (OptionType): Call or Put
            volume (int): the volume of the trade
            price (float): the price of the trade
        """
        Record.__init__(self, timestamp, expiration_date, ticker, strike_price, underlying_price)
        self.option_type = option_type
        self.volume = volume
        self.price = price
        
        
    def __init__(self, record: Record, option_type: OptionType, volume: int, price: float):
        """Initializes a new Trade object from the given Record object and trade details.
        This creates a new record object and does not utilize the input record object to avoid side effects.

        Args:
            record (Record): the record object to create the trade from
            option_type (OptionType): Call or Put
            volume (int): the volume of the trade
            price (float): the price of the trade
        """
        Record.__init__(self, record.timestamp, record.expiration_date, record.ticker, record.strike_price, record.underlying_price)
        self.option_type = option_type
        self.volume = volume
        self.price = price