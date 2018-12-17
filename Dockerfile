FROM kennethreitz/pipenv as build
MAINTAINER Mark Medum Bundgaard <mmedum@gmail.com>

ADD . /code
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 8000

WORKDIR /code

CMD ["python3", "api.py"]
