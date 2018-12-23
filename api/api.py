import os
from sanic import Sanic
from sanic_compress import Compress
from sanic.log import logger
from sanic.response import json
from handlers.sqs_handler import SqsHandler

app = Sanic('limbo')
Compress(app)


@app.listener('before_server_start')
async def setup_sqs(app, loop):
    app.sqs = SqsHandler()


@app.listener('before_server_stop')
async def notify_server_stopping(app, loop):
    logger.info('Server shutting down!')


@app.get('/')
async def hello_world(request):
    return json({'hello': 'world'})


@app.get('/health')
async def health(request):
    return json({'health': 'ok'})


@app.get('/metrics')
async def metrics(request):
    return json({'metrics': 'ok'})


@app.post('/mail', version=1)
async def process_mail(request):
    # TODO There could be made a case for email validation.
    # This method only solves adding the message to a queue.
    # Validation could be done by using regex, which is kinda
    # terrible, since there is no official RFC
    # TODO Needs better error handling if sqs is down
    app.sqs.send_message(request.json)
    return json({'Message': 'submitted'})


if __name__ == '__main__':
    logger.info('Starting server')
    app.run(access_log=False, debug=False, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8000)))
