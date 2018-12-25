# TODO
# Should handles multiple failures instead of just going
# through a if-else struture.


def validate_body(request_body):
    if 'subject' not in request_body:
        return False, {
            'Message': 'not submitted',
            'Problem': 'no subject defined'
        }, 400
    elif 'message' not in request_body:
        return False, {
            'Message': 'not submitted',
            'Problem': 'no message defined'
        }, 400
    elif 'to' not in request_body:
        return False, {
            'Message': 'not submitted',
            'Problem': 'no receivers defined'
        }, 400
    elif 'from' not in request_body:
        return False, {
            'Message': 'not submitted',
            'Problem': 'no from defined'
        }, 400
    else:
        return True, {
            'Message': 'submitted',
        }, 200
    # TODO email validation?
