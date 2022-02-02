import sys

import discord
from discord.ext import commands, tasks
from main.bot import *

sys.path.append('./')

class Ready(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):

        self.change_status.start()
        print("\n")
        print(f'{client.user} has connected to Discord!')
        print("\n")

        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

    @tasks.loop(seconds=60)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(choice(status)))

def setup(client):
    client.add_cog(Ready(client))
