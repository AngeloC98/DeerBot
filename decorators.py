from discord.ext import commands

from config import bot_owners


@commands.check
async def is_bot_owner(ctx):
    if ctx.author.id not in bot_owners:
        await ctx.send("Only bot owners are allowed to use this command!")
        return False
    return True
