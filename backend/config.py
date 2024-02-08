import os
from dataclasses import dataclass
from typing import List


@dataclass
class PostgresDbSettings:
    url: str
    echo: bool


@dataclass
class ApiConfig:
    title: str
    version: str
    allow_origins: List[str]


def load_api_config() -> ApiConfig:
    title = 'api for bonus system'
    version = "/api/v1"
    allow_origins = [
        "http://localhost:8000",
    ]
    return ApiConfig(title, version, allow_origins)


def load_postgres_db_settings() -> PostgresDbSettings:
    url = f"postgresql+asyncpg://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}@" \
          f"{os.environ.get('DATABASE')}:{os.environ.get('POSTGRES_PORT')}/{os.environ.get('POSTGRES_DB')}"
    return PostgresDbSettings(url=url, echo=True)
