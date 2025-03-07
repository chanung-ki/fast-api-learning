from fastapi import APIRouter

from .user_schema import User

temp_user = [
    {
        "name": "test1",
        "phone": "01000000000",
        "gender": "female",
        "birth": None,
    },
    {
        "name": "test2",
        "phone": "01000000002",
        "gender": "male",
        "birth": "970216",
    },
]

router = APIRouter(
    prefix="/api/v1/user",
)

@router.get(path="",
            description="유저 목록 출력")
async def get_user_lsit():
    return {
        "result": True,
        "data": temp_user
    }

@router.post(path="",
             description="회원 가입")
async def signin_user(user: User):
    return {
        "result": True,
        "data": temp_user
    }