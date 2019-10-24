"""
Lab 4: Q1C: Start and Stop an EC2 Instance
"""
import sys
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
action = sys.argv[1].upper()
if action == 'ON':
    #do a dryrun to verify permissions
    try:
        ec2.start_instances(InstanceIds=['i-0001d6f7e865487c2'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry run succeeded, run start_instances again without dryrun
    try:
        response = ec2.start_instances(InstanceIds=['i-0001d6f7e865487c2'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
else:
    #do a dryrun to verify permissions
    try:
        ec2.stop_instances(InstanceIds=['i-0001d6f7e865487c2'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry run succeeded, run start_instances again without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=['i-0001d6f7e865487c2'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
    
