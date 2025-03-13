from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import api
from src.conf.middleware import log
from src.conf.settings import settings

from contextlib import asynccontextmanager



@asynccontextmanager
async def span(_app: FastAPI):
    try:
        from src.conf.db_engine import engine
        yield
        await engine.dispose()
    except Exception as e:
        raise e


app = FastAPI(
    lifespan=span,
    title=settings.app_title,
    version=settings.app_version,
    description=settings.app_description
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of allowed origins here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware('http')(log)

@app.get('/')
async def home():
    return {
        "msg": "Hello World!"
    }


app.include_router(api)
