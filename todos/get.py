import os
import json
import logging
from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def getRun(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    logger.info('create::createRun::event:{}'.format(event))

    # fetch todo from the database
    get_result = table.get_item(
        Key={
            'id': event['pathParameters']['id'],
            'run': event['pathParameters']['run']
        }
    )
    logger.info('create::createRun::put_response:{}'.format(get_result))
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(get_result['Item'],
                           cls=decimalencoder.DecimalEncoder),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True
        }
    }
    logger.info('create::createRun::put_response:{}'.format(response))

    return response
