from model.models import RawPayloadModel, PayloadModel, ValidationError


def parser_mqtt(paylaod):
    try:
        raw_payload = RawPayloadModel(**paylaod)

        return PayloadModel(
            id=raw_payload.id,
            data=raw_payload.date,
            relogio=raw_payload.clock,
            vazao=raw_payload.flow
        ).model_dump(exclude_none=True)

    except ValueError as e:
        print(f'O Erro é:{e}\nPacote Ínvalido, {paylaod}')
