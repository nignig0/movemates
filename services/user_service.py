from fastapi import Request
from models.user import *
from pymongo.collection import Collection

def get_user_collection(request: Request)-> Collection:
    return request.app.database['users']

def create_user(request: Request, user: User):
    userObj = user.dict()
    user = get_user_collection(request).insert_one(userObj)
    return str(user.inserted_id)

def verify_user(request: Request, login: LoginPayload):
    loginObj = login.dict()
    db = get_user_collection(request)
    user = db.find_one({
        'email': loginObj['email'],
        'password': loginObj['password']
    })

    return str(user['_id']) if user else None