import discord
import random
import os

from player import Player
import json

intents = discord.Intents.default()
intents.message_content = True

TOKEN = os.environ.get('DISCORD_TOKEN')

client = discord.Client(intents=intents)

users = []

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}. Preparing user file...')
    


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # TODO Draw Card

    # TODO Play Card

    # TODO Roll Dice
    if message.content.startswith('!rollmydice'):
        result = random.randint(2, 12)
        await message.channel.send(f'*Roll my dice!*\nYou roll two d6.\nThe dice come up {result}.\nIt does nothing.')


if __name__ == '__main__':

    if TOKEN == None:
        print('Token is invalid!')
    else:
        client.run(TOKEN)
