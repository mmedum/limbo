from mail_handlers.base_handler import BaseHandler
import requests
import os


class MailgunHandler(BaseHandler):

    def __init__(self):
        self._api_key = os.environ.get('MAILGUN')
        self._domain_name = os.environ.get('DOMAIN')
        self._request_url = f'https://api.mailgun.net/v3/{self._domain_name}/messages'

    def send_mail(self, message):
        def build_data_object(elements):
            dest = {}
            if elements['to']:
                dest['to'] = elements['to']
            if elements['cc']:
                dest['cc'] = elements['cc']
            if elements['bcc']:
                dest['bcc'] = elements['bcc']
            if elements['subject']:
                dest['subject'] = elements['subject']
            if elements['message']:
                dest['text'] = elements['message']
            return dest

        request_data = build_data_object(message)
        response = requests.post(
            self._request_url,
            auth=('api', self._api_key),
            data=request_data)
        status_code = response.status_code
        if status_code == 200:
            return True, False
        elif status_code >= 400 and status_code <= 499:
            return False, True
        else:
            return False, False
