import discord
import sys
from discord.ext import commands
sys.path.append('./')
from main.bot import *


class Ticker(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @ commands.command(name="ticker", help="Gives coin ticker")
    async def ticker(self, ctx: commands.Context):
        x = ctx.message.content.lower()
        a = x.split()
        database = "Data/data.json"
        data = json.loads(open(database).read())

        for i in data:
            if str(i["name"]).lower() == a[1]:
                print(i["id"])  # name with dashes for api requests
                await ctx.send("The ticker for this coin is: " + str(i["symbol"]).upper())
                break

def setup(client):
    client.add_cog(Ticker(client))