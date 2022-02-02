# Import discord package
import json
import os
import sys
from datetime import datetime
from os.path import dirname, join
from random import choice

import discord
import matplotlib.pyplot as plt
from discord.ext import commands, tasks
from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI

sys.path.append('./')

# Get discord Token
dotenv_path = join(dirname(""), '.env')
load_dotenv(dotenv_path)
TOKEN = os.environ.get("DISCORD_TOKEN")

# crypto API
cg = CoinGeckoAPI()

# Get Date and time
now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")

# Update Database
list = cg.get_coins_list()
with open('Data/data.json', 'w') as f:
    json.dump(list, f)

# client (bot)
client = commands.Bot(command_prefix="!", case_insensitive=True, help_command=None)
GUILD = os.getenv('DISCORD_GUILD')
status = ["Mario Kart", "Wii", "Nintendo DS", "Game Cube"]

#Load events
for efilename in os.listdir('./Events'):
    if efilename.endswith('.py'):
        client.load_extension(f'Events.{efilename[:-3]}')

#Load Commands
for filename in os.listdir('./Commands'):
    if filename.endswith('.py'):
        client.load_extension(f'Commands.{filename[:-3]}')

# Run de client on the server
client.run(TOKEN)
