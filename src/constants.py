import os
from typing import NamedTuple

from dotenv import load_dotenv

load_dotenv()


class Config(NamedTuple):
    token = os.getenv("BOT_TOKEN")
    rabbitmq_url = os.getenv("RABBITMQ_URL")
    routing_key = os.getenv("ROUTING_KEY")
