import random
import asyncio
from discord.ext import commands


class Games(commands.Cog):
    '''
    Minigames
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 5, type=commands.BucketType.guild)
    @commands.command()
    async def flip(self, ctx):
        '''
        Flips a coin! Heads or tails?
        Usage: !flip
        '''
        coin_sides = ['Heads!', 'Tails!']
        result = random.choice(coin_sides)
        await ctx.send('Flipping a coin...')
        await ctx.trigger_typing()
        await asyncio.sleep(2)
        await ctx.send(result)


def setup(bot):
    bot.add_cog(Games(bot))
