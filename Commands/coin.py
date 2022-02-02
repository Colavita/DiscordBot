import discord
import json
import datetime
from discord.ext import commands
import sys
sys.path.append('./')
from main.bot import *

class CryptoCoin(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(name="coin", help="Gives coin price")
    async def coin(self, ctx: commands.Context, arg):
        arg = arg.lower()
        database = "Data/data.json"
        data = json.loads(open(database).read())
        coinName = arg
        for i in data:
            if str(i["symbol"]).lower() == arg:
                coinName = str(i["name"]).lower()
                message = cg.get_price(ids=coinName, vs_currencies='usd')
                break
            elif str(i["name"]).lower() == arg:
                message = cg.get_price(ids=arg, vs_currencies='usd')
                break
        message2 = str(message).replace("'", '"')
        realMessage = json.loads(message2)
        coin = coinName.capitalize()
        await ctx.message.channel.send(coin + " price is $" + str("{:,}".format(realMessage[coinName]["usd"]) + " USD"))


def setup(client):
    client.add_cog(CryptoCoin(client))