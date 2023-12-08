"""Startup code for astoria bot."""
from os import listdir
import logging
import asyncio
import discord

from discord.ext import commands

from bot.utils.common import BotConstants, DiscordConstants


# Set severity level of logs to display
logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Set status to be displayed on Discord
activity = discord.Game(BotConstants.STATUS)
bot = commands.Bot(
    command_prefix=BotConstants.PREFIX,
    activity=activity,
    status=discord.Status.online,
    intents=intents,
)


async def load_extensions() -> None:
    """Load cogs from cogs/ directory"""
    logging.info("Loading cogs...")
    for file in listdir("bot/cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            cog_name = f"cogs.{name}"
            try:
                await bot.load_extension(cog_name)
            except commands.ExtensionNotFound as err:
                logging.error("Cannot find %s: %s", cog_name, err)
            except commands.ExtensionAlreadyLoaded as err:
                logging.warning("%s has already been loaded: %s", cog_name, err)
            except commands.NoEntryPointError as err:
                logging.error("%s is missing a setup function: %s", cog_name, err)
            except commands.ExtensionFailed as err:
                logging.error("%s had an execution error: %s", cog_name, err)
            else:
                logging.info("Loaded %s", cog_name)


async def main() -> None:
    """Load extensions and start bot"""
    await load_extensions()
    await bot.start(DiscordConstants.TOKEN)


@bot.event
async def on_ready() -> None:
    """Launch bot and connect to specified Discord server."""
    try:
        logging.info("%s has connected to Discord!", bot.user)
    except AttributeError as err:
        logging.error(
            "An error occured. "
            "Please check your '.env' file for incorrect variables.\n"
            "Error message: %s",
            err,
        )
        return
    logging.info("All setup tasks are completed! astoria is good to go!")

# Run the bot
if __name__ == "__main__":
    # Run the main function using the default event loop
    asyncio.run(main())
