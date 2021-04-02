import discord
from discord.ext import commands
import urllib
import urllib.parse
import json
import asyncio
import random
import asyncio
import psutil
import pybithumb
from discord.ext import commands
from datetime import datetime


class _invite(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='초대', aliases=['초대코드','초대링크'])
    async def _invite(self, ctx):
        embedinvite=(
            discord.Embed(
                title="Wonder-Music-Studico-Proj 초대코드", 
                description="지원하지않",
                color=0xabcee9
            )
            .add_field(
                name="아래 클릭",
                value="[초대하기](link)"
            )
        )
        await ctx.send(
            ctx.author.mention,
            embed=embedinvite
        )
