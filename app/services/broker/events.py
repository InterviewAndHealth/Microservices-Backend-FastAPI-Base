import aio_pika
import json
import logging

from app.services.broker import Broker
from app import EXCHANGE_NAME, SERVICE_QUEUE


class EventService:
    """Publish and subscribe to events"""

    @staticmethod
    async def publish(service: str, data: dict):
        """
        Publish an event to a service

        Parameters
        ----------
        service : str
            The service to publish the event to
        data : dict
            The event data

        Returns
        -------
        None

        Examples
        --------
        >>> await EventService.publish("service", {"key": "value"})
        """
        try:
            exchange = await Broker.channel()
            message = json.dumps(data)
            await exchange.publish(
                aio_pika.Message(body=message.encode()), routing_key=service
            )
            logging.info(f"Published event to {service}: {data}")
        except Exception as err:
            logging.error(f"Failed to publish event: {err}")

    @staticmethod
    async def subscribe(service: str, subscriber):
        """
        Subscribe to events from a service

        Parameters
        ----------
        service : str
            The service to subscribe to
        subscriber : class or object
            The service subscriber with a handle_event method

        Returns
        -------
        None

        Examples
        --------
        >>> class Subscriber:
        ...     @staticmethod
        ...     async def handle_event(message):
        ...         print(message)
        ...
        >>> await EventService.subscribe("service", Subscriber)
        """

        try:
            channel = await Broker.connect()
            queue = await channel.declare_queue(SERVICE_QUEUE, durable=True)
            await queue.bind(exchange=EXCHANGE_NAME, routing_key=service)

            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    async with message.process():
                        data = json.loads(message.body)
                        await subscriber.handle_event(data)

            logging.info(f"Subscribed to service: {service}")
        except Exception as err:
            logging.error(f"Failed to subscribe to service: {err}")
