from fastapi import APIRouter


router = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def text():
    return {"message": "Hello endpoint1"}