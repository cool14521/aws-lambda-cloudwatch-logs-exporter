import json
import os

import boto3

LOG_GROUP_NAME = os.environ['LOG_GROUP_NAME']
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
S3_DESTINATION_NAME = os.environ['S3_DESTINATION_NAME']


def lambda_handler(event, context):
    print(f'Received event: {json.dumps(event, indent=4)}')

    task_name = event['taskName']
    fromTime = event['fromTime']
    toTime = event['toTime']

    client = boto3.client('logs')
    response = client.create_export_task(
        taskName=task_name,
        logGroupName=LOG_GROUP_NAME,
        fromTime=fromTime,
        to=toTime,
        destination=S3_BUCKET_NAME,
        destinationPrefix=S3_DESTINATION_NAME)

    print(f'Response: {json.dumps(response, indent=4)}')

    return response
