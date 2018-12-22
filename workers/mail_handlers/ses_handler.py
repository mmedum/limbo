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
            if elements['to']:
                dest['ToAddresses'] = [','.join(map(str, elements['to']))]
            if elements['cc']:
                dest['CcAddresses'] = [','.join(map(str, elements['cc']))]
            if elements['bcc']:
                dest['BccAddresses'] = [','.join(map(str, elements['bcc']))]
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
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                return True
            else:
                return False

        except ClientError as e:
            logging.error(f'Not possible to send email through ses failed with error {e}')
            return False
