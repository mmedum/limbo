class BaseHandler:
    '''Abstract handler for send emails'''

    def send_mail(self, package):
        raise NotImplementedError('Not implemented in abstract class')
