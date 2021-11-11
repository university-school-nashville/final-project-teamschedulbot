# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:08:13 2021

@author: alexb
"""

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTA3NjcyMDQ2ODY2MTYxNzA0.YYqldw.8OfrjdReSQgRQGExSfOMywcwsR4')