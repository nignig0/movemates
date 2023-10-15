from fastapi import responses

def response_success(message: str, data = None, status_code = 200):
    return responses.JSONResponse({
        'message': message,
        'data': data,
    }, status_code=status_code)

def response_failure(message: str, data = None, status_code = 500):
    return responses.JSONResponse({
        'message': message,
        'data': data,
    }, status_code=status_code)
