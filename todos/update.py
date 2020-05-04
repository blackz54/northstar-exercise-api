import json
import time
import logging
import os
import uuid

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def updateRun(event, context):
    data = json.loads(event['body'])
    if 'run' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    # update the todo in the database
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id'],
            'run': event['pathParameters']['run']
        },
        UpdateExpression='SET id = :id, run = :run, createdAt = :createdAt',
        ExpressionAttributeValues={
          ':id': data['id'],
          ':run': data['run'],
          ':createdAt': timestamp
        },
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
