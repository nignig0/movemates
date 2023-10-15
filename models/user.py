import uuid
from pydantic import BaseModel, SecretStr, Field
from enums import *
from pydantic.networks import EmailStr

class User(BaseModel):
    _id: str = Field(default_factory=uuid.uuid4, alias='_id')
    first_name: str
    last_name: str
    password: str
    profile_picture: str
    email: EmailStr = Field(unique = True )
    contact_info: list[str]
    