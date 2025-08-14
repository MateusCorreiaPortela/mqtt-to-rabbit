import pika


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
