import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "test"


settings = Settings()