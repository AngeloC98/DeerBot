import discord

from config import token

client = discord.Client()


@client.event
async def on_ready():
    print(f"DeerBot online! :)\ndiscord.py version:{discord.__version__}")


client.run(token)
