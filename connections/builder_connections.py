import paho.mqtt.client as mqtt
import pika
from time import sleep


class ConsumerMQTT:
    def __init__(
        self, host, port,
        keepalive, topic,
        on_connect, on_message
    ):
        self.client = mqtt.Client()
        self.host = host
        self.port = port
        self.keepalive = keepalive
        self.topic = topic
        self.on_connect = on_connect
        self.on_message = on_message

    def config_connect(self):
        self.client.connect(
            self.host,
            self.port,
            self.keepalive
        )
        self.client.subscribe(self.topic)
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


class PublisherAMQP:
    def __init__(
        self,
        host,
        port
    ):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host, port)
        )

        self.channel = self.connection.channel()

    def declarete(self, fila, exchange):
        if not fila:
            return

        self.channel.queue_declare(queue=fila)
        self.channel.exchange_declare(exchange=exchange)

    def queue_bind(self, exchange, queue, routing_key):
        if (
            not exchange
            or not queue
            or not routing_key
        ):
            return

        self.channel.queue_bind(
            exchange=exchange,
            queue=queue,
            routing_key=routing_key
        )

    def basic_publish(self, exchange, routing_key, payload):

        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=payload
        )


class ConsumerAMQP:
    def __init__(
        self,
        host,
        port
    ):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host, port)
        )

        self.channel = self.connection.channel()

    def declarete(self, fila, exchange):
        if not fila:
            return

        self.channel.queue_declare(queue=fila)
        self.channel.exchange_declare(exchange=exchange)

    def queue_bind(self, exchange, queue, routing_key):
        if (
            not exchange
            or not queue
            or not routing_key
        ):
            return

        self.channel.queue_bind(
            exchange=exchange,
            queue=queue,
            routing_key=routing_key
        )

    def channel_basic_consume(self, queue, on_message_callback, auto_ack=True):
        self.channel.basic_consume(
            queue=queue,
            on_message_callback=on_message_callback,
            auto_ack=auto_ack
        )
