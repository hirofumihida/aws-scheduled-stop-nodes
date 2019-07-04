import os
import json
import boto3
from botocore.vendored import requests

url = os.environ['WEBHOOK_URL']
aws_access_key_id = os.environ['ACCESS_TOKEN']
aws_secret_access_key = os.environ['ACCESS_TOKEN_SECRET']

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

# Example use:

def lambda_handler(event, context):
    ssm_client = boto3.client('ssm', region_name=region) # Need your credentials here
    commands = ['echo "hello world"']
    instance_ids = ['i-0a9c03872fc13e6da']
    execute_commands_on_linux_instances(ssm_client, commands, instance_ids)
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    payload=json.dumps(payload_dic)
    message=requests.post(url, data=payload)
    print(message)

def execute_commands_on_linux_instances(client, commands, instance_ids):
    """Runs commands on remote linux instances
    :param client: a boto/boto3 ssm client
    :param commands: a list of strings, each one a command to execute on the instances
    :param instance_ids: a list of instance_id strings, of the instances on which to execute the command
    :return: the response from the send_command function (check the boto3 docs for ssm client.send_command() )
    """

    resp = client.send_command(
        DocumentName="AWS-RunShellScript", # One of AWS' preconfigured documents
        Parameters={'commands': commands},
        InstanceIds=instance_ids,
    )
    return resp

