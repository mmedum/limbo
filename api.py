import responder

api = responder.API()


@api.route("/")
async def hello_world(req, resp):
    resp.text = "Hello World!"


if __name__ == "__main__":
    api.run()
