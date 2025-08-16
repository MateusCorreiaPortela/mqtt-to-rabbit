import os
import json
from connections.rabbitmq_builder_connection import ConsumerAMQP
from connections.database_builder_connection import MongoDB


QUEUE_AMQP = os.getenv('QUEUE_AMQP', 'fila_teste')
EXCHANGE_QUEUE = os.getenv('EXCHANGE_AMQP', 'exchange_teste')
KEY_AMQP = os.getenv('KEY_AMQP', 'chave_teste')


def callback(ch, method, properties, body):
    print('A mensagem é: ', body)
    client_mongo.colecao.insert_one(json.loads(body))
    print('\033[1;32mA mensagem foi gravada no banco com sucesso!\033[m', body)


consumer_amqp = ConsumerAMQP(
    os.getenv('AMQP_HOST', 'rabbitmq'),
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

client_mongo = MongoDB(
    os.getenv('MONGO_HOST', 'mongo'),
    os.getenv('MONGO_DATABASE', 'banco_teste'),
    os.getenv('MONGO_COLLECTION', 'colecao_teste')
)

try:
    consumer_amqp.channel.start_consuming()
    print('\033[1;32m]Consumo feito com sucesso!\033[m')

except KeyboardInterrupt:
    print('Control + C Pressionado saindo!')
