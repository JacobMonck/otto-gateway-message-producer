from asyncio import get_event_loop

from corded import CordedClient, Intents, GatewayEvent
from dotenv import load_dotenv
from loguru import logger as log

from constants import Config
from rabbitmq import RabbitMQ

load_dotenv()

loop = get_event_loop()
bot = CordedClient(Config.token, intents=Intents.all())
rabbit = RabbitMQ(loop)


@bot.on("ready")
async def ready(event: GatewayEvent) -> None:
    log.info("Connected to gateway {}".format(event.d))


class MessageEvents:
    """Handles all gateway events regarding messages."""

    @bot.on("message_create")
    async def on_message_create(self, event: GatewayEvent) -> None:
        data = event.d
        await rabbit.publish(data)

    @bot.on("message_update")
    async def on_message_update(self, event: GatewayEvent) -> None:
        data = event.d
        await rabbit.publish(data)

    @bot.on("message_delete")
    async def on_message_delete(self, event: GatewayEvent) -> None:
        data = event.d
        await rabbit.publish(data)

    @bot.on("message_delete_bulk")
    async def on_bulk_message_delete(self, event: GatewayEvent) -> None:
        data = event.d
        await rabbit.publish(data)

    @bot.on("message_reaction_add")
    async def on_reaction_add(self, event: GatewayEvent) -> None:
        data = event.d
        await rabbit.publish(data)

    @bot.on("message_reaction_remove")
    async def on_reaction_remove(self, event: GatewayEvent) -> None:
        data = event.d
        await rabbit.publish(data)

    @bot.on("message_reaction_remove_all")
    async def on_reaction_remove_all(self, event: GatewayEvent) -> None:
        data = event.d
        await rabbit.publish(data)

    @bot.on("message_reaction_remove_emoji")
    async def on_reaction_remove_emoji(self, event: GatewayEvent) -> None:
        data = event.d
        await rabbit.publish(data)


class GuildEvents:
    @bot.on("guild_update")
    async def on_guild_update(self, event: GatewayEvent) -> None:
        data = event.d
        await rabbit.publish(data)

    @bot.on("guild_delete")
    async def on_guild_delete(self, event: GatewayEvent) -> None:
        data = event.d
        await rabbit.publish(data)

    @bot.on("guild_role_create")
    async def on_guild_role_create(self, event: GatewayEvent) -> None:
        data = event.d
        await rabbit.publish(data)


if __name__ == "__main__":
    loop.run_until_complete(rabbit.connect())
    bot.start()
