# hanghim.py
# By Gaëtan "Helielzël" CHAUGNY

##   https://discord.com/developers/applications/844702707650134046/information

#from _typeshed import OpenTextModeUpdating
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='$')

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

game_status = 0
word = ""
toGuess = list()
mistakes = 0
errorList = ""

@client.event
async def on_ready():
    print("Bot is ready")

@client.command(name='hanghelp')
async def printHelp(ctx):
    await ctx.send("$hang : start a game\n$h [letter]")

@client.command(name='hang')
async def chooseWord(ctx):
    global game_status
    global word
    global toGuess

    if game_status == 1:
        await ctx.send("Guess what was previous word before !")
        return
    await ctx.send("Come on " + str(ctx.author) + ", choose a word with /spoiler")
    word = "prout"
    for elem in word:
        toGuess.append("_")
    toGuess[0] = word[0]
    toGuess[len(word) - 1] = word[len(word) - 1]
    game_status = 1
    toPrint = list()
    for elem in toGuess:
        toPrint.append(elem)
        toPrint.append(" ")
    await ctx.send("The word to guess is : " + "_".join(toPrint))
    return

@client.command(name='h')
async def getLetter(ctx, arg1):
    global mistakes
    global errorList
    global game_status

    letter = str(arg1)
    if len(letter) != 1:
        await ctx.send("Invalid letter proposal")
        return
    if letter in toGuess:
        await ctx.send("This letter was already picked !")
        mistakes += 1
        await ctx.send(HANGMANPICS[mistakes])
        await ctx.send(errorList)
        return
    if letter not in word:
        errorList += letter
        errorList += "-"
        mistakes += 1
        try:
            await ctx.send("Nope !\n" + HANGMANPICS[mistakes])
            await ctx.send("Errors : " + errorList)
            await ctx.send("".join(toGuess))            
        except:
            await ctx.send("Are you taking me for a fool ? You LOOOOST !")
            game_status = 0
            return
        return
    if letter in word:
        for i in range (len(word)):
            if letter == word[i]:
                toGuess[i] = word[i]
    if "_" not in toGuess:
        await ctx.send("YOU DID IT !")
        game_status = 0
        return
    if mistakes != 0:
        await ctx.send(errorList)
    await ctx.send("".join(toGuess))

client.run(TOKEN)