from fastapi import Request
from fastapi.encoders import jsonable_encoder
from models.user import User
from pymongo.collection import Collection

def get_user_collection(request: Request)-> Collection:
    return request.app.database['users']

def create_user(request: Request, user: User):
    userObj = user.dict()
    user = get_user_collection(request).insert_one(userObj)
    new_user = get_user_collection(request).find_one({'_id': user.inserted_id}, {'_id': 0})
    return new_user