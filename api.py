import responder

api = responder.API()


@api.route("/health")
def health(req, resp):
    resp.media = {"health": "ok"}
#    resp.status_code = api.status_codes.HTTP_200


@api.route("/")
def hello_world(req, resp):
    resp.text = "Hello World!"


if __name__ == "__main__":
    api.run()
