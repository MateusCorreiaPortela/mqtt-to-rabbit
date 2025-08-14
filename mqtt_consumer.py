import os
import json
from connections.builder_connections import ConsumerMQTT, PublisherAMQP, MongoDB
from parsers.parser_packet import parser_mqtt
from pymongo import MongoClient


QUEUE_AMQP = os.getenv('QUEUE_AMQP', 'fila_teste')
EXCHANGE_QUEUE = os.getenv('EXCHANGE_AMQP', 'exchange_teste')
KEY_AMQP = os.getenv('KEY_AMQP', 'chave_teste')


def on_connect(client, userdata, flags, rc):
    print(f'\033[1;32mConectado ao Broker MQTT\033[m: {rc}')


def on_message(client, userdata, msg):
    print(f'\033[1;34mTOPIC\033[m: {msg.topic}')
    print(f'\033[1;34mMENSAGEM RECEBIDA\033[m: {msg.payload}')

    payload = json.loads(msg.payload)

    if not (parse_payload := parser_mqtt(payload)):
        return

    publisher_amqp.declarete(
        QUEUE_AMQP,
        EXCHANGE_QUEUE
    )

    publisher_amqp.queue_bind(
        EXCHANGE_QUEUE,
        QUEUE_AMQP,
        KEY_AMQP
    )

    publisher_amqp.basic_publish(
        EXCHANGE_QUEUE,
        KEY_AMQP,
        json.dumps(payload)
    )


client_mongo = MongoDB(
    os.getenv('MONGO_HOST', 'localhost'),
    os.getenv('MONGO_DATABASE', 'banco_teste'),
    os.getenv('MONGO_COLLECTION', 'colecao_teste')
)

publisher_amqp = PublisherAMQP(
    os.getenv('AMQP_HOST', '172.17.0.2'),
    os.getenv('AMQP_PORT', 5672)
)

consumer_mqtt = ConsumerMQTT(
    os.getenv('MQTT_HOST', 'mongodb://mongo:localhost'),
    os.getenv('MQTT_PORT', 1883),
    os.getenv('MQTT_KEEPALIVE', 60),
    os.getenv('MQTT_TOPIC', 'topico_teste'),
    on_connect,
    on_message
).config_connect()
