import discord
import sys
from discord.ext import commands
sys.path.append('./')
from main.bot import *

class LoadCogs(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(name="load", help="Load Commands")
    async def load(self, extension):
        await client.load_extension(f'Commands.{extension}')


def setup(client):
    client.add_cog(LoadCogs(client))


