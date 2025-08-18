from pydantic import BaseModel, ValidationError, computed_field


class RawPayloadModel(BaseModel):
    id: str
    date: str
    clock: int
    flow: float
    count_1: int
    count_2: int
    count_3: int

    @computed_field
    def get_cont(self) -> list:
        return [self.count_1, self.count_2, self.count_3]

class PayloadModel(BaseModel):
    id: str
    data: str
    relogio: int
    vazao: float
    contador:  list
