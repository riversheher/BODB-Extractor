
from datetime import datetime

class Record():
    def __init__(self, timestamp: datetime, expiration_date: datetime, ticker: str, strike_price: float, underlying_price: float):
        """Initializes a new Record object from the given parameters.

        Args:
            timestamp (datetime): the time at which the quote was recorded
            expiration_date (datetime): the expiration date of the option
            ticker (str): the option ticker
            strike_price (float): the strike price of the option
            underlying_price (float): the price of the underlying asset
        """
        self.timestamp = timestamp
        self.expiration_date = expiration_date
        self.ticker = ticker
        self.strike_price = strike_price
        self.underlying_price = underlying_price
        