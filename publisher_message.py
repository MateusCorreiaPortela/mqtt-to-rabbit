from connections.builder_connections import PublisherMQTT
import os
import json

example_payload = {
    "ID": "HA1U2E4OA",
    "data": "2025-04-24 11:57:03",
    "relogio": 2548,
    "vazao_instantanea": 2.14
}

publisher = PublisherMQTT(
    os.getenv('HOST', 'localhost'),
    os.getenv('PORT', 1883),
    os.getenv('KEEPALIVE', 60),
    os.getenv('TOPIC', 'topico_teste')
).publisher(json.dumps(example_payload))
