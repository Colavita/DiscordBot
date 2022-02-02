import discord
import sys
from discord.ext import commands
sys.path.append('./')
from main.bot import *

class Help(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(name="help", description="Gives more info on the bot")
    async def help(self, ctx: commands.Context):
        myEmbed = discord.Embed(title="Smeje Bot",
                                description="Version 1.0", color=0xff0000)
        myEmbed.set_thumbnail(url="https://img.icons8.com/fluency/344/chatbot.png")
        myEmbed.add_field(name="Date Started",
                        value="December 29, 2020", inline=False,)
        myEmbed.set_author(name="Matteo Colavita", icon_url="https://img.icons8.com/office/344/person-male.png")
        helptext = "```"
        for command in client.commands:
            helptext += f"{command}\n"
        helptext += "```"
        await ctx.send(embed=myEmbed)
        await ctx.send(helptext)

def setup(client):
    client.add_cog(Help(client))