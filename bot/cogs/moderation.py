import discord
from discord.ext import commands


class Moderation(commands.Cog):
    '''
    Moderation Tools for astoria.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        '''
        Kicks a user from the server.
        '''
        try:
            await member.kick()
            await ctx.send("Kicking")
        except BadArgument:
            await ctx.send("Member does not exist")

def setup(bot):
    bot.add_cog(Moderation(bot))