import boto3
import os

def lambda_handler(event, context):
    # Create dynamodb client
    dynamodb_client = boto3.client('dynamodb')
    result = dynamodb_client.scan(TableName=os.environ['USERS_TABLE'], Select='ALL_ATTRIBUTES', ScanFilter=event['Data'])
    return result

