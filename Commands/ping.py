import discord
import sys
from discord.ext import commands
sys.path.append('./')
from main.bot import *


class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(name="ping", help="Your latency")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Latency: {round(client.latency * 1000)}ms")

def setup(client):
    client.add_cog(Ping(client))