"""
Lab 4: Q1A: First Pyton Boto3 Activity
"""
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
