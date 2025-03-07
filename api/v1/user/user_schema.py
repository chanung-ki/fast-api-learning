from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Annotated

class GenderType(str, Enum):
    male = 'male'
    female = 'female'

class User(BaseModel):
    # 이렇게 지정함으로써 빈 문자열을 방지할 수 있다.
    name: str = Field(...,  
                      min_length=1, 
                      max_length=10, 
                      description="이름은 1자 이상, 10자 이하로 입력해주세요.")
    phone: Annotated[str, "전화번호"]
    gender: GenderType
    birth: Optional[str] = None

    class Config:
        orm_mode = True