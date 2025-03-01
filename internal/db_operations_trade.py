from boto3 import resource
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve AWS credentials from environment variables
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

dynamodb = resource(
    'dynamodb',
    region_name=aws_region,
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

trade_table = dynamodb.Table('Options_Data')

# Insert a Trade record
def insert_trade(trade):
    response = trade_table.put_item(
        Item={
            'Ticker_Symbol': trade.ticker,  # Partition key
            'Symbol': trade.strike_price,   # Sort key
            'timestamp': trade.timestamp.isoformat(),
            'expiration_date': trade.expiration_date.isoformat(),
            'underlying_price': trade.underlying_price,
            'option_type': trade.option_type.name,
            'volume': trade.volume,
            'price': trade.price
        }
    )
    print(f'Insert response: {response}')

# Query by Ticker_Symbol
def query_by_ticker(ticker):
    response = trade_table.query(
        KeyConditionExpression=Key('Ticker_Symbol').eq(ticker)
    )
    for item in response['Items']:
        print(f'Item: {item}')

# Query by Ticker_Symbol and Symbol
def query_by_ticker_and_symbol(ticker, symbol):
    response = trade_table.query(
        KeyConditionExpression=Key('Ticker_Symbol').eq(ticker) & Key('Symbol').eq(symbol)
    )
    for item in response['Items']:
        print(f'Item: {item}')

# Update a Trade record
def update_trade(ticker, symbol, new_volume, new_price):
    response = trade_table.update_item(
        Key={
            'Ticker_Symbol': ticker,
            'Symbol': symbol
        },
        UpdateExpression='SET volume=:v, price=:p, updated_date=:d',
        ExpressionAttributeValues={
            ':v': new_volume,
            ':p': new_price,
            ':d': datetime.now().isoformat()
        },
        ReturnValues='UPDATED_NEW'
    )
    print(f'Update response: {response}')

# Batch delete Trades
def batch_delete_trades(items_to_delete):
    with trade_table.batch_writer() as batch:
        for item in items_to_delete:
            batch.delete_item(Key={
                'Ticker_Symbol': item['Ticker_Symbol'],
                'Symbol': item['Symbol']
            })
    print('Batch delete completed.')