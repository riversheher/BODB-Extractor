import sys
import os

# Add the parent directory to the Python path so `internal/` can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from internal.dynamodb_queries import MarketDataQueries, TradeRecordQueries  
market_queries = MarketDataQueries()
trade_queries = TradeRecordQueries()

def test_queries():
    """Runs a test on all queries to ensure they return results or empty lists without errors."""

    #Test fetching records by ticker symbol
    ticker = "AAPL"
    print(f"🔍 Fetching records for ticker: {ticker}")
    print(market_queries.get_records_by_ticker(ticker))

    #Test fetching records by timestamp range
    start_time = "2024-03-01T00:00:00"
    end_time = "2024-03-05T00:00:00"
    print(f"🔍 Fetching records between {start_time} and {end_time}")
    print(market_queries.get_records_by_timestamp_range(start_time, end_time))

    #Test fetching records by expiration date
    expiration_date = "2024-12-31"
    print(f"🔍 Fetching records for expiration date: {expiration_date}")
    print(trade_queries.get_records_by_expiration_date(expiration_date))

    #Test fetching records by option type
    option_type = "CALL"
    print(f"🔍 Fetching records for option type: {option_type}")
    print(trade_queries.get_records_by_option_type(option_type))

    #Test fetching records by strike price
    strike_price = 150.0
    print(f"🔍 Fetching records for strike price: {strike_price}")
    print(market_queries.get_records_by_strike_price(strike_price))

    #Test fetching records by underlying price
    underlying_price = 200.5
    print(f"🔍 Fetching records for underlying price: {underlying_price}")
    print(market_queries.get_records_by_underlying_price(underlying_price))

    #Test fetching records by bid price
    bid_price = 5.0
    print(f"🔍 Fetching records for bid price: {bid_price}")
    print(market_queries.get_records_by_bid(bid_price))

    #Test fetching records by ask price
    ask_price = 6.0
    print(f"🔍 Fetching records for ask price: {ask_price}")
    print(market_queries.get_records_by_ask(ask_price))


if __name__ == "__main__":
    test_queries()