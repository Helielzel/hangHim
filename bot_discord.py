# bot_discord.py
# By Gaëtan "Helielzël" CHAUGNY

import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

import create_board as bd

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='$')

###game###

gameBoard = {
    "a10" : ["black", "p", "p2"],
    "b10" : ["white", "", ""],
    "c10" : ["black", "p", "p2"],
    "d10" : ["white", "", ""],
    "e10" : ["black", "p", "p2"],
    "f10" : ["white", "", ""],
    "g10" : ["black", "p", "p2"],
    "h10" : ["white", "", ""],
    "i10" : ["black", "p", "p2"],
    "j10" : ["white", "", "p2"],
    
    "a9" : ["white", "", ""],
    "b9" : ["black", "p", "p2"],
    "c9" : ["white", "", ""],
    "d9" : ["black", "p", "p2"],
    "e9" : ["white", "", ""],
    "f9" : ["black", "p", "p2"],
    "g9" : ["white", "", ""],
    "h9" : ["black", "p", "p2"],
    "i9" : ["white", "", ""],
    "j9" : ["black", "p", "p2"],
    
    "a8" : ["black", "p", "p2"],
    "b8" : ["white", "", ""],
    "c8" : ["black", "p", "p2"],
    "d8" : ["white", "", ""],
    "e8" : ["black", "p", "p2"],
    "f8" : ["white", "", ""],
    "g8" : ["black", "p", "p2"],
    "h8" : ["white", "", ""],
    "i8" : ["black", "p", "p2"],
    "j8" : ["white", "", "p2"],
    
    "a7" : ["white", "", ""],
    "b7" : ["black", "p", "p2"],
    "c7" : ["white", "", ""],
    "d7" : ["black", "p", "p2"],
    "e7" : ["white", "", ""],
    "f7" : ["black", "p", "p2"], 
    "g7" : ["white", "", ""],
    "h7" : ["black", "p", "p2"], 
    "i7" : ["white", "", ""],
    "j7" : ["black", "p", "p2"],

    "a6" : ["black", "", ""],
    "b6" : ["white", "", ""],
    "c6" : ["black", "", ""],
    "d6" : ["white", "", ""],
    "e6" : ["black", "", ""],
    "f6" : ["white", "", ""],
    "g6" : ["black", "", ""],
    "h6" : ["white", "", ""],
    "i6" : ["black", "", ""],
    "j6" : ["white", "", ""],

    "a5" : ["white", "", ""],
    "b5" : ["black", "", ""],
    "c5" : ["white", "", ""],
    "d5" : ["black", "", ""],
    "e5" : ["white", "", ""],
    "f5" : ["black", "", ""],
    "g5" : ["white", "", ""],
    "h5" : ["black", "", ""],
    "i5" : ["white", "", ""],
    "j5" : ["black", "", ""],

    "a4" : ["black", "p", "p1"],
    "b4" : ["white", "", ""],
    "c4" : ["black", "p", "p1"],
    "d4" : ["white", "", ""],
    "e4" : ["black", "p", "p1"],
    "f4" : ["white", "", ""],
    "g4" : ["black", "p", "p1"],
    "h4" : ["white", "", ""],
    "i4" : ["black", "p", "p1"],
    "j4" : ["white", "", ""],

    "a3" : ["white", "", ""],
    "b3" : ["black", "p", "p1"],
    "c3" : ["white", "", ""],
    "d3" : ["black", "p", "p1"],
    "e3" : ["white", "", ""],
    "f3" : ["black", "p", "p1"],
    "g3" : ["white", "", ""],
    "h3" : ["black", "p", "p1"],
    "i3" : ["white", "", ""],
    "j3" : ["black", "p", "p1"],

    "a2" : ["black", "p", "p1"],
    "b2" : ["white", "", ""],
    "c2" : ["black", "p", "p1"],
    "d2" : ["white", "", ""],
    "e2" : ["black", "p", "p1"],
    "f2" : ["white", "", ""],
    "g2" : ["black", "p", "p1"],
    "h2" : ["white", "", ""],
    "i2" : ["black", "p", "p1"],
    "j2" : ["white", "", ""],

    "a1" : ["white", "", ""],
    "b1" : ["black", "p", "p1"],
    "c1" : ["white", "", ""],
    "d1" : ["black", "p", "p1"],
    "e1" : ["white", "", ""],
    "f1" : ["black", "p", "p1"],
    "g1" : ["white", "", ""],
    "h1" : ["black", "p", "p1"],
    "i1" : ["white", "", ""],
    "j1" : ["black", "p", "p1"]
}

player1 = "Edmond"
player2 = "Pascal"
turn = "p1"
loser = "p1"
winner = "p2"
game_status = 0

##########

@client.event
async def on_ready():
    print("Bot is ready")

@client.command(name='tambouille')
async def printHelp(ctx):
    await ctx.send("$dames : start a game\n$ff : surender\n$move departure arrival : move a pawn\n$turn : know which player have to play")

