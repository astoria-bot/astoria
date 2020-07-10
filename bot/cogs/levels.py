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
        # Set the cooldown for processing messages from a user
        self._cd = commands.CooldownMapping.from_cooldown(
            1.0, 60.0, commands.BucketType.user)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        '''
        Add new members to the leveling database.
        '''
        self.db.add_user(member.id, member.name, 1, 0, 0)

    @commands.Cog.listener()
    async def on_message(self, msg):
        '''
        Grants user experience points for a message sent every 60 seconds per
        user.
        '''
        # Cooldown for updating user stats in leveling system
        bucket = self._cd.get_bucket(msg)
        retry_after = bucket.update_rate_limit()
        if retry_after:
             # User is rate limited
            pass
        else:
            # User is not rate limited
            msg_sent(msg.author.id, msg.author.name)
          
    
def setup(bot):
    bot.add_cog(Levels(bot))