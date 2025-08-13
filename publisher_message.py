from connections.builder_connections import PublisherMQTT
import os
import json


example_payload = {
    "id": "HA1U2E4OA",
    "date": "2025-04-24 11:57:03",
    "clock": 2548,
    "flow": 2.14
}

publisher = PublisherMQTT(
    os.getenv('HOST', 'localhost'),
    os.getenv('PORT', 1883),
    os.getenv('KEEPALIVE', 60),
    os.getenv('TOPIC', 'topico_teste')
).publisher(json.dumps(example_payload))
