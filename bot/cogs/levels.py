from discord.ext import commands
from cogs.utils.levelconfig import msg_sent
from cogs.utils.database.methods import Methods
from cogs.utils.database.config import DBConfig

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.engine = DBConfig().get_engine()
        self.metadata = DBConfig().get_metadata()
        self.conn = DBConfig().get_connection()
        self.db = Methods(self.engine, self.metadata, self.conn)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.db.add_user(member.id, member.name, 1, 0, 0)

def setup(bot):
    bot.add_cog(Levels(bot))