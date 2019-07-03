import os
import json
import boto3
from botocore.vendored import requests

url = os.environ['WEBHOOK_URL']
instances = [i for i in os.environ.get("INSTANCE_LIST").split(" ")]
channel_name = '#info_aws'

region = 'us-east-1'

content = 'stopped your instances: ' + str(instances)
payload_dic = {
    "text":content,
    "username":'AWS Instance Stop',
    "icon_emoji":':awscloud:',
    "channel":channel_name
    }

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    payload=json.dumps(payload_dic)
    message=requests.post(url, data=payload)
    print(message)

