"""
Lab 4: Q1D: Describe Key Pairs
"""
import sys
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs()
print('Success', response)