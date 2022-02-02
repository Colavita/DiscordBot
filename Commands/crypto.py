import discord
import json
import datetime
from discord.ext import commands
import sys
sys.path.append('./')
from main.bot import *

class Crypto(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(name="crypto", help="Crypto Price")
    async def crypto(self, ctx: commands.Context):
        message = cg.get_price(
            ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
        message2 = str(message).replace("'", '"')
        realMessage = json.loads(message2)
        await ctx.message.channel.send("@ " + current_time + "\n\n" + "Bitcoin price is $" + str("{:,}".format(realMessage["bitcoin"]["usd"])) + " USD" + "\n" + "Ethereum price is $" + str(("{:,}".format(realMessage["ethereum"]["usd"]))) + " USD" + "\n" + "Litecoin price is $" + str("{:,}".format(realMessage["litecoin"]["usd"]) + " USD"))

def setup(client):
    client.add_cog(Crypto(client))