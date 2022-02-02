from datetime import datetime
import discord
import os
import matplotlib.pyplot as plt
import json
import sys
from discord.ext import commands
import sys
sys.path.append('./')
from main.bot import *

class CryptoChart(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(name="chart", help="Gives coin chart")
    async def chart(self, ctx: commands.Context, *args):
        database = "Data/data.json"
        data = json.loads(open(database).read())
        coinName = args[0]
        picture = ""
        
        for i in data:
            if str(i["symbol"]).lower() == args[0]:
                coinName = str(i["name"]).lower()
                break
            elif str(i["name"]).lower() == args[0]:
                break

        try:
            picture = cg.get_coin_market_chart_by_id(
                id=coinName, vs_currency='usd', days=args[1])
        except:
            try:
                picture = cg.get_coin_market_chart_by_id(
                    id=coinName, vs_currency='usd', days=1)
            except:
                    await ctx.channel.send("Coin not found!")

        if picture != "":
            f = open("Data\Chart.json", "w")
            f.write(str(picture).replace("'", '"'))
            f.close()
            coin = coinName.capitalize()
            fig, ax = plt.subplots()
            fig.set_size_inches(8, 6)

            ax.plot([datetime.utcfromtimestamp(x[0]/1000) for x in picture['prices']],
                    [x[1] for x in picture['prices']], label=str(coin))

            ax.set_xlabel('Time')
            ax.set_ylabel('Price *US$)')
            ax.legend()
            plt.savefig(str(coin) + "_Chart.png")
            await ctx.channel.send(file=discord.File(str(coin) + "_Chart.png"))
            os.remove(str(coin) + "_Chart.png")


def setup(client):
    client.add_cog(CryptoChart(client))