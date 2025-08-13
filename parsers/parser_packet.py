from model.models import RawPayloadModel, PayloadModel, ValidationError


def parser_mqtt(paylaod):
    try:
        raw_payload = RawPayloadModel(**paylaod)

        return PayloadModel(
            id=raw_payload.id,
            data=raw_payload.date,
            relogio=raw_payload.clock,
            vazao=raw_payload.clock
        ).model_dump(exclude_none=True)

    except ValidationError as e:
        print(f'{ValidationError}\nPacote Ínvalido, {paylaod}')