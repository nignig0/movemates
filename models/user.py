import uuid
from pydantic import BaseModel, SecretStr, Field
from enums import *
from pydantic.networks import EmailStr

class User(BaseModel):
    first_name: str
    last_name: str
    password: str
    profile_picture: str = None
    email: EmailStr = Field(unique = True )
    contact_info: list[str] = None
    
class LoginPayload(BaseModel):
    email: EmailStr
    password: str
