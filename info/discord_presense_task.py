from core import status
from discord.ext import tasks, commands
from core import bot
import discord

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(
            next(
                status
            )
        )
    )

