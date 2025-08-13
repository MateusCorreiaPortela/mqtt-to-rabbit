from pydantic import BaseModel, ValidationError


class RawPayloadModel(BaseModel):
    id: str
    date: str
    clock: int
    flow: float


class PayloadModel(BaseModel):
    id: str
    data: str
    relogio: int
    vazao: float
