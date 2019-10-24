"""
Lab 4: Q1B: Start and Stop Detailed Monitring of an EC2 Instance
"""
import sys
import boto3
ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['i-02ab4ce6bc5eeaf0d'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['i-02ab4ce6bc5eeaf0d'])
print(response)
