from fastapi import APIRouter

from server.api.endpoints import point1

api_router = APIRouter()
api_router.include_router(point1.router)