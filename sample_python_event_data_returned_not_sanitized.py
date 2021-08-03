import os

def lambda_handler(event, context):

    sns.publish(
        TopicArn = 'arn:aws:sns:us-east-1::NotifyMe',
        Message = event['queryStringParameters']['message']
    )

    return {
            'statusCode': "200",
            'body': "Lambda has just sent a SNS: " + event['queryStringParameters']['message'],
            'headers': {'Content-Type': 'text/html'},
            }

