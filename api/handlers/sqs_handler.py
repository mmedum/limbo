import boto3
from botocore.exceptions import ClientError
import os
import json
import uuid
from sanic.log import logger


class SqsHandler:

    def __init__(self):
        self._sqs = boto3.resource('sqs', region_name=os.environ.get('REGION'))
        self._queue = self._sqs.get_queue_by_name(QueueName=os.environ.get('QUEUE'))

    def send_message(self, message):
        # TODO should handle the duplication problem with sqs
        # better, than just generating a uuid, by using
        # content deduplication, each message needs to be fully
        # unique when looking at the contents, which is solved by
        # using this uuid at the moment.
        retries = 3
        success = False
        message['uuid'] = str(uuid.uuid4())
        messagebody = json.dumps(message)
        while not success and retries > 0:
            try:
                response = self._queue.send_message(MessageGroupId='1', MessageBody=messagebody)
                response_code = response['ResponseMetadata']['HTTPStatusCode']
                if response_code == 200:
                    success = True
            except ClientError as e:
                logger.error(f'Not possible to interact with sqs, failed with error {e}')
            except Exception as e:
                logger.error(f'Connection issues failed with error {e}')
            finally:
                retries -= 1
