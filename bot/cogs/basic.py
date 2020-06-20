import discord
from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await dm.send('Welcome {0.name}!'.format(member)) 

def setup(bot):
    bot.add_cog(Basic(bot))