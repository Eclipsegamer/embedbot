# Embedbot 1.2 made by -Kiwi Catnip ♡#1540 and @isy#0669.

import discord
from discord.ext import commands
import asyncio
import inspect
import os
import json
import time
try:
    import clint
    from clint.textui import colored
    clintexists = True
except ImportError:
    clintexists = False
    pass

# Config loading

with open('myconfig.json') as c:
    jsonhandler = json.load(c)
    email = jsonhandler['email']
    password = jsonhandler['password']
    invoker = jsonhandler['invoker']
    textargs = jsonhandler['textargs']
    advancedmode = jsonhandler['advancedmode']

bot = commands.Bot(command_prefix=invoker, self_bot=True)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name.encode("ascii","backslashreplace").decode())
    print(bot.user.id)
    print('------')
    if clintexists:
        print(colored.green('If you get any errors, please join https://discordapp.com/invite/KFYAUyw to complain about how I can\'t code.', bold=True))
    else:
        print('If you get any errors, please join https://discordapp.com/invite/KFYAUyw to complain about how I can\'t code.')
        print('You don\'t have clint installed. Please install it with "pip install clint".')
    print('')
    bot.remove_command("help")
    bot.remove_command("HelpFormatter")

@bot.event
async def on_message(message):
    if textargs == "True":
        if message.author == bot.user:	
            messagereplace = message.content.replace("{hug}","\\\\(^.^\\\\)").replace("{lenny}","( ͡° ͜ʖ ͡°)").replace("{disapprove}","ಠ\_ಠ").replace("{tableflip}","(╯°□°）╯︵ ┻━┻").replace("{unflip}","┬─┬﻿ ノ( ゜-゜ノ)").replace("{unflip2}","​┬─┬ノ( º ⁓ ºノ)").replace("{unflip3}","┬─┬ノ( º _ ºノ)").replace("{cute}","(◕‿◕✿)").replace("{zwsp}","​").replace("{rtl}","\u202e")
            if not message.content == messagereplace:
                await bot.edit_message(message, messagereplace)
    await bot.process_commands(message)
			
			
@bot.command(pass_context=True)
async def cls(ctx):
    import subprocess as sp
    tmp = sp.call('cls',shell=True)
@bot.command()
async def spinny():
	"""whee"""
	msg = await bot.say("`|`")
	await asyncio.sleep(0.5)
	await bot.edit_message(msg, '`/`')
	await asyncio.sleep(0.5)
	await bot.edit_message(msg, '`-`')
	await asyncio.sleep(0.5)
	await bot.edit_message(msg, '`\`')
	await asyncio.sleep(0.5)
	await bot.edit_message(msg, '`|`')
	await asyncio.sleep(0.5)
	await bot.edit_message(msg, '`/`')
	await asyncio.sleep(0.5)
	await bot.edit_message(msg, '`-`')
	await asyncio.sleep(0.5)
	await bot.edit_message(msg, '`\`')
	await asyncio.sleep(0.5)
	await bot.edit_message(msg, '`|`')
	await asyncio.sleep(1)
	await bot.edit_message(msg, 'how 2 aboose api')
	
@bot.command(pass_context=True)
async def restart(ctx):
    await bot.say("Restarting.")
    print("Restarting.")
    await asyncio.sleep(1)
    os.system(__file__)
    await bot.logout()
		
@bot.command(pass_context=True)
async def nick(ctx):
    try:
        cmdarg = ctx.message.content.split(" ",1)[1]
        try:
            await bot.change_nickname(ctx.message.server.me, cmdarg)
            msg = await bot.say("Your nickname on this server has been changed to **{}**.".format(cmdarg))
        except:
            msg = await bot.say("Your nickname could not be changed on this server.")
    except IndexError:
        await bot.change_nickname(ctx.message.server.me, "")
        msg = await bot.say("Your nickname on this server has been reset.")
    await asyncio.sleep(5)
    await bot.delete_message(ctx.message)
    await bot.delete_message(msg)
	
@bot.command(pass_context=True, name="print")
async def _print(ctx, asdf):
    print(asdf.encode("ascii","backslashreplace").decode())
	
@bot.command(pass_context=True)
async def test(ctx):
    await bot.say("The selfbot is active.")
	
@bot.command(pass_context=True)
async def kill(ctx):
    await bot.say("Killed.")
    await asyncio.sleep(1)
    await bot.logout()

@bot.command(pass_context=True)
async def embeds(ctx, *, asdf):
    if type(ctx.message.channel) == discord.PrivateChannel:
            em = discord.Embed(description=asdf, colour=0xFFFFFF)
            await bot.edit_message(ctx.message, "​", embed=em)
    else:
        if ctx.message.server.me.permissions_in(ctx.message.channel).embed_links == True:
            em = discord.Embed(description=asdf, colour=ctx.message.author.color)
            await bot.edit_message(ctx.message, "​", embed=em)
        else:
            await bot.say("I need the `embed links` permission to send an embed.")

@bot.command(pass_context=True, name='eval')
async def _eval(ctx, *, code : str):
    """Evaluates code."""
    if advancedmode == "True":
        code = code.strip('` ')
        python = '```py\n{}\n```'
        result = None

        env = {
            'ctx': ctx,
            'message': ctx.message,
            'server': ctx.message.server,
            'channel': ctx.message.channel,
            'author': ctx.message.author
        }

        env.update(globals())
 
        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            await bot.say(python.format(type(e).__name__ + ': ' + str(e)))
            return
        await bot.say(python.format(result))
    else:
        await bot.say("This command is an `advanced mode` command.")
		
		
		
# ----- Non useful commands ----- #

@bot.command(pass_context=True)
async def f(ctx):
    await bot.edit_message(ctx.message, "`Respects have been paid.`")
    await bot.add_reaction(ctx.message, '\U0001f1eb')
	
try:
    bot.run(email, password, bot=False)
except:
    print("Please add your credentials in config.json. If you already have,\nthey are incorrect.")
    time.sleep(5)
