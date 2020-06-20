import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

status = 'Reading Documentation Hell'       # Set bot status message here

load_dotenv()

# Loaded from separate .env file
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Main channel for the bot to post messages
MAIN_CHANNEL = int(os.getenv('CHANNEL_ID'))

bot = commands.Bot(command_prefix='-')

# List of cogs/extensions for the bot to load
extensions = [
    'cogs.admin',
    'cogs.games'
]


@bot.event
async def on_ready():
    '''
        Displays specific information about the server the bot is connected to.
        Also updates status of the bot.
    '''
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} has connected to Discord!\n'
        f'{bot.user} has connected to the following guild: '
        f'{guild.name}(id: {guild.id})'
    )
    # Set status to be displayed on Discord
    game = discord.Game(status)
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("All setup tasks are completed!")


@bot.event
async def on_member_join(member):
    '''
        Welcomes new members to the server.
    '''
    guild = discord.utils.get(bot.guilds, name=GUILD)
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to {guild.name}!'
    )
    ch = bot.get_channel(MAIN_CHANNEL)
    await ch.send(f'{member.name} has joined the server!')


@bot.event
async def on_command_error(ctx, error):
    '''
        Handles exception errors caused by commands.
    '''
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

if __name__ == "__main__":
    # Loads extensions/cogs
    for ext in extensions:
        try:
            bot.load_extension(ext)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(ext, exc))
    bot.run(TOKEN)
