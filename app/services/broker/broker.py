import aio_pika

from app import RABBITMQ_URL, EXCHANGE_NAME


class Broker:
    """RabbitMQ broker"""

    _channel = None
    _exchange = None

    @classmethod
    async def connect(cls):
        """Connect to RabbitMQ"""

        if cls._channel:
            return cls._channel
        try:
            connection = await aio_pika.connect_robust(RABBITMQ_URL)
            channel = await connection.channel()
            cls._channel = channel
            print("Connected to RabbitMQ")
            return channel
        except Exception as err:
            print(f"Failed to connect to RabbitMQ: {err}")

    @classmethod
    async def channel(cls):
        """Create a new channel"""

        if cls._exchange:
            return cls._exchange
        try:
            channel = await cls.connect()
            exchange = await channel.declare_exchange(
                EXCHANGE_NAME, aio_pika.ExchangeType.DIRECT, durable=True
            )
            cls._exchange = exchange
            print("Created RabbitMQ exchange")
            return exchange
        except Exception as err:
            print(f"Failed to create RabbitMQ channel: {err}")
