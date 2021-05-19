# hanghim.py
# By Gaëtan "Helielzël" CHAUGNY

##   https://discord.com/developers/applications/844702707650134046/information

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command(name='hanghelp')
async def printHelp(ctx):
    await ctx.send("$hang : start a solo game")

client.run(TOKEN)
