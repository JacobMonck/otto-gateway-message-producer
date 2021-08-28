import json
from asyncio import AbstractEventLoop
from typing import Optional

import aio_pika
from aio_pika import Channel, Message
from aio_pika.connection import Connection
from loguru import logger as log

from src.constants import Config


class RabbitMQ:
    """A class to connect to RabbitMQ"""

    def __init__(self, loop: AbstractEventLoop):
        self.loop = loop
        self.connection: Optional[Connection] = None
        self.channel: Optional[Channel] = None

    async def connect(self) -> None:
        """A function to connect to RabbitMQ and create a channel."""
        self.connection = await aio_pika.connect_robust(
            Config.rabbitmq_url,
            loop=self.loop
        )
        log.info("Connected to RabbitMQ")

        self.channel = await self.connection.channel()
        await self.channel.declare_queue(Config.routing_key)

    async def publish(self, message: dict) -> None:
        """Publishes a message to the message queue."""
        json_object = json.dumps(message, indent=1)

        await self.channel.default_exchange.publish(
            Message(body=json_object.encode()),
            routing_key=Config.routing_key
        )
