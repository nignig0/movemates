from pydantic import BaseModel, Field
from enums import *
from datetime import datetime
import uuid
    
class Trip(BaseModel):
    user_id: str
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
