from fastapi import APIRouter

from src.api.endpoints import router

api_router = APIRouter()
api_router.include_router(router.router)