
from datetime import datetime
from models.record import Record


class Quote(Record):
    def __init__(self, timestamp: datetime, expiration_date: datetime, ticker: str, strike_price: float, underlying_price: float, bid: float, ask: float):
        """Initializes a new Quote object from the given parameters.

        Args:
            timestamp (datetime): the time at which the quote was recorded
            expiration_date (datetime): the expiration date of the option
            ticker (str): the option ticker
            strike_price (float): the strike price of the option
            underlying_price (float): the price of the underlying asset
            bid (float): the bid price of the option
            ask (float): the ask price of the option
        """
        Record.__init__(self, timestamp, expiration_date, ticker, strike_price, underlying_price)
        self.bid = bid
        self.ask = ask
        
    def __init__(self, record: Record, bid: float, ask: float):
        """Initializes a new Quote object from the given Record object and bid and ask prices.
        This creates a new record object and does not utilize the input record object to avoid side effects.

        Args:
            record (Record): the record object to create the quote from
            bid (float): the bid price of the option
            ask (float): the ask price of the option
        """
        record.__init__(self, record.timestamp, record.expiration_date, record.ticker, record.strike_price, record.underlying_price)
        self.bid = bid
        self.ask = ask
