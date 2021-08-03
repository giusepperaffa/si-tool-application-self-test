import os

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    logs_tbl = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    logs_tbl.put_item(Item={"request_id": context.aws_request_id, "event": "invoked"})
    os.system("echo %s > /tmp/user_input" % event)
    result = None
    if os.path.exists("/tmp/user_input"):
        with open("/tmp/user_input", "r") as f:
            result = f.read()
    return result
 
