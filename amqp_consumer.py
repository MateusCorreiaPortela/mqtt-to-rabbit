import os
from connections.builder_connections import ConsumerAMQP


QUEUE_AMQP = os.getenv('QUEUE_AMQP', 'fila_teste')
EXCHANGE_QUEUE = os.getenv('EXCHANGE_AMQP', 'exchange_teste')
KEY_AMQP = os.getenv('KEY_AMQP', 'chave_teste')


def callback(ch, method, properties, body):
    print('A mensagem é: ', body)


consumer_amqp = ConsumerAMQP(
    os.getenv('AMQP_HOST', 'localhost'),
    os.getenv('AMQP_PORT', 5672)
)

consumer_amqp.declarete(
        QUEUE_AMQP,
        EXCHANGE_QUEUE
    )

consumer_amqp.queue_bind(
    EXCHANGE_QUEUE,
    QUEUE_AMQP,
    KEY_AMQP
)

consumer_amqp.channel_basic_consume(
    QUEUE_AMQP,
    callback,
)

try:
    consumer_amqp.channel.start_consuming()
    print('\033[1;32m]Consumo feito com sucesso!\033[m')

except KeyboardInterrupt:
    print('Control + C Pressionado saindo!')
