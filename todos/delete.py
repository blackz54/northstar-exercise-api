import os
import logging
import boto3
dynamodb = boto3.resource('dynamodb')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def deleteRun(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    logger.info('create::createRun::event:{}'.format(event))

    # delete the todo from the database

    del_result = table.delete_item(
        Key={
            'id': event['pathParameters']['id'],
            'run': event['pathParameters']['run']
        }
    )
    logger.info('create::createRun::put_response:{}'.format(del_result))

    # create a response
    response = {
        "statusCode": 200
    }

    logger.info('create::createRun::response:{}'.format(response))

    return response
