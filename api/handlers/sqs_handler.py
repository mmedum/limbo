import boto3
import os
import json
import uuid


class SqsHandler:

    def __init__(self):
        self._sqs = boto3.resource('sqs', region_name=os.environ.get('REGION'))
        self._queue = self._sqs.get_queue_by_name(QueueName=os.environ.get('QUEUE'))

    def send_message(self, message):
        should_try_sending = True
        while should_try_sending:
            message['uuid'] = str(uuid.uuid4())
            messagebody = json.dumps(message)
            response = self._queue.send_message(MessageGroupId='1', MessageBody=json.dumps(messagebody))
            if response:
                should_try_sending = False
