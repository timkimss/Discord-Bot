import discord
from discord.ext import commands

import urllib.request
import json

import random

import project1
import project_cass

import cassiopeia as cass
from cassiopeia import Summoner, MatchHistory, Match



api = 'RGAPI-d5f0cdd8-82d0-4114-89cc-e42cfbe7dbbd'

client = commands.Bot(command_prefix = '.')
token = 'NjYzODY4NTkzNjI0MzE3OTUy.XhPUYw.jDS7MxphuvWPeCwcjZEd-QTrk9o'
channel = client.get_channel(663868923292418080)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server.")
    

@client.event
async def on_member_remove(member):
    print(f"{member} has been removed from the server.")
   
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')


@client.command()
async def foo(ctx, *, arg):
    await ctx.send(arg)


@client.command()
async def printAccountId(ctx):
    id = project1.get_AccountId("GammaRays123")
    await ctx.send(id)

@client.command()
async def printGames(ctx):
    id = 'VGBu0lWyajmEzhQeiQsRLzFQzfcW9WJ8nSUul1G5q7WhIIk'
    games = project1.arams_ranked_total_games_on_account(id)
    total = games['total']
    await ctx.send(total)


@client.command()
async def totalGames(ctx, queue, *, summonerName):
    player = Summoner(name = str(summonerName))
    history = player.match_history

    arams = 0
    ranked = 0
    total = 0

    for Match in history:
        total += 1
        if str(Match.queue) == 'Queue.ranked_solo_fives':
            ranked += 1
        elif str(Match.queue) == 'Queue.aram':
            arams += 1
    games = {
        'aram' : arams,
        'ranked' : ranked,
        'total' : total
    }
    await ctx.send(str(summonerName) + " has played " + str(games[queue]) + ' ' + str(queue) + ' games')


    
@client.command()
async def arams(ctx, *, summonerName):
    id = project1.get_AccountId(summonerName)
    games = project1.arams_ranked_total_games_on_account(id)
    arams = games['aram']
    await ctx.send(arams)

@client.command(aliases = ['8ball', '8b'])
async def eight_ball(ctx, *, question):
    responses = [
        'Yes',
        'For sure!',
        'Maybe',
        'Unlikely',
        'No'
    ]

    await ctx.send(f'Question" {question} \n Anwer: {random.choice(responses)}')

@client.command()
async def clear (ctx, number = 5):
    await ctx.channel.purge(limit = number)











client.run(token)