"""
Lab 4: Q1I: Create a new security group
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.create_security_group(GroupName='lab4_1i', Description='lab4_1i created 10/29/19')
    print('Success', response)
except ClientError as e:
        print(e)

