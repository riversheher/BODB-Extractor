
from datetime import datetime

class Record():
    def __init__(self, put_flag: bool, timestamp: datetime, expiration_date: datetime, ticker: str, strike_price: float, underlying_price: float):
        """Initializes a new Record object from the given parameters.

        Args:
            put_flag (bool): True if the option is a put, False if the option is a call
            timestamp (datetime): the time at which the record was recorded
            expiration_date (datetime): the expiration date of the option
            ticker (str): the option ticker
            strike_price (float): the strike price of the option
            underlying_price (float): the price of the underlying asset
        """
        self.put = put_flag
        self.timestamp = timestamp
        self.expiration_date = expiration_date
        self.ticker = ticker
        self.strike_price = strike_price
        self.underlying_price = underlying_price
        