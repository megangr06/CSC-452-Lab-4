"""
Lab 4: Q2C: Create an Amazon S3 Bucket
"""
import boto3
s3_client = boto3.client('s3')
filename = 'README.md'
bucket_name = 'mcg033lab42abuc'
s3_client.upload_file(filename, bucket_name, filename)





