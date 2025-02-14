import boto3

client = boto3.client('ec2')

instance = ec2.create_instances(
    ImageId='ami-04b4f1a9cf54c11d0',
    InstanceType='t2.micro'
    KeyName='/home/akshay-singh/MyKeyPair.pem',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': True
    }
)