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

test_player = Player("Cody", [], [], 53)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}. Preparing user file...')
    


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # TODO Draw Card
    if message.content.startswith('!draw'):
        card = test_player.draw()
        test_player.hand.append(card)

        print(test_player.hand)
        await message.channel.send(f"You drew {card.name}!")

    # TODO Play Card
    if message.content.startswith('!play'):
        for card in test_player.hand:
            if card.name.lower() in message.content.lower():
                card.card_effect()
                test_player.hand.remove(card)
                


    # TODO Roll Dice
    if message.content.startswith('!rollmydice'):
        result = random.randint(2, 12)
        await message.channel.send(f'*Roll my dice!*\nYou roll two d6.\nThe dice come up {result}.\nIt does nothing.')


if __name__ == '__main__':

    if TOKEN == None:
        print('Token is invalid!')
    else:
        client.run(TOKEN)
