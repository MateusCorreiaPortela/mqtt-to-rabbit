import os
import json
from connections.builder_connections import ConsumerMQTT
from parsers.parser_packet import parser_mqtt


def on_connect(client, userdata, rc):
    print(f'\033[1;32mConectado ao Broker MQTT\033[m: {rc}')
    consumer_mqtt.subiscribe_topic()


def on_message(client, userdat, msg):
    print(f'\033[1;34mTOPIC\033[m]: {msg.topic}')
    print(f'\033[1;34mMENSAGEM RECEBIDA: {msg.payload}')

    payload = json.loads(msg.payload)

    if not (parse_payload := parser_mqtt(payload)):
        return


consumer_mqtt = ConsumerMQTT(
    os.getenv('HOST', 'localhost'),
    os.getenv('PORT', 1883),
    os.getenv('KEEPALIVE', 60),
    os.getenv('TOPIC', 'topico_teste'),
    on_connect,
    on_message
).config_connect()
