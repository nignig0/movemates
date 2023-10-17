import time
import jwt
from typing import Dict
from dotenv import dotenv_values
from fastapi import HTTPException, Request, status

config = dotenv_values('.env')
algorithm = config['algorithm']
secret = config['secret']

def token_response(token: str):
    return {
        'access_token': token
    }

def signJWT(user_id: str) -> Dict[str,str]:
    payload = {
        'user_id': user_id,
        'expiry_time': time.time()+86400
    }

    token = jwt.encode(payload=payload, key = secret, algorithm=algorithm)
    
    return token_response(token)

def unsignJWT(token: str) -> Dict:
    try:
        payload = jwt.decode(token, key = secret, algorithms=[algorithm])

        return payload if payload['expiry_time'] >= time.time() else None

    except Exception as e:
        return {
            'error': e
        }

def checkAuthorisation(request: Request):
    authorization_header = request.headers.get('Authorization')
    
    if not authorization_header:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Provide a token')
    
    token = authorization_header.split(' ')[1]
    verified_token = unsignJWT(token)

    if not verified_token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Expired token')

    if 'error' in verified_token.keys():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(verified_token['error']))
    return verified_token['user_id']
