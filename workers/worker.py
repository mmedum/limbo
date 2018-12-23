import logging
import boto3
import os
import json
from mail_handlers import ses_handler, mailgun_handler


def setup_handlers():
    '''
    Factory method for setting up handlers for the worker
    '''
    return [ses_handler.SESHandler(), mailgun_handler.MailgunHandler()]


def process_messages():
    logging.info('Starting up')
    sqs = boto3.resource('sqs', region_name=os.environ.get('REGION'))
    queue = sqs.get_queue_by_name(QueueName=os.environ.get('QUEUE'))

    handlers = setup_handlers()

    while True:
        logging.info('Waiting for messages')
        messages = queue.receive_messages(WaitTimeSeconds=20, MaxNumberOfMessages=10)
        for message in messages:
            messsage_body = json.loads(message.body)
            success = False
            handler_index = 0
            while not success and handler_index < len(handlers):
                success = handlers[handler_index].send_mail(messsage_body)
                handler_index += 1
            if success:
                message.delete()


if __name__ == '__main__':
    process_messages()
