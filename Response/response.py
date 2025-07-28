def json_response(data=None, success=None, message=''):
    return {
        'data': data,
        'success': success,
        'message': message
    }

def json_error_response(e):
    exception_message = 'Ocurrio un error: ' + str(e)
    return json_response(success=False, message=exception_message)