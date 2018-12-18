import boto3
import os
import json
from sanic.log import logger


class SqsHandler:

    def __init__(self):
        self._sqs = boto3.resource('sqs')
        self._queue = self._sqs.get_queue_by_name(QueueName=os.environ.get('QUEUE'))
        logger.info(self._queue)

    def send_message(self, message):
        should_try_sending = True
        while should_try_sending:
            response = self._queue.send_message(MessageGroupId='1', MessageBody=json.dumps(message))
            if response:
                should_try_sending = False
