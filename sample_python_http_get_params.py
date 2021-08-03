import requests

def lambda_handler(event, context):
    # Define URL of the api endpoint
    URL = "https://httpbin.org/get"
    # Init get request parameters from event data
    ParamDict = {"query": event['Records'][0]['s3']['bucket']['name'],"object": event['Records'][0]['s3']['object']['key']}
    # HTTP Get
    Response = requests.get(URL, params=ParamDict)
    # Inspect response object
    print(Response.text)
    print(Response.url)

