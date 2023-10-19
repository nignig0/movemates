from fastapi import Request, HTTPException, status
from models.trip import *
from pymongo.collection import Collection
from pymongo import ReturnDocument
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

def get_one_trip(request: Request, trip_id: str):
    db = get_trip_collection(request)
    dbTrip = db.find_one({'_id': ObjectId(trip_id)})
    
    if dbTrip == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Trip does not exis')

    return documentToTrip(dbTrip)

def update_trip(request: Request, trip_id: str, updateObj: TripUpdatingObject):
    db = get_trip_collection(request)
    new_trip = db.find_one_and_update({'_id': ObjectId(trip_id)}, {'$set': updateObj}, return_document=ReturnDocument.AFTER)
    return documentToTrip(new_trip)

