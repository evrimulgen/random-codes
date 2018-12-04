import json

import discord
import asyncio
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from constants import *
from create_db import Base, User
import re


client = discord.Client()

engine = create_engine('sqlite:///invites.db')
Session = sessionmaker(bind=engine)
session = Session()

def get_role(invite):
    # TODO: Change roles with ids
    if invite == 0:
        return "404307411969507329", 1          # Soldier
    elif invite < 100:
        return "403985074464489492", 200        # Affiliate
    elif invite < 200:
        return "403985127337885696", 500        # Captain
    elif invite < 500:
        return "409749411971989504", 1000       # Lieutenant
    elif invite < 1000:
        return "403985161341108226", 1500       # Commander
    else:
        return "403985221164466177", 2000       # Supreme

async def get_invites():
    # TODO: Implement process invites logic
    await client.wait_until_ready()
    invite_endpoint = DISCORD_API_BASE_URL + '/guilds/%s/invites' % TEST_GUILD_ID
    user_endpoint = DISCORD_API_BASE_URL + '/guilds/%s/members' % TEST_GUILD_ID
    headers = {'Authorization': 'Bot ' + DISCORD_API_KEY}
    while not client.is_closed:
        r = requests.get(invite_endpoint, headers=headers)
        invites = json.loads(r.text)
        for invite in invites:
            if invite['channel']['name'] != 'welcome':
                continue
            user = session.query(User).filter_by(user_id=invite['inviter']['id']).first()
            if not user:
                user = User(user_id=invite['inviter']['id'], count=invite['uses'])
                session.add(user)
                session.commit()
            rank, next = get_role(invite['uses'])
            r = requests.get(user_endpoint + '/%s' % invite['inviter']['id'], headers=headers)
            api_user = json.loads(r.text)
            if "code" in api_user:
                continue
            elif "message" in api_user:
                if api_user["message"] == "You are being rate limited.":
                    await asyncio.sleep(api_user["retry_after"] / 1000)
                    r = requests.get(user_endpoint + '/%s' % invite['inviter']['id'], headers=headers)
                    api_user = json.loads(r.text)
            roles = api_user['roles']
            user.count = invite['uses']
            session.commit()
            if rank in roles:
                pass
            else:
                roles.append(rank)
                r = requests.patch(user_endpoint + '/%s' % invite['inviter']['id'], json={'roles': roles}, headers=headers)
        await asyncio.sleep(250)  # Check invites every 30 seconds



@client.event
async def on_member_remove(member):
    headers = {'Authorization': 'Bot ' + DISCORD_API_KEY}
    ban_endpoint = DISCORD_API_BASE_URL + "/guilds/%s/bans/%s" % (TEST_GUILD_ID, member.id)
    r = requests.put(ban_endpoint, json={"reason": "Spam control"}, headers=headers)



@client.event
async def on_message(message, *args, **kwargs):
    if message.content.startswith('!test'): 
        if "admin" in [role.name.lower() for role in message.author.roles]: # Only accept command for the selected role
            text = message.content.split(' ')[1:]
            text = ' '.join(text)
            await client.send_message(discord.Object(id='403985798896156672'), text) # Chairman
            await client.send_message(message.channel, text)
            await asyncio.sleep(1)
            await client.send_message(discord.Object(id='403985733158961172'), text) # Ambassador
            await asyncio.sleep(2)
            await client.send_message(discord.Object(id='403985667173908480'), text) # Senator
            await asyncio.sleep(2)
            await client.send_message(discord.Object(id='403985597397467138'), text) # Minister  						
            await asyncio.sleep(5)
            await client.send_message(discord.Object(id='403985509732319232'), text) # Conselor
            await asyncio.sleep(5)
            await client.send_message(discord.Object(id='403985444414554114'), text) # Affiliate
            await client.send_message(message.channel, "did it")
            return
    if message.channel.id == '409771333359108106':
        text = message.content.split()[1:]
        print(text)
        for i in text:
            reddit_link = re.search('...https://www.reddit.com/r/?|https://www.reddit.com/r/?', i)
            if reddit_link:
                reddit_link2 = ''.join(i)
        print(reddit_link2)
        if reddit_link2 is True:
            await client.send_message(message.channel, ":hand_splayed: {}\r\r{}\r\r:white_check_mark: GIVE SOME UPVOTES! :white_check_mark:".format(message.author.mention, reddit_link2))
            await client.delete_message(message)
        else:
            await client.delete_message(message)
            return
    elif message.content.startswith('!invite'):
        if message.channel.id == '407965998256488448':
            asker = message.author
            asker_id = message.author.id
            user = session.query(User).filter_by(user_id=asker_id).first()
            if not user:
                await client.send_message(message.channel, "Your invites are not created yet, try 5 minutes later")
                return
            rank, next = get_role(int(user.count))
            if rank == "404307411969507329":        # Soldier
                _rank, _next = "Affiliate", 1
            elif rank == "403985074464489492":      # Affiliate
                _rank, _next = "Captain", 100
            elif rank == "403985127337885696":      # Captain   
                _rank, _next = "Lieutenant", 200
            elif rank == "409749411971989504":      # Lieutenant        
                _rank, _next = "Commander", 500
            elif rank == "403985161341108226":      # Commander 
                _rank, _next = "Supreme", 1000
            elif rank == "403985221164466177":      # Supreme
                _rank, _next = "GOD", 0
            needed_invite = _next - user.count
            # await client.send_message(message.channel, "@{} \rYou currently have {} invites. \rYou need {} more invites to become {}".format(asker, user.count, needed_invite, _rank))
            embed = discord.Embed(title="{}'s Stats".format(asker), color=0xff0000)
            embed.add_field(name=":bell: Invite count", value=":arrow_right: {}".format(user.count), inline=False)
            embed.add_field(name=":bell: Required invites to be {}".format(_rank), value=":arrow_right: {}".format(needed_invite), inline=False)
            embed.set_thumbnail(url=asker.avatar_url)
            embed.set_footer(text="Invite Count will be updated every 5 mins")
            await client.send_message(message.channel, embed=embed)



@client.event
async def on_ready():
    best_coders = "01100101011011100110100101110011011011010110100101110010011010110110000101101110"


client.loop.create_task(get_invites())
client.run(DISCORD_API_KEY)
