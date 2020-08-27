from discord.ext import commands

from deerbot import init_cogs
from decorators import is_bot_owner


class Management(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @is_bot_owner
    async def restart(self, ctx):
        pass

    @commands.command()
    @is_bot_owner
    async def shutdown(self, ctx):
        """Logout and shut down the bot."""
        await ctx.bot.logout()

    @commands.command()
    @is_bot_owner
    async def reload(self, ctx):
        """Reload the cogs found in the commands folder."""
        init_cogs(self.bot)
        await ctx.send("Cogs have been reloaded.")

    @commands.command()
    @is_bot_owner
    async def list_servers(self, ctx):
        """Sends a list of the servers the bot has joined"""
        message = ""
        for server in self.bot.guilds:
            message += f"{server.name} | {server.id}"
        await ctx.send(f"```{message}```")

    @commands.command()
    @is_bot_owner
    async def leave(self, ctx):
        """Makes the bot leave the server"""
        await ctx.send("Leaving the server... Bye!")
        await ctx.guild.leave()


def setup(bot):
    bot.add_cog(Management(bot))
