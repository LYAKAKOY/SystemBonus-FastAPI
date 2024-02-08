from contextlib import asynccontextmanager
from functools import partial
from typing import NoReturn
from starlette.middleware.cors import CORSMiddleware
from database.postgres.core import new_session, create_session_maker
from fastapi import FastAPI, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from config import load_api_config


@asynccontextmanager
async def lifespan(app: FastAPI) -> NoReturn:
    session_maker = create_session_maker()
    app.dependency_overrides[AsyncSession] = partial(new_session, session_maker)
    yield


def create_app():
    config = load_api_config()
    app = FastAPI(title=config.title, lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    main_api_router = APIRouter(prefix=config.version)
    app.include_router(main_api_router)
    return app


app = create_app()
