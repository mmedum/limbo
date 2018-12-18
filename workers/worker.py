import logging
import boto3
import os


def main():
    logging.info('Starting up')
    sqs = boto3.resource('sqs', region_name=os.environ.get('REGION'))
    queue = sqs.get_queue_by_name(QueueName=os.environ.get('QUEUE'))

    while True:
        logging.info('Waiting for messages')
        messages = queue.receive_messages(WaitTimeSeconds=20, MaxNumberOfMessages=10)
        for message in messages:
            logging.info(f'{message.body}')
            message.delete()


if __name__ == '__main__':
    main()
