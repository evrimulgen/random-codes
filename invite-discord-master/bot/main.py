import json

import discord
import asyncio
import requests
from discord.ext import commands

from constants import *

client = discord.Client()

async def get_invites():
    # TODO: Implement process invites logic
    await client.wait_until_ready()
    invite_endpoint = DISCORD_API_BASE_URL + '/guilds/%s/invites' % TEST_GUILD_ID
    headers = {'Authorization': 'Bot ' + DISCORD_API_KEY}
    r = requests.get(invite_endpoint, headers=headers)
    invites = json.loads(r.text)
    await asyncio.sleep(30)  # Check invites every 30 seconds

@client.event
async def on_message(message, *args, **kwargs):
    if message.content.startswith('!test'): # Only accept command for the selected role
        if "admin2" in [role.name.lower() for role in message.author.roles]:
            text = message.content.split(' ')[1:]
            text = ' '.join(text)
            await client.send_message(message.channel, text)
            return
            # await client.send_message(discord.Object(id='403241216180748288'), text)
            # await asyncio.sleep(5)
            # await client.send_message(discord.Object(id='403241234891800576'), text)
            # await asyncio.sleep(10)
            # await client.send_message(discord.Object(id='403241255611531265'), text)
            # await asyncio.sleep(20)
    # elif message.content.startswith('!ch'):
    #     text = message.content.split(' ')[1:]
    #     text = ' '.join(text)
    #     await client.send_message(message.channel, text)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    for server in client.servers:
        print(server.id)
    print('------')

client.loop.create_task(get_invites())
client.run(DISCORD_API_KEY)
