import os
from connections.builder_connections import ConsumerAMQP


def callback(ch, method, properties, body):
    print('A mensagem é: ', body)

consumer_amqp = ConsumerAMQP(
    os.getenv('AMQP_HOST', 'localhost'),
    os.getenv('AMQP_PORT', 5672)
)

consumer_amqp.declarete(
        os.getenv('QUEUE_AMQP', 'fila_teste'),
        os.getenv('EXCHANGE_AMQP', 'exchange_teste')
    )

consumer_amqp.queue_bind(
    os.getenv('EXCHANGE_AMQP', 'exchange_teste'),
    os.getenv('QUEUE_AMQP', 'fila_teste'),
    os.getenv('KEY_AMQP', 'chave_teste')
)

consumer_amqp.channel_basic_consume(
    os.getenv('QUEUE_AMQP', 'fila_teste'),
    callback,
)

try:
    consumer_amqp.channel.start_consuming()
    print('\033[1;32m]Consumo feito com sucesso!\033[m')

except KeyboardInterrupt:
    print('Control + C Pressionado saindo!')
