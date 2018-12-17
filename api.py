import os
from sanic import Sanic
from sanic.log import logger
from sanic.response import json


app = Sanic('limbo')


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
    received = request.json
    logger.info(received)
    return json({'Message': 'ok'})


if __name__ == '__main__':
    app.run(access_log=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
