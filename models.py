from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum
import random
import string

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    return result_str

class Gender(str, Enum):
    male = "male"
    female = "female"
    
class personal(str):
    name = str(get_random_string(8))

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    return result_str
    
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class User1(BaseModel):
    fullname: personal

class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]

class User2(BaseModel):
    personal: dict