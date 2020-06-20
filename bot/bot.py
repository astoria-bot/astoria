import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='-')

# List of cogs/extensions for the bot to load
extensions = [
    'cogs.games'
]

@bot.event
async def on_ready():
    '''
        Displays specific information about the server the bot is connected to.
    '''
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} has connected to Discord!\n'
        f'{bot.user} is connected to the following guild: '
        f'{guild.name}(id: {guild.id})'
    )

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
    await guild.channel.send("Welcome!")

# @bot.command(name='create-channel')
# @commands.has_role('admin')
# async def create_channel(ctx, channel_name='test'):
#     guild = ctx.guild
#     existing_channel = discord.utils.get(guild.channels, name=channel_name)
#     if not existing_channel:
#         print(f'Creating a new channel: {channel_name}')
#         await guild.create_text_channel(channel_name)

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
