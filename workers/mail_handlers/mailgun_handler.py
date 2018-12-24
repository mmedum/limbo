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
        status_code = response.status_code
        if status_code == 200:
            return True, False
        elif status_code >= 400 and status_code <= 499:
            return False, True
        else:
            return False, False
