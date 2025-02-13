import boto3

client = boto3.client('s3')

response = client.delete_bucket(
    Bucket='demo-akshay-2211-apsdk' #bucket name to be entered 
    
)