import os
import discord
from discord.ext import commands

from config import token, prefix


def init_cogs(bot):
    # Get file names from commands folder (removes .py extension and excludes __init__.py)
    cogs = [os.path.splitext(p)[0] for p in os.listdir("commands") if not p.startswith("_")]

    # Loops through and loads cogs
    has_extensions = bool(bot.extensions)
    for cog in cogs:
        bot.reload_extension(f"commands.{cog}") if has_extensions else bot.load_extension(f"commands.{cog}")


if __name__ == "__main__":
    bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix))
    #  Remove default help command so it can be replaced with a custom one
    bot.remove_command("help")

    init_cogs(bot)


    @bot.event
    async def on_ready():
        print(f"DeerBot online! :)\ndiscord.py version:{discord.__version__}")


    bot.run(token)
