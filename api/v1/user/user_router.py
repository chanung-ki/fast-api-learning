from fastapi import APIRouter, Path, Query, Form, UploadFile
from typing import Annotated

from .user_schema import User, GenderType 

temp_user = [
    {
        "name": "test1",
        "phone": "01000000000",
        "gender": "female",
        "birth": None
    },
    {
        "name": "test2",
        "phone": "01000000002",
        "gender": "male",
        "birth": "970216"
    },
]


router = APIRouter(
    prefix="/api/v1/user",
)


@router.get(path="", description="유저 목록 출력")
async def get_user_lsit():
    return {
        "result": True, 
        "data": temp_user
    }


@router.get(path="/{user_id}", description="유저 상세 정보 출력")
async def get_user_detail(
    user_id: Annotated[int, Path(..., description="조회하고자 하는 유저의 id 값")] # 이렇게 함으로써 swagger에 설명 추가 가능
):
    return {
        "result": True, 
        "data": temp_user
    }


@router.get(path="/", description="유저 상세 정보 출력")
async def get_user_detail2(
    user_id: Annotated[int, Query(..., description="조회하고자 하는 유저의 id 값")]  # Query로 변경
):
    return {
        "result": True,
        "data": temp_user
    }

@router.post(path="", description="회원 가입")
async def signin_user(user: User):

    temp_user.append(user)

    return {
        "result": True, 
        "data": temp_user
    }



@router.post(path="/form", description="form 회원 가입")
async def signin_user_form(
    name: str = Form(...),
    phone: str = Form(...),
    gender: GenderType = Form(...),
    birth: str = Form(None)
):
    
    response_data = {
        "name": name,
        "phone": phone,
        "gender": gender,
        "birth": birth,
    }

    return {
        "result": True, 
        "data": response_data
    }


# 파일 처리
@router.patch(path="/profile", description="프로필 사진 변경")
async def update_profile_image(file: UploadFile):
    return {"filename": file.filename}