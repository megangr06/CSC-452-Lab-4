"""
Lab 4: Q1J: Delete a security group
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.delete_security_group(GroupId='sg-08e190d5f58209da4')
    print('Success', response)
except ClientError as e:
        print(e)

