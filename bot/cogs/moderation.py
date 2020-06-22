import discord
from discord.ext import commands


class Moderation(commands.Cog):
    '''
    Moderation tools for astoria.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        '''
        Kicks a user from the server.
        Usage: !kick [username]
        '''
        await member.kick()
        await ctx.send(discord.Member.display_name)

    @commands.has_permissions(manage_channels=True)
    @commands.command(name='new-channel')
    async def new_channel(self, ctx, channel_name='text channel'):
        '''
        Creates new text channel.
        Usage: !new-channel [name (optional)]
        '''
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_text_channel(channel_name)


def setup(bot):
    bot.add_cog(Moderation(bot))
