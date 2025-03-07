from typing import Union

from fastapi import FastAPI

from api.v1.user import user_router

app = FastAPI()

### routing
app.include_router(user_router.router) # 유저


@app.get("/")
def read_root():
    return {
        "result": True,
        "msg": "root_page"
    }



