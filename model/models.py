from pydantic import BaseModel, ValidationError


class RawPayloadModel(BaseModel):
    id: int
    date: str
    clock: int
    flow: float


class PayloadModel(BaseModel):
    id: int
    data: str
    relogio: str
    vazao: float
