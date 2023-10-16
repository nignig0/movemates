from fastapi import Request
from models.trip import *
from pymongo.collection import Collection
import json

def get_trip_collection(request: Request)-> Collection:
    return request.app.database['trips']

def create_trip(request: Request, tripObj: Trip):
    db = get_trip_collection(request)
    new_trip_id = db.insert_one(tripObj).inserted_id
    new_trip = db.find_one({'_id': new_trip_id})
    return json.dump(new_trip)
