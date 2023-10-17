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
    
