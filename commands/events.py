from discord.ext import commands
from queries import create_guild_if_new


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        guild = {
            '_id': message.guild.id
        }
        create_guild_if_new(guild)


def setup(bot):
    bot.add_cog(Events(bot))
