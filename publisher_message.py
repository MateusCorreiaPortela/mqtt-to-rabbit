from connections.mqtt_builder_connection import PublisherMQTT
from random import randint
import arrow
import os
import json


example_payload = {
    "id": "HA1U2E4OA",
    "date": str(arrow.now().format('YYYY-MM-DD HH:mm:ss')),
    "clock": 2548,
    "flow": 2.14,
    "count_1": randint(1, 400),
    "count_2": randint(1, 400),
    "count_3": randint(1, 400),
}

publisher = PublisherMQTT(
    os.getenv('HOST', 'emqx'),
    os.getenv('PORT', 1883),
    os.getenv('KEEPALIVE', 60),
    os.getenv('TOPIC', 'topico_teste')
).publisher(json.dumps(example_payload))
