import discord
import sys
from discord.ext import commands
sys.path.append('./')
from main.bot import *


class Purge(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(name="purge", help="Cleans the chat")
    async def purge(self, ctx: commands.Context, amount = 5):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Purge(client))