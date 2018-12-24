import logging
import boto3
import os
import json
from random import shuffle
from mail_handlers import ses_handler, mailgun_handler


# TODO
# Should using the deadletter queue, at the moment the naive approach
# is adding a message, when it has been 'taken' three times from the queue.

def setup_handlers():
    '''
    Factory method for setting up handlers for the worker
    '''
    handlers = [ses_handler.SESHandler(), mailgun_handler.MailgunHandler()]
    shuffle(handlers)
    return handlers


def process_messages():
    logging.info('Starting processing messages')
    sqs = boto3.resource('sqs', region_name=os.environ.get('REGION'))
    queue = sqs.get_queue_by_name(QueueName=os.environ.get('QUEUE'))
    deadletter_queue = sqs.get_queue_by_name(QueueName=os.environ.get('DEADLETTERQUEUE'))

    handlers = setup_handlers()

    while True:
        logging.info('Waiting for messages')
        messages = queue.receive_messages(WaitTimeSeconds=20, MaxNumberOfMessages=10)
        for message in messages:
            messsage_body = json.loads(message.body)

            success = False
            dead_message = False
            handler_index = 0
            while not success and not dead_message and handler_index < len(handlers):
                success, dead_message = handlers[handler_index].send_mail(messsage_body)
                handler_index += 1

            if dead_message:
                deadletter_queue.send_message(MessageGroupId='1', MessageBody=messsage_body)
                message.delete()
            if success:
                message.delete()


if __name__ == '__main__':
    process_messages()
