import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import chalk

client = discord.Client()
bot = commands.Bot(command_prefix='#')

# @client.event
# async def on_ready():
#     print('Logged in as')
#     print(client.user.name)
#     print(client.user.id)
#     print('------')

# @client.event
# async def on_message(message):
#     if message.content.startswith('!test'):
#         counter = 0
#         tmp = await client.send_message(message.channel, 'Calculating messages...')
#         async for log in client.logs_from(message.channel, limit=100):
#             if log.author == message.author:
#                 counter += 1
#         await client.edit_message(tmp, 'You have {} messages.'.format(counter))
#     elif message.content.startswith('!sa'):
#         await client.send_message(message.channel, 'as')
#     elif message.content.startswith('!sleep'):
#         await asyncio.sleep(5)
#         await client.send_message(message.channel, 'Done sleeping')
@bot.event
async def on_ready():
    print('I am running on ' + bot.user.name)
    print('My ID is: ' + bot.user.id)
    print('------')

# @bot.event
# async def on_message(message):
#     if message.content.startswith('!test'):
#         print(message.content)
#         await bot.send_message(message.channel, 'test 1 2 3')
#         print(message.channel)

@bot.command(pass_context=True)
@commands.has_role('admin2')
async def ping(ctx):
    await bot.say('ping, ping')

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say('The user name is: {}'.format(user.name))
    await bot.say('Highest role is {}'.format(user.top_role))               #Top Status
    await bot.say('User status is {}'.format(user.status))
    await bot.say('The user ID is: {}'.format(user.id))                     #ID
    await bot.say('The user joined at: {}'.format(user.joined_at))
    await bot.say(user.channel)
    # user.roles.append('<discord.role.Role object at 0x7f6445523408>')
    # print(role)
    # print(user.server)
    # print(user)
    # print(user.name)
    # print(user.top_role)
    # print(user.id) 
#admin2 = discord.Role(id=402192055767531530)

@bot.command(pass_context=True)
async def add_role(ctx, user: discord.Member, roles: discord.Role):
    await bot.add_roles(user, roles)
    print(bot.add_roles(user, roles))
    print('gave role to {}'.format(user))

@bot.command(pass_context=True)
async def delete(ctx, roles: discord.Role):
    await bot.delete_role(discord.Server(id=402192055767531530), roles)

@bot.command(pass_context=True)
async def remove(ctx, user: discord.Member, roles: discord.Role):
    await bot.remove_roles(user, roles)
    print('deleted role from {}'.format(user))

@bot.command(pass_context=True)
async def role(ctx, roles: discord.Role):
    # await bot.say(bot.add_roles(roles))
    await bot.say(roles.name)
    await bot.say(roles.id)
    await bot.say(roles.server)

@bot.command(pass_context=True)
async def ch(ctx, channel: discord.Channel):
    await bot.say(channel.name)
    await bot.say(channel.id)

@bot.command(pass_context=True)
async def invite(ctx):
    await bot.say(discord.Server(name='mirkan1', id=402192055767531530))
    await bot.say(bot.invites_from(discord.Server(name='mirkan1', id=402192055767531530)))
    print(bot.invites_from(discord.Server(name='mirkan1', id=402192055767531530)))
    print(discord.Server(name='mirkan1', id=402192055767531530))


# class discord.Invite():

# @bot.event
# async def on_message(message):
#     if message.content.startswith('#start'):
#         await bot.send_message(message.channel, 'Type #stop 4 times.')
#         for i in range(4):
#             msg = await bot.wait_for_message(author=message.author, content='!stop')
#             fmt = '{} left to go...'
#             await bot.send_message(message.channel, fmt.format(3 - i))

#         await bot.send_message(message.channel, 'Good job!')

bot.run('NDAxNzgxOTgyMjI2Mjg0NTY0.DTwv2g.Jmigf_3NHRQ5Ty--mM4ewJ4WbBo')

