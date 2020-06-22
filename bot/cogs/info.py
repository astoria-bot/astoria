import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="about")
    async def about(self, ctx):
        '''
        Displays a description about the bot.
        '''
        await ctx.send(
            "Hi I'm astoria! I'm a Discord bot made with Discord.py."
        )


def setup(bot):
    bot.add_cog(Info(bot))