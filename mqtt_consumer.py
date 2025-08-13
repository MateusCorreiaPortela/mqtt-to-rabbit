import os
import json
from connections.builder_connections import ConsumerMQTT, PublisherAMQP
from parsers.parser_packet import parser_mqtt


def on_connect(client, userdata, flags, rc):
    print(f'\033[1;32mConectado ao Broker MQTT\033[m: {rc}')


def on_message(client, userdata, msg):
    print(f'\033[1;34mTOPIC\033[m]: {msg.topic}')
    print(f'\033[1;34mMENSAGEM RECEBIDA: {msg.payload}')

    payload = json.loads(msg.payload)

    if not (parse_payload := parser_mqtt(payload)):
        return

    publisher_amqp.declarete(
        os.getenv('QUEUE_AMQP', 'fila_teste'),
        os.getenv('EXCHANGE_AMQP', 'exchange_teste')
    )

    publisher_amqp.queue_bind(
        os.getenv('EXCHANGE_AMQP', 'exchange_teste'),
        os.getenv('QUEUE_AMQP', 'fila_teste'),
        os.getenv('KEY_AMQP', 'chave_teste')
    )

    publisher_amqp.basic_publish(
        os.getenv('EXCHANGE_AMQP', 'exchange_teste'),
        os.getenv('KEY_AMQP', 'chave_teste'),
        json.dumps(payload)
    )


publisher_amqp = PublisherAMQP(
    os.getenv('AMQP_HOST', '172.17.0.2'),
    os.getenv('AMQP_PORT', 5672)
)

consumer_mqtt = ConsumerMQTT(
    os.getenv('MQTT_HOST', 'localhost'),
    os.getenv('MQTT_PORT', 1883),
    os.getenv('MQTT_KEEPALIVE', 60),
    os.getenv('MQTT_TOPIC', 'topico_teste'),
    on_connect,
    on_message
).config_connect()
