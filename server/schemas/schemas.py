from pydantic import BaseModel


class TestBase(BaseModel):
    info: str
    data: str | None = None


class TestCreate(TestBase):
    pass


class Test(TestBase):
    id: int

    class Config:
        orm_mode = True