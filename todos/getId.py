import os
import json
from boto3.dynamodb.conditions import Key, Attr
from todos import decimalencoder
import boto3
import logging
dynamodb = boto3.resource('dynamodb')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def getIdRuns(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    logger.info('create::createRun::event:{}'.format(event))

    query_result = table.query(
        KeyConditionExpression=Key('id').eq(event['pathParameters']['id'])
    )
    logger.info('create::createRun::event:{}'.format(query_result))
    response = {
        "statusCode": 200,
        "body": json.dumps(query_result['Items'],
                           cls=decimalencoder.DecimalEncoder),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True
        }
    }
    logger.info('create::createRun::event:{}'.format(response))

    return response
