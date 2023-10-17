from fastapi import Request
from models.trip import *
from pymongo.collection import Collection
import json
from utils.mappers import documentToTrip

def get_trip_collection(request: Request)-> Collection:
    return request.app.database['trips']

def create_trip(request: Request, tripObj: Trip):
    db = get_trip_collection(request)
    new_trip_id = db.insert_one(tripObj).inserted_id
    new_trip = db.find_one({'_id': new_trip_id})
    return documentToTrip(new_trip)

def get_all_trips(request: Request, limit: int, page: int):
    db = get_trip_collection(request)
    dbTrips = list(db.find(limit=limit, skip=(page-1)*limit))
    trips = []
    for trip in dbTrips:
        trips.append(documentToTrip(trip))
    return trips

