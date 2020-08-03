import os
import discord
from discord.ext import commands

from config import token, prefix

bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix))
#  Remove default help command so it can be replaced with a custom one
bot.remove_command("help")
# Get file names from commands folder (removes .py extension and excludes __init__.py)
cogs = [os.path.splitext(p)[0] for p in os.listdir("commands") if not p.startswith("_")]

# Loops through and loads cogs
for cog in cogs:
    bot.load_extension(f"commands.{cog}")


@bot.event
async def on_ready():
    print(f"DeerBot online! :)\ndiscord.py version:{discord.__version__}")


bot.run(token)
