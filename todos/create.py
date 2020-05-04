import json
import logging
import os
import time
import uuid

import boto3
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')


def createRun(event, context):
    logger.info('create::createRun::event:{}'.format(event))
    data = json.loads(event['body'])
    if 'run' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
    
    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': data['id'],
        'run': data['run'],
        'createdAt': timestamp,
        'uuid': str(uuid.uuid1())
    }

    # write the todo to the database

    put_result = table.put_item(Item=item)
    logger.info('create::createRun::put_response:{}'.format(put_result))

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    logger.info('create::createRun::response:{}'.format(response))
    return response
