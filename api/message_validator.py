def validate_body(request_body):
    if 'to' not in request_body:
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
