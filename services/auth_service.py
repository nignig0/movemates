import time
import jwt
from typing import Dict
from dotenv import dotenv_values

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
        'expiry_time': time.time()+600
    }

    token = jwt.encode(payload=payload, key = secret, algorithm=algorithm)
    
    return token_response(token)

def unsignJWT(token: str) -> Dict:
    try:
        payload = jwt.decode(token, key = secret, algorithm = algorithm)

        return payload if payload['expiry_time'] >= time.time() else None

    except Exception as e:
        return {
            'error': e
        }
