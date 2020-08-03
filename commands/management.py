from discord.ext import commands


class Management(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def restart(self):
        pass

    @commands.command()
    async def shutdown(self):
        pass

    @commands.command()
    async def reload(self):
        pass

    @commands.command()
    async def list_servers(self):
        pass

    @commands.command()
    async def leave(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Management(bot))
