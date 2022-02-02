import discord
import sys
from discord.ext import commands
sys.path.append('./')
from main.bot import *

class UnLoadCogs(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(name="unload", help="Unload Commands")
    async def unload(self, extension):
        client.unload_extension(f'Commands.{extension}')


def setup(client):
    client.add_cog(UnLoadCogs(client))