import sys
from internal import dynamodb_queries

def query_test():
    query_quotes = dynamodb_queries.MarketDataQueries()
    print(query_quotes.get_records_by_ticker("AA"))

query_test()
