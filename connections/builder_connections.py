import paho.mqtt.client as mqtt
from time import sleep


class ConsumerMQTT:
    def __init__(
        self, host, port,
        keepalive, topic,
        on_connect, on_message
    ):
        self.client = mqtt.Client()
        self.host = host,
        self.port = port,
        self.keepalive = keepalive,
        self.topic = topic,
        self.on_connect = on_connect
        self.on_message = on_message,

    def config_connect(self):
        self.client.connect(
            self.host,
            self.port,
            self.keepalive
        )
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.loop_forever()

    def subiscribe_topic(self):
        self.client.subscribe(self.topic)


class PublisherMQTT:
    def __init__(self, host, port, keepalive, topic):
        self.client = mqtt.Client()
        self.client.connect(
            host, port, keepalive
        )
        self.topic = topic

    def publisher(self, payload):
        self.client.loop_start()
        for i in range(3):
            self.client.publish(
                self.topic, payload
            )
            sleep(10)

        self.client.loop_stop()
