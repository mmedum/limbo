from mail_handlers.base_handler import BaseHandler
import requests
import os


class MailgunHandler(BaseHandler):

    def __init__(self):
        self._api_key = os.environ.get('MAILGUN')
        self._domain_name = os.environ.get('DOMAIN')
        self._request_url = f'https://api.mailgun.net/v3/{self._domain_name}/messages'

    def send_mail(self, message):
        response = requests.post(
            self._request_url,
            auth=('api', self._api_key),
            data={'from': message['from'],
                  'to': message['to'],
                  'subject': message['subject'],
                  'text': message['message']})
        return response.ok
