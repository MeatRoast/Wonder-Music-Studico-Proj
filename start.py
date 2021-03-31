import discord
import time
import datetime
import json
from discord.ext import commands
from discord.ext import commands
from core import *
from command.etc._server import _server
from command.etc._help import _help
from command.etc._invite import _invite

token = config['Token']

@bot.event
async def on_ready():
    change_status.start()
    print('')
    print('')
    print("             Copyright ©2021 MeatRoast Inc. All rights reserve")
    print("             Copyright ©2021 Wonder-Music-Studico. All rights reserve")
    print("             ")
    print('')
    print("         BOT NAME:", bot.user.name)
    print("         BOT Clint ID:", bot.user.id)
    print('')
    print("------------------")

@tasks.loop(seconds=60)
async def change_status():
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(
            next(
                status
            )
        )
    )

if __name__ == '__main__':
    bot.remove_command('help')  
    bot.add_cog(_server(bot))
    bot.add_cog(_help(bot))
    bot.add_cog(_invite(bot))
    bot.run(token)
