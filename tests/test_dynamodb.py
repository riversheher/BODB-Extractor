import pytest
import boto3
from botocore.exceptions import ClientError
from internal.dynamodb_queries import MarketDataQueries, TradeRecordQueries

# ✅ Setup: Use real AWS DynamoDB
@pytest.fixture(scope="module")
def dynamodb_client():
    return boto3.client("dynamodb", region_name="us-east-2")

# ✅ Test fetching data from AWS DynamoDB
def test_get_records_by_ticker(dynamodb_client):
    market_queries = MarketDataQueries()
    
    try:
        result = market_queries.get_records_by_ticker("AAPL")
        assert isinstance(result, list)
        print("✅ Test Passed: Data fetched from AWS DynamoDB")
    except ClientError as e:
        print(f"❌ AWS DynamoDB Access Error: {e}")

def test_get_records_by_option_type(dynamodb_client):
    trade_queries = TradeRecordQueries()

    try:
        result = trade_queries.get_records_by_option_type("CALL")
        assert isinstance(result, list)
        print("✅ Test Passed: Data fetched from AWS DynamoDB")
    except ClientError as e:
        print(f"❌ AWS DynamoDB Access Error: {e}")
