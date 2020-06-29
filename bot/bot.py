import os
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv

status = "!help"      # Set bot status message here

load_dotenv()

# Loaded from separate .env file
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Main channel for the bot to post messages
MAIN_CHANNEL = int(os.getenv('CHANNEL_ID'))

bot = commands.Bot(command_prefix='!')

# Log errors and debug information

# Simple logger setup, outputs to console
logging.basicConfig(level=logging.INFO)     

# More advanced logger setup
# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(
#     filename='discord.log', encoding='utf-8', mode='w'
# )
# handler.setFormatter(logging.Formatter(
#     '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
#     )
# )
# logger.addHandler(handler)

@bot.event
async def on_ready():
    '''
    Displays specific information about the server the bot is connected to.
    Also updates status of the bot.
    '''
    try:
        guild = discord.utils.get(bot.guilds, name=GUILD)
        print(
            f'{bot.user} has connected to Discord!\n'
            f'{bot.user} has connected to the following guild: '
            f'{guild.name}(id: {guild.id})'
        )
    except AttributeError:
        print(
            "An error occured. "
            "Please check your .env file for incorrect variables.")
        return
    # Set status to be displayed on Discord
    game = discord.Game(status)
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("All setup tasks are completed! astoria is good to go!")


# Loads extensions/cogs from cogs folder
print("Loading extensions...")
for file in os.listdir("bot/cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")
        print("Loading " + f"cogs.{name}")
bot.run(TOKEN)
