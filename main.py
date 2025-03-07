import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from api.v1.user import user_router

app = FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### routing
app.include_router(user_router.router) # 유저


@app.get("/")
def read_root():
    return {
        "result": True,
        "msg": "root_page"
    }


# 미들웨어 사용 방법
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    # response.headers["X-Process-Time"] = str(process_time)
    print(f"process_time: {process_time}")
    return response


