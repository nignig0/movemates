from fastapi import APIRouter, Request, status
from models.user import *
from utils.api_reponse import *
from services import user_service,auth_service

router = APIRouter(prefix='/auth')

@router.post('/register')
def register(request: Request, userObj: User):
    try:
        user_id = user_service.create_user(request, userObj)
        token = auth_service.signJWT(user_id)
        return response_success(
        message= 'User Created',
        data=token, status_code= status.HTTP_201_CREATED)

    except Exception as e:
        print(e)
        return response_failure('There was an error') 
    
@router.post('/login')
def login(request: Request, loginPayload: LoginPayload):
    try:
        user_id = user_service.verify_user(request, loginPayload)
        if user_id:
            token = auth_service.signJWT(user_id)
            return response_success(
                message = 'User Logged in!',
                data = token
            )
        else:
            return response_failure(
                message = 'Incorrect username or password',
                status_code=status.HTTP_400_BAD_REQUEST
            )

    except Exception as e:
        print(e)
        return response_failure('There was an error')  
