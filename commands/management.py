from discord.ext import commands

from deerbot import init_cogs


class Management(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def restart(self, ctx):
        pass

    @commands.command()
    async def shutdown(self, ctx):
        """Logout and shut down the bot."""
        await ctx.bot.logout()

    @commands.command()
    async def reload(self, ctx):
        """Reload the cogs found in the commands folder."""
        init_cogs(self.bot)

    @commands.command()
    async def list_servers(self, ctx):
        """Sends a list of the servers the bot has joined"""
        message = ""
        for server in self.bot.guilds:
            message += f"{server.name} | {server.id}"
        await ctx.send(f"```{message}```")

    @commands.command()
    async def leave(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Management(bot))
