import discord
from discord.ext import commands


class Admin(commands.Cog):
    '''
        Administrative Tools for Discord.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='create-channel')
    @commands.has_role('admin')
    async def create_channel(self, ctx, channel_name='text channel'):
        '''
            Creates new text channel. 
            Usage: -create-channel [name (optional)]
        '''
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_text_channel(channel_name)

def setup(bot):
    bot.add_cog(Admin(bot))
