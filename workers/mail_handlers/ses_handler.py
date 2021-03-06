import boto3
from botocore.exceptions import ClientError
import os
from mail_handlers.base_handler import BaseHandler
import logging


class SESHandler(BaseHandler):

    def __init__(self):
        self._ses = boto3.client('ses', region_name=os.environ.get('REGION'))

    def send_mail(self, message):
        def build_destination_object(elements):
            dest = {}
            if 'to' in elements:
                dest['ToAddresses'] = elements['to']
            if 'cc' in elements:
                dest['CcAddresses'] = elements['cc']
            if 'bcc' in elements:
                dest['BccAddresses'] = elements['bcc']
            return dest

        try:
            response = self._ses.send_email(
                Destination=build_destination_object(message),
                Message={
                    'Body': {
                        'Text': {
                            'Charset': 'UTF-8',
                            'Data': message['message'],
                        },
                    },
                    'Subject': {
                        'Charset': 'UTF-8',
                        'Data': message['subject'],
                    },
                },
                Source=os.environ.get('SESSOURCE'))

            status_code = response['ResponseMetadata']['HTTPStatusCode']
            if status_code == 200:
                return True, False
            elif status_code >= 400 and status_code <= 499:
                return False, True
            else:
                return False, False

        except ClientError as e:
            logging.error(f'Not possible to send email through ses failed with error {e}')
