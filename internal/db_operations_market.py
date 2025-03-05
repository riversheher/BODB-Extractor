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

quote_table = dynamodb.Table('market_data')

# Insert a Quote record
def insert_quote(quote):
    response = quote_table.put_item(
        Item={
            'Fingerprint': quote.fingerprint, # Partition key
            'Ticker_Symbol': quote.ticker,
            'Strike': quote.strike_price,
            'timestamp': quote.timestamp.isoformat(),
            'expiration_date': quote.expiration_date.isoformat(),
            'underlying_price': quote.underlying_price,
            'bid': quote.bid,
            'ask': quote.ask
        }
    )
    print(f'Insert response: {response}')

# Query by Ticker_Symbol
def query_by_ticker(fingerprint):
    response = quote_table.query(
        KeyConditionExpression=Key('Fingerprint').eq(fingerprint)
    )
    for item in response['Items']:
        print(f'Item: {item}')

# Query by Ticker_Symbol and Symbol
def query_by_ticker_and_symbol(fingerprint):
    response = quote_table.query(
        KeyConditionExpression=Key('Fingerprint').eq(fingerprint)
    )
    for item in response['Items']:
        print(f'Item: {item}')

# Update a Quote record
def update_quote(fingerprint, strike, new_bid, new_ask):
    response = quote_table.update_item(
        Key={
            'Fingerprint': fingerprint,
        },
        UpdateExpression='SET bid=:b, ask=:a, updated_date=:d',
        ExpressionAttributeValues={
            ':b': new_bid,
            ':a': new_ask,
            ':d': datetime.now().isoformat()
        },
        ReturnValues='UPDATED_NEW'
    )
    print(f'Update response: {response}')

# Batch delete Quotes
def batch_delete_quotes(items_to_delete):
    with quote_table.batch_writer() as batch:
        for item in items_to_delete:
            batch.delete_item(Key={
                'Fingerprint': item['Fingerprint']
            })
    print('Batch delete completed.')