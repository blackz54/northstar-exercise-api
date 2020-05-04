import json
import os

from todos import decimalencoder
import boto3
import logging
dynamodb = boto3.resource('dynamodb')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def getAllRuns(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    logger.info('create::createRun::event:{}'.format(event))
    # fetch all todos from the database
    scan_result = table.scan()
    logger.info('create::createRun::event:{}'.format(scan_result))
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(scan_result['Items'], cls=decimalencoder.DecimalEncoder)
    }
    logger.info('create::createRun::event:{}'.format(response))
    return response
