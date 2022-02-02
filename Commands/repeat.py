import discord
import sys
from discord.ext import commands
sys.path.append('./')
from main.bot import *


class Repeat(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(name="repeat", help="Repeats what you say")
    async def repeat(self, ctx: commands.Context, *args):
        response = ""
        for arg in args:
            response = response + " " + arg

        await ctx.channel.send(response)

def setup(client):
    client.add_cog(Repeat(client))