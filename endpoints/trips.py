from typing import Annotated
from fastapi import APIRouter, Body, Request, status, Depends
from models.trip import *
from services import auth_service, trip_service
from utils.api_reponse import *
from fastapi.security.api_key import APIKeyHeader

api_key_header = APIKeyHeader(name='Authorization')


router = APIRouter(prefix='/trips')

@router.post('/')
def create_trip(request: Request, trip: TripCreationObject, token:str = Depends(api_key_header), user_id: str = Depends(auth_service.checkAuthorisation)):
    try:
        trip = trip.dict()
        trip['user_id'] = ObjectId(user_id)

        if trip['travel_buddies']:
            new_travel_buddies = []
            for buddies in trip['travel_buddies']:
                new_travel_buddies.append(ObjectId(buddies))
            trip['travel_buddies'] = new_travel_buddies

        response_data = trip_service.create_trip(request, trip)
        return response_success(
            message = 'Trip Successfully Created!',
            data = response_data,
            status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        print(e)
        return response_failure(
            message='There was an error',
            data=str(e),
        )
    
@router.get('/')
def get_all_trips(request: Request,
                  limit: Annotated[int, "number of things we want in a page"] = 2, 
                  page: Annotated[int, "the page"] = 1):
    try:
        trips: list = trip_service.get_all_trips(request, limit, page)
        return response_success(
            message = 'Trips retrieved successfully',
            data= trips
        )
    except Exception as e:
        print(e)
        return response_failure(
            message='There was an error',
            data=str(e),
        )

@router.get('/{trip_id}')
def get_one_trip(request: Request, trip_id: Annotated[str, "The trip id"]):
    try:
        trip = trip_service.get_one_trip(request, trip_id)
        return response_success(
            message='Trip successfully retrieved',
            data = trip
        )
    except Exception as e:
        print(e)
        return response_failure(
            message='Trip does not exist',
            data=str(e),
        )   

@router.post('/{trip_id}')
def join_leave_a_trip(request: Request, trip_id: str, token:str = Depends(api_key_header), user_id: str = Depends(auth_service.checkAuthorisation)):
    try:
        trip = trip_service.get_one_trip(request, trip_id)
        if trip['user_id'] == user_id:
            return response_failure(
                message='You are hosting the trip already',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        number_of_buddies = len(trip['travel_buddies'])+1
        if number_of_buddies+1 > trip['limit']:
            return response_failure(
                message='You cannot join',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        if user_id in trip['travel_buddies']:
            #remove the user and change the estimated cost 
            index = trip['travel_buddies'].index(user_id)
            trip['travel_buddies'].pop(index)
            trip['estimated_cost_of_trip'] = trip['estimated_cost_of_trip']*number_of_buddies/(number_of_buddies-1)
        else:
            #add the user and change the estimated cost
            trip['travel_buddies'].append(user_id)
            trip['estimated_cost_of_trip'] = trip['estimated_cost_of_trip']*number_of_buddies/(number_of_buddies+1)
     
        del trip['_id']
        del trip['user_id']
        trip['travel_buddies'] = [ObjectId(buddies) for buddies in trip['travel_buddies']]
        new_trip = trip_service.update_trip(request, trip_id, trip)

        return response_success(
            message='Successfully updated trip',
            data = new_trip
        )
        
    except Exception as e:
        print(e)
        return response_failure(
            message='There was an error',
            data=str(e),
        )   
