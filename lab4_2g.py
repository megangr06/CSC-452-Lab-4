"""
Lab 4: Q2E: Retrieve a bucket policy
"""
import boto3
s3 = boto3.client('s3')
bucket_name = 'mcg033lab42abuc'
response = s3.get_bucket_acl(Bucket = bucket_name)
print(response)
