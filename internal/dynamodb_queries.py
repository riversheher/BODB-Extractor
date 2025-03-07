import boto3
from boto3.dynamodb.conditions import Key
import logging
from decimal import Decimal  

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class MarketDataQueries:
    """Handles querying the market_data table in DynamoDB."""

    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb", region_name="us-east-2")  
        self.table = self.dynamodb.Table("market_data")  

    def get_records_by_fingerprint(self, fingerprint):
        """Fetch records by Fingerprint, which is the partition key."""
        try:
            response = self.table.query(
                KeyConditionExpression=Key("Fingerprint").eq(fingerprint) 
            )
            logger.info(f"✅ Retrieved {len(response['Items'])} records for fingerprint {fingerprint}")
            return response["Items"]
        except Exception as e:
            logger.error(f"❌ Error fetching records by fingerprint: {e}")
            return []

    def get_records_by_ticker(self, ticker):
        """Fetch records by ticker symbol using the GSI."""
        try:
            response = self.table.query(
                IndexName="ticker_symbol-index",
                KeyConditionExpression=Key("ticker_symbol").eq(ticker)
            )
            logger.info(f"✅ Retrieved {len(response['Items'])} records for ticker {ticker}")
            return response["Items"]
        except Exception as e:
            logger.error(f"❌ Error fetching records by ticker: {e}")
            return []

    def get_records_by_timestamp_range(self, start_time, end_time):
        """Fetch records within a timestamp range using SCAN (since timestamp is NOT the partition key)."""
        try:
            response = self.table.scan(
                FilterExpression=Key("timestamp").between(start_time, end_time)  
            )
            logger.info(f"✅ Retrieved {len(response['Items'])} records between {start_time} and {end_time}")
            return response["Items"]
        except Exception as e:
            logger.error(f"❌ Error fetching records by timestamp range: {e}")
            return []

    def get_records_by_strike_price(self, strike):
        """Fetch records by strike price (convert float to Decimal)."""
        try:
            response = self.table.query(
                IndexName="Strike-index",
                KeyConditionExpression=Key("Strike").eq(Decimal(strike))  
            )
            logger.info(f"✅ Retrieved {len(response['Items'])} records for strike price {strike}")
            return response["Items"]
        except Exception as e:
            logger.error(f"❌ Error fetching records by strike price: {e}")
            return []

    def get_records_by_underlying_price(self, underlying_price):
        """Fetch records by underlying price (convert float to Decimal)."""
        try:
            response = self.table.query(
                IndexName="underlying_price-index",
                KeyConditionExpression=Key("underlying_price").eq(Decimal(underlying_price))  
            )
            logger.info(f"✅ Retrieved {len(response['Items'])} records for underlying price {underlying_price}")
            return response["Items"]
        except Exception as e:
            logger.error(f"❌ Error fetching records by underlying price: {e}")
            return []

    def get_records_by_bid(self, bid):
        """Fetch records by bid price (convert float to Decimal)."""
        try:
            response = self.table.query(
                IndexName="bid-index",
                KeyConditionExpression=Key("bid").eq(Decimal(bid))  
            )
            logger.info(f"✅ Retrieved {len(response['Items'])} records for bid price {bid}")
            return response["Items"]
        except Exception as e:
            logger.error(f"❌ Error fetching records by bid price: {e}")
            return []

    def get_records_by_ask(self, ask):
        """Fetch records by ask price (convert float to Decimal)."""
        try:
            response = self.table.query(
                IndexName="ask-index",
                KeyConditionExpression=Key("ask").eq(Decimal(ask))  
            )
            logger.info(f"✅ Retrieved {len(response['Items'])} records for ask price {ask}")
            return response["Items"]
        except Exception as e:
            logger.error(f"❌ Error fetching records by ask price: {e}")
            return []


class TradeRecordQueries:
    """Handles querying the trade_record table in DynamoDB."""

    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb", region_name="us-east-2")  
        self.table = self.dynamodb.Table("trade_record")

    def get_records_by_expiration_date(self, expiration_date):
        """Fetch records by expiration date."""
        try:
            response = self.table.query(
                IndexName="expiration_date-index",
                KeyConditionExpression=Key("expiration_date").eq(expiration_date)
            )
            logger.info(f"✅ Retrieved {len(response['Items'])} records for expiration date {expiration_date}")
            return response["Items"]
        except Exception as e:
            logger.error(f"❌ Error fetching records by expiration date: {e}")
            return []

    def get_records_by_option_type(self, option_type):
        """Fetch records by option type (CALL or PUT)."""
        try:
            response = self.table.query(
                IndexName="option_type-index",
                KeyConditionExpression=Key("option_type").eq(option_type)
            )
            logger.info(f"✅ Retrieved {len(response['Items'])} records for option type {option_type}")
            return response["Items"]
        except Exception as e:
            logger.error(f"❌ Error fetching records by option type: {e}")
            return []

    def get_records_by_price(self, price):
        """Fetch records by price (convert float to Decimal)."""
        try:
            response = self.table.query(
                IndexName="price-index",
                KeyConditionExpression=Key("price").eq(Decimal(price))  
            )
            logger.info(f"✅ Retrieved {len(response['Items'])} records for price {price}")
            return response["Items"]
        except Exception as e:
            logger.error(f"❌ Error fetching records by price: {e}")
            return []

    def get_records_by_volume(self, volume):
        """Fetch records by volume (convert float to Decimal)."""
        try:
            response = self.table.query(
                IndexName="volume-index",
                KeyConditionExpression=Key("volume").eq(Decimal(volume))  
            )
            logger.info(f"✅ Retrieved {len(response['Items'])} records for volume {volume}")
            return response["Items"]
        except Exception as e:
            logger.error(f"❌ Error fetching records by volume: {e}")
            return []
