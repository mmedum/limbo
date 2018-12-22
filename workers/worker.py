import logging
import boto3
import os
import json
from mail_handlers import ses_handler


def process_messages():
    logging.info('Starting up')
    sqs = boto3.resource('sqs', region_name=os.environ.get('REGION'))
    queue = sqs.get_queue_by_name(QueueName=os.environ.get('QUEUE'))

    ses = ses_handler.SESHandler()
    while True:
        logging.warning('Waiting for messages')
        messages = queue.receive_messages(WaitTimeSeconds=20, MaxNumberOfMessages=10)
        for message in messages:
            messsage_body = json.loads(message.body)
            success = ses.send_mail(messsage_body)
            message.delete()


if __name__ == '__main__':
    process_messages()
