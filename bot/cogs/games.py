import random
import asyncio
from discord.ext import commands


class Games(commands.Cog):
    """Minigames"""
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 5, type=commands.BucketType.guild)
    @commands.command()
    async def flip(self, ctx):
        """Flips a coin! Heads or tails?
        Usage: !flip"""
        coin_sides = ["Heads!", "Tails!"]
        result = random.choice(coin_sides)
        await ctx.send("Flipping a coin...")
        await ctx.typing()
        await asyncio.sleep(2)
        await ctx.send(result)

    @commands.cooldown(1, 5, type=commands.BucketType.guild)
    @commands.command(name="8ball")
    async def eight_ball(self, ctx, question: str = None):
        """Ask the magic 8-ball for an answer to a question.
        Usage: !8ball [question]"""
        responses = [
            "As I see it, yes.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don’t count on it.",
            "It is certain.",
            "It is decidedly so.",
            "Most likely.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Outlook good.",
            "Reply hazy, try again.",
            "Signs point to yes.",
            "Very doubtful.",
            "Without a doubt.",
            "Yes.",
            "Yes – definitely.",
            "You may rely on it."
        ]
        if question is None:
            await ctx.send("Please ask me a question.")
            return
        result = random.choice(responses)
        await ctx.send("Let me see...")
        await ctx.trigger_typing()
        await asyncio.sleep(2)
        await ctx.send(result)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Games(bot))
