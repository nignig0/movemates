from fastapi import APIRouter, Request
from models import user
from services import user_service

router = APIRouter(prefix='/users')

@router.post('/')
def create_user(request: Request, user: user.User):
    new_user = user_service.create_user(request, user)
    return new_user
