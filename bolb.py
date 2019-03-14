import discord
from discord.ext import commands
import random
import requests
import random
import asyncio
import aiohttp
import traceback
import sys
import json
import random
import datetime
import time
import os
import subprocess

discordBotToken = "NTU1NzQxMTM4NDE0MjA2OTc2.D2wjFA.o-XAgmCsa4lqEb2VpUgJma-Z_bQ"


client = commands.Bot(command_prefix = '!')

#IN MY DISCORD SERVER, WE HAVE ROLES EVERY 10 LVL RANGE, THAT'S WHY I CHECK FOR THESE LEVEL RANGES
def getLevelRoleName(level):
	if (level>=0 and level <10):
		return "0-10"
	elif (level>=10 and level <20):
		return "10-20"
	elif (level>=20 and level <30):
		return "20-30"
	elif (level>=30 and level <40):
		return "30-40"
	elif (level>=40 and level <50):
		return "40-50"
	elif (level>=50 and level <60):
		return "50-60"
	elif (level>=60 and level <70):
		return "60-70"
	elif (level>=70 and level <80):
		return "70-80"
	elif (level>=80 and level <90):
		return "80-90"
	elif (level>=90 and level <100):
		return "90-100"
	elif (level>=100):
		return "Lenda"


def getRoleToAdd(roleName,roles):
	for role in roles:
		if roleName in role.name:
			return role

def getRolesToRemove(roles):
	rolesToRemove = []
	for role in roles:
		if ("-" in role.name):
			rolesToRemove.append(role)
	return rolesToRemove

def getPlatformId(platform):
	if(platform == "pc" or platform == "PC"):
		return 5
	elif (platform == "xbox" or platform == "XBOX"):
		return 1
	elif (platform == "ps4" or platform == "PS4"):
		return 2


initial_extensions = ['cogs.moderating',
'cogs.apex']

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('Connected to {} servers and {} users | {} shards'.format(len(client.servers), len(set(client.get_all_members())), client.shard_count))
	await client.change_presence(game=discord.Game(name=' !help | {} users'.format(len(set(client.get_all_members())), client.shard_count)))
	print('------')
	# startup channel log
client.remove_command('help')

#activity = discord.Streaming(
	#	 name=f"Just testing",
	#	 url='https://twitch.tv'
	#	 )
#await bot.change_presence(status=discord.Status.online, activity=activity)

# Who dares to use the almighty ping function? The main goal of this entire bot
@client.command(pass_context=True)
async def ping(ctx):
	"""Ping the bot."""
	now = datetime.datetime.utcnow()
	delta = ctx.message.timestamp
	pingtime = now-delta
	embed = discord.Embed(title="Pong! {} ms".format(pingtime), color=0x800080)
	embed.set_author(name="Requested by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	await client.say(embed=embed)
 
   # wherewedroppin command
@client.command(pass_context=True)
async def wherewedroppin(ctx):
	locations = ['https://i.imgur.com/whE3Xej.jpg', 'https://i.imgur.com/vRIbhOL.jpg', 'https://i.imgur.com/xI2dgyR.jpg', 'https://i.imgur.com/tf0Qn5T.jpg']
	embed=discord.Embed(title="Where we droppin'?", color=0x761fa1)
	embed.add_field(name="Location", value=random.choice(locations), inline=False)
	await client.say(embed=embed)

client.run(discordBotToken)
