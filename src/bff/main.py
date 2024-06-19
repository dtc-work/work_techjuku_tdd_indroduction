from api.api_v1.api import api_router
from core.config import settings
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from utils.util import output_log

app = FastAPI()


# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 初期処理ミドルウェア
@app.middleware("http")
async def initial_middleware(request: Request, call_next):
    # access log
    headers = ", ".join(
        f'"{key}": "{value}"' for key, value in dict(request.headers).items()
    )
    output_log(settings.LOG_LEVEL_INFO, request, "access: { " + headers + " }")

    response = await call_next(request)

    return response


app.include_router(api_router, prefix=settings.API_PATH)
