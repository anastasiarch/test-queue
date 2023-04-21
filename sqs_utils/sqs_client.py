import boto3

sqs = boto3.client('sqs', endpoint_url='http://localhost:4566')