@client.command(name='dames')
async def launch_game(ctx):
    global game_status
    global player1
    global player2
    global turn
    
    player1 = ctx.author
    player2 = ctx.author
    turn = player1
    game_status = 1
    
    await ctx.send("Ok, let's play.\n" + str(player1) + ", YOUR MOVE ! (you play whites)")
    bd.create_board(gameBoard)
    await ctx.send(file=discord.File('img/coucou.png'))
    return

@client.command(name='connard')
async def mpf(ctx):
    await ctx.send("Pas ma faute si je suis codé avec le cul.")
    return

@client.command(name='duel')
async def duel_mod(ctx, user: discord.Member = None):
    global player2
    global game_status

    if game_status == 0:
        await ctx.send("As you wish, but game hasn't started yet...")
        return
    if ctx.author != player1:
        await ctx.send("It's not up to you to decide to come and play.")
        return
    if user:
        await ctx.send("So " + str(user.name) + " , you are player 2 ! (you play blacks)")
        player2 = user.name
    else:
        await ctx.send("Yeah, but who do you want to play with ?")
        return
    return

@client.command(name='ff')
async def forfeit(ctx):
    global game_status
    if game_status == 0:
        await ctx.send("As you wish, but game hasn't started yet...")
        return
    loser = ctx.author
    if loser == player1:
        winner = player2
    else:
        winner = player1 
    await ctx.send("Ah, le nul ! " + str(loser) + " yields, " + str(winner) + " is the winner !")
    game_status = 0
    return

@client.command(name='move')
async def nextMove(ctx, arg1, arg2):
    global game_status
    global turn
    checker = 0

    if game_status == 0:
        await ctx.send("Game hasn't started yet...")
        return
    if turn == ctx.author:
        #await ctx.send("So you want to move " + str(arg1) + " pawn in " + str(arg2) + "...")
        if player1 == ctx.author:
            checker = "p1"
        else:
            checker = "p2"
        # is the key good ? does the pawn belong to the player ? 
        if str(arg1) not in gameBoard or gameBoard[str(arg1)][2] != checker:
            await ctx.send("Wrong coord / Not your pawn")
            return
        
        #checks everything (pawn, queen, color, move, eat)
        if is_move_possible(str(arg1), str(arg2)) != "ok":
            await ctx.send("This move isn't available (not sure yet)")
            return


        move_piece(str(arg1), str(arg2), checker)

        #WINDOW
        bd.create_board(gameBoard)
        await ctx.send(file=discord.File('img/coucou.png'))

        if (gameOver() != "no"):
            game_status = 0
            return
        turn = player2
    else:
        await ctx.send(str(ctx.author) + " , It's not your turn !")
    return

@client.command(name='turn')
async def whichTurn(ctx):
    await ctx.send(str(turn) + ", it's your turn")
    return

#FUNCTIONS

def is_move_possible(arg1, arg2):
    dico_alpha = { "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10}

    splitted_arg1 = list()
    splitted_arg1.append(arg1[0])
    splitted_arg1.append(arg1[1])
    try:
        splitted_arg1.append(arg1[2])
    except:
        pass
    splitted_arg2 = list()
    splitted_arg2.append(arg2[0])
    splitted_arg2.append(arg2[1])
    try:
        splitted_arg2.append(arg1[2])
    except:
        pass

    if pawn_move(arg1, arg2, dico_alpha, splitted_arg1, splitted_arg2) != "ok":
        return ("nope")
    return ("ok")


def move_piece(arg1, arg2, checker):
    gameBoard[arg1][1] = ""
    gameBoard[arg1][2] = ""
    gameBoard[arg2][1] = "p"
    gameBoard[arg2][2] = checker
    return

def pawn_move(arg1, arg2, dico_alpha, splitted_arg1, splitted_arg2):
    color = 0

    if gameBoard[arg2][0] == "white" or gameBoard[arg2][1] == "d" or gameBoard[arg2][1] == "p":
        print("move is not possible, invalid destination")
        return ("error")

    color = -1 if gameBoard[arg1][0] == "black" else 1

    if ((int(splitted_arg2[1]) + color == int(splitted_arg1[1])) and (dico_alpha[splitted_arg2[0]] - dico_alpha[splitted_arg1[0]] == 1 or dico_alpha[splitted_arg2[0]] - dico_alpha[splitted_arg1[0]] == -1)):
        print("Pion qui bouge")
        return ("ok")
    return ("nope")

def gameOver():
    p1_pawns = 0
    p2_pawns = 0

    for key in gameBoard:
        if (gameBoard[key][1] == 'p' or gameBoard[key][1] == 'd') and gameBoard[key][2] == 'p1':
            p1_pawns += 1
        if (gameBoard[key][1] == 'p' or gameBoard[key][1] == 'd') and gameBoard[key][2] == 'p2':
            p2_pawns += 1
    print("p1 has " + str(p1_pawns) + " pawns left")
    print("p2 has " + str(p2_pawns) + " pawns left")

    if p1_pawns == 0:
        print("p2 is the winner")
        return ("p2")
    elif p2_pawns == 0:
        print("p1 is the winner") 
        return ("p1")
    else:
        print("Game is not over yet")
        return ("no")

def DEBUG_emptyBoard():
    for key in gameBoard:
        gameBoard[key][1] = ""
        gameBoard[key][2] = ""


client.run(TOKEN)