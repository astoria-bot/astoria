import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

STATUS = "!help"      # Set bot status message here
PREFIX = "!"          # Prefix to trigger bot commands on Discord

load_dotenv()

# Loaded from separate .env file
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("DISCORD_GUILD")
MAIN_CHANNEL = int(os.getenv("CHANNEL_ID")) # Main channel for the bot to post messages

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    """Launches bot and connects to Discord server based on
    information in '.env' file."""
    try:
        print(
            f"{bot.user} has connected to Discord!\n"
        )
    except AttributeError as err:
        print(
            "An error occured. "
            "Please check your '.env' file for incorrect variables.\n"
            "Error message: ", err)
        return
    # Set status to be displayed on Discord
    game = discord.Game(STATUS)
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("All setup tasks are completed! astoria is good to go!")

@bot.event
async def setup_hook() -> None:
    """Loads extensions/cogs from 'cogs/' folder"""
    print("Loading extensions...")
    for file in os.listdir("bot/cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            # TODO: Improve the system to catch cog related exception errors
            try:
                await bot.load_extension(f"cogs.{name}")
            except Exception as err:
                print("ERROR! Unable to load " + f"cogs.{name}\n" + f"Error msg: {err}")
            else:
                print("Loading " + f"cogs.{name}")

bot.run(TOKEN)
