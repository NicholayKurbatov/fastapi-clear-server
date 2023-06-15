from fastapi import APIRouter

from src.api.endpoints.endpoint1 import router

api_router = APIRouter()
api_router.include_router(router.router)