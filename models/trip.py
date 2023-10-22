from bson import ObjectId
from pydantic import BaseModel, Field
from enums import *
from datetime import datetime
import uuid
    
class Trip(BaseModel):
    user_id: ObjectId
    limit: int = Field(gt=1)
    trip_type: TripTypes
    destination: str
    meet_up_spot: str
    rt_meet_up_spot: str = None #rt -> round trip
    departure_time: datetime
    rt_departure_time: datetime = None
    travel_buddies: list[ObjectId] = None
    estimated_cost_of_trip: int
    active: bool = True
    created_at: datetime = None
    updated_at: datetime = None

    class Config: 
        arbitrary_types_allowed = True

class TripCreationObject(BaseModel):
    limit: int = Field(gt=1)
    trip_type: TripTypes
    destination: str
    meet_up_spot: str
    rt_meet_up_spot: str = None #rt -> round trip
    departure_time: datetime
    rt_departure_time: datetime = None
    travel_buddies: list[str] = None
    estimated_cost_of_trip: int
    active: bool = True
    created_at: datetime = datetime.now()     


class TripUpdatingObject(BaseModel):
    limit: int = None
    trip_type: TripTypes = None
    destination: str = None
    meet_up_spot: str = None
    rt_meet_up_spot: str = None #rt -> round trip
    departure_time: datetime = None
    rt_departure_time: datetime = None
    travel_buddies: list[str] = None
    estimated_cost_of_trip: int = None
    active: bool = True
    updated_at: datetime = datetime.now()     
