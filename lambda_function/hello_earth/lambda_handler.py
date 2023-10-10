import requests

def lambda_handler(event, context):
    response = requests.get("example.com")
    return {
        'statusCode': 200,
        'body': "Hello, earth 1"
    }