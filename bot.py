import discord
import model_user
import time
from discord.ext import tasks
import json
import os
import random

pogaduszki = 847475105519894618

client = discord.Client()

with open('save_okku', 'r', encoding='utf-8') as f:
    model = json.load(f)

@client.event
async def on_ready():
    print('Ready')

@client.event
async def on_message(message):
    if message.channel.id == pogaduszki and random.randrange(0, 100) > 80 and not message.author.bot or client.user.mentioned_in(message):
        print("Message")
        sentence = model_user.generate(model)
        if client.user.mentioned_in(message):
            await message.reply(sentence)
        else:
            await message.channel.send(sentence)


client.run(os.getenv('DISCORD_TOKEN'))