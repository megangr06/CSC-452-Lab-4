"""
Lab 4: Q1F: Create a new key pair
"""

import boto3
ec2 = boto3.client('ec2')
response = ec2.create_key_pair(KeyName='mcg033Lab41fKey')
print('Success', response)