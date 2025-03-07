from enum import Enum
from pydantic import BaseModel
from typing import Optional

class GenderType(str, Enum):
    male = 'male'
    female = 'female'

class User(BaseModel):
    name: str
    phone: str
    gender: GenderType
    birth: Optional[str] = None