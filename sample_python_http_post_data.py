import requests

def lambda_handler(event, context):
    # Define URL of the api endpoint
    URL = "https://httpbin.org/post"
    # Init post request data from event data
    DataDict = {"message": event['Records']['Sns']['Message']}
    # HTTP Post
    Response = requests.post(URL, data=DataDict)
    # Inspect response object
    print(Response.text)

