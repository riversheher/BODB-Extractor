import boto3
import unittest
from datetime import datetime
from decimal import Decimal
from moto import mock_aws
from boto3.dynamodb.conditions import Key

# Sample Trade class to mock incoming data
class Trade:
    def __init__(self, fingerprint, ticker, strike_price, expiration_date, underlying_price, option_type, volume, price):
        self.fingerprint = fingerprint
        self.ticker = ticker
        self.strike_price = Decimal(strike_price)
        self.timestamp = datetime.utcnow()
        self.expiration_date = expiration_date
        self.underlying_price = Decimal(underlying_price)
        self.option_type = option_type
        self.volume = int(volume)
        self.price = Decimal(price)

class TestTradeDynamoDB(unittest.TestCase):
    def setUp(self):
        """Start the mock AWS environment and create the DynamoDB table."""
        self.mock_aws = mock_aws()
        self.mock_aws.start()  # Start Moto mock

        self.dynamodb = boto3.resource("dynamodb", region_name="us-east-2")

        # Create the table
        self.table = self.dynamodb.create_table(
            TableName="trade_record",
            KeySchema=[{"AttributeName": "Fingerprint", "KeyType": "HASH"}],  # Partition Key
            AttributeDefinitions=[{"AttributeName": "Fingerprint", "AttributeType": "S"}],
            BillingMode="PAY_PER_REQUEST",
        )
        self.table.wait_until_exists()

    def test_insert_trade(self):
        """Test inserting a trade record."""
        trade = Trade(
            fingerprint="TRADE123",
            ticker="AAPL",
            strike_price=150.0,
            expiration_date=datetime(2025, 12, 31),
            underlying_price=145.5,
            option_type="CALL",
            volume=10,
            price=5.0,
        )

        # Insert the trade
        response = self.table.put_item(
            Item={
                "Fingerprint": trade.fingerprint,
                "Ticker_Symbol": trade.ticker,
                "Strike": trade.strike_price,
                "timestamp": trade.timestamp.isoformat(),
                "expiration_date": trade.expiration_date.isoformat(),
                "underlying_price": trade.underlying_price,
                "option_type": trade.option_type,
                "volume": trade.volume,
                "price": trade.price,
            }
        )

        # Verify insert response
        self.assertEqual(response["ResponseMetadata"]["HTTPStatusCode"], 200)

        # Fetch the record
        response = self.table.get_item(Key={"Fingerprint": "TRADE123"})
        self.assertIn("Item", response)
        self.assertEqual(response["Item"]["Ticker_Symbol"], "AAPL")

    def test_query_by_ticker(self):
        """Test querying trade records by fingerprint."""
        # Insert test record
        self.table.put_item(
            Item={"Fingerprint": "TRADE456", "Ticker_Symbol": "MSFT", "volume": int(20), "price": Decimal(7.5)}
        )

        # Query the record
        response = self.table.query(KeyConditionExpression=Key("Fingerprint").eq("TRADE456"))

        # Verify the result
        self.assertEqual(len(response["Items"]), 1)
        self.assertEqual(response["Items"][0]["Ticker_Symbol"], "MSFT")

    def test_update_trade(self):
        """Test updating an existing trade record."""
        # Insert test record
        self.table.put_item(
            Item={"Fingerprint": "TRADE789", "Ticker_Symbol": "TSLA", "volume": int(5), "price": Decimal(10.0)}
        )

        # Update the record
        response = self.table.update_item(
            Key={"Fingerprint": "TRADE789"},
            UpdateExpression="SET volume=:v, price=:p",
            ExpressionAttributeValues={":v": int(15), ":p": Decimal(12.5)},
            ReturnValues="UPDATED_NEW",
        )

        # Verify update response
        self.assertEqual(response["ResponseMetadata"]["HTTPStatusCode"], 200)
        self.assertEqual(response["Attributes"]["volume"], 15)

    def test_batch_delete_trades(self):
        """Test batch deletion of trades."""
        # Insert multiple test records
        items_to_delete = [
            {"Fingerprint": "DEL1"},
            {"Fingerprint": "DEL2"},
        ]
        for item in items_to_delete:
            self.table.put_item(Item=item)

        # Perform batch deletion
        with self.table.batch_writer() as batch:
            for item in items_to_delete:
                batch.delete_item(Key={"Fingerprint": item["Fingerprint"]})

        # Verify deletion
        for item in items_to_delete:
            response = self.table.get_item(Key={"Fingerprint": item["Fingerprint"]})
            self.assertNotIn("Item", response)  # Should be deleted

    def tearDown(self):
        """Stop the Moto mock."""
        self.mock_aws.stop()

if __name__ == "__main__":
    unittest.main()