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
            # TODO should handle the duplication problem with sqs
            # better, than just generating a uuid, by using
            # content deduplication, each message needs to be fully
            # unique when looking at the contents, which is solved by
            # using this uuid at the moment.
            message['uuid'] = str(uuid.uuid4())
            messagebody = json.dumps(message)
            response = self._queue.send_message(MessageGroupId='1', MessageBody=messagebody)
            if response:
                should_try_sending = False
