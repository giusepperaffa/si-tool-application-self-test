import os

def lambda_handler(event, context):
    # Helper class to convert a DynamoDB item to JSON.
    class DecimalEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                if o % 1 > 0:
                    return float(o)
                else:
                    return int(o)
            return super(DecimalEncoder, self).default(o)

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    key = urllib.unquote_plus(urllib.unquote(key))
    order = key.split("/")[3]
    orderId = order.split("_")[0]
    userId = order.split("_")[1].replace(".raw", "")

    s3 = boto3.client('s3')
    # download file to /tmp
    download_path = '/tmp/' + order.replace(".raw", ".txt")

    # print download_path
    s3.download_file(bucket, key, download_path)
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    os.system('echo -e "\t\n\t\tDate: {}" >> {}'.format(date, download_path))

