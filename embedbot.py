# Embedbot 1.4 made by -Kiwi Catnip ♡#1540, @isy#0669 and @HYP3RD34TH#2104.
# Thanks to @Dav999#3322 for helping with the code a lot.
import subprocess as sp
import asyncio
import inspect
import os
import datetime
import platform
import sys
import traceback
import json
import time
import threading
import itertools
try:
    import cursor
except ImportError:
    print("Please run \"pip install Cursor\".")
    sys.exit()
logged_in = False
try:
    passedargs = sys.argv[1]
except:
    passedargs = None
	
botversion = "1.4"


def I(hello):
    why_are_you_here = "?"
    #I see no point.
"""If there's a bug, just report it."""
there = [
"is no reason you should be looking through the code.",
"It makes no sense."
]
do = "as you wish."
I("will be watching.")

current_os = platform.system()

def clear_screen():
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        tmp = sp.call('clear',shell=True)
    if current_os == "Windows":
        tmp = sp.call('cls' ,shell=True)

if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
    tmp = sp.call('clear',shell=True)
if current_os == "Windows":
    tmp = sp.call('cls' ,shell=True)

try:
    import clint
    from clint.textui import colored
    clintexists = True
except ImportError:
    clintexists = False
    pass
uptime = datetime.datetime.now()

try:
    assert sys.version_info >= (3, 5)
    from discord.ext import commands
    import discord
except ImportError:
    if clintexists:
        print("Discord.py is not installed.\nPlease install it using {}.\nAlso, you can install the dev versions from here:\nhttps://github.com/Rapptz/discord.py".format(colored.green('pip install discord.py')))
    else:
        print("Discord.py is not installed.\nPlease install it using pip install discord.py.\nAlso, you can install the dev versions from here:\nhttps://github.com/Rapptz/discord.py")
    print("Note: If you get an error saying pip doesn't exist, try this:\n\"Your python installation path\\Scripts\\pip.exe install discord.py\".\nAlso make sure you are running command prompt (or whatever you're using)\nas admin.")
    print("Another note: If the above doesn't work, try pip3 or pip3.5.")
    sys.exit()
except AssertionError:
    print("Embedbot needs Python 3.5 or superior.")
    sys.exit()
spinner = itertools.cycle(['-', '\\', '|', '/'])
sys.stdout.write('Logging in to Discord... ')
cursor.hide()
def fuck():
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        for i in range(0,4):
            sys.stdout.write(spinner.__next__())
            sys.stdout.flush()
            sys.stdout.write('\b') 
            time.sleep(0.5)
            if not getattr(t, "do_run", True):
                break
thread = threading.Thread(target=fuck)
thread.start()
# Config loading

try:
    customconfig = sys.argv[1]
except:
    customconfig = "config.json"

with open(customconfig) as c:
    jsonhandler = json.load(c)
    email = jsonhandler['email']
    password = jsonhandler['password']
    invoker = jsonhandler['invoker']
    textargs = jsonhandler['textargs']
    rminvokermsg = jsonhandler['autoremoveinvokermessage']
    advancedmode = jsonhandler['advancedmode']
    silent = jsonhandler['silentmode']
bot = commands.Bot(command_prefix=invoker, self_bot=True)

# Bot Loading

@bot.event
async def on_ready():
    thread.do_run = False
    thread.join()
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        tmp = sp.call('clear',shell=True)
    if current_os == "Windows":
        tmp = sp.call('cls' ,shell=True)
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    login_time = datetime.datetime.now() - uptime
    login_time = login_time.seconds + login_time.microseconds/1E6
    print("Login successful. ({}ms)".format(login_time))
    print("-----------------------------------")
    print("    Embedbot - Discord selfbot")
    print("-----------------------------------")
    print("Running as: " + str(bot.user).encode("ascii","backslashreplace").decode())
    print("Connected to:")
    print(" - {} servers".format(servers))
    print(" - {} channels".format(channels))
    print("-----------------------------------") 
    print("Embedbot version {}".format(botversion)) 
    if silent == "True" or rminvokermsg == "True":
        if silent == "True":
            if clintexists:
                print(colored.yellow('Silentmode is not implemented yet.'))
                return
            else:
                print('Silentmode is not implemented yet.')
                return
        if rminvokermsg == "True":
            if clintexists:
                print(colored.yellow('Autoremove invoker message is not implemented yet.'))
                return
            else:
                print('Autoremove invoker message is not implemented yet.')
                return
        print("-----------------------------------")
        return
    if clintexists:
        print(colored.green('If you get any errors, please join https://discordapp.com/invite/KFYAUyw\nto complain about how I can\'t code.'))
    else:
        print('If you get any errors, please join https://discordapp.com/invite/KFYAUyw\nto complain about how I can\'t code.')
        print('You don\'t have clint installed. Please install it with "pip install clint".')
    bot.remove_command("help")
    bot.remove_command("HelpFormatter")

@bot.event
async def on_message(message):
    if textargs == "True":
        if message.author == bot.user:	
            messagereplace = message.content.replace("{hug}","\\\\(^.^\\\\)").replace("{shrug}","¯\\_(ツ)_/¯").replace("{lenny}","( ͡° ͜ʖ ͡°)").replace("{disapprove}","ಠ\_ಠ").replace("{tableflip}","(╯°□°）╯︵ ┻━┻").replace("{unflip}","┬─┬﻿ ノ( ゜-゜ノ)").replace("{unflip2}","​┬─┬ノ( º ⁓ ºノ)").replace("{unflip3}","┬─┬ノ( º _ ºノ)").replace("{cute}","(◕‿◕✿)").replace("{zwsp}","​").replace("{rtl}","\u202e")
            if not message.content == messagereplace:
                await bot.edit_message(message, messagereplace)
    await bot.process_commands(message)
			
@bot.command(pass_context=True)
async def cls(ctx):
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        tmp = sp.call('clear',shell=True)
        await bot.edit_message(ctx.message, "`Cleared console`")
    if current_os == "Windows":
        tmp = sp.call('cls' ,shell=True)
        await bot.edit_message(ctx.message, "`Cleared console`")
    await asyncio.sleep(3)
    await bot.delete_message(ctx.message)	

@bot.command(pass_context=True)
async def restart(ctx):
    await bot.edit_message(ctx.message, "`Restarting..`")
    print("Restarting.")
    await asyncio.sleep(2)
    bot.delete_message(ctx.message)
    if passedargs == None:
        os.system(__file__)
    else:
        os.system(__file__ + " " + passedargs)
    await bot.logout()
		
@bot.command(pass_context=True)
async def nick(ctx):
    try:
        cmdarg = ctx.message.content.split(" ",1)[1]
        try:
            await bot.change_nickname(ctx.message.server.me, cmdarg)
            await asyncio.sleep(0.3)
            msg = await bot.edit_message(ctx.message, "Your nickname on this server has been changed to **{}**.".format(cmdarg))
        except:
            msg = await bot.edit_message(ctx.message, "Your nickname could not be changed on this server.")
    except IndexError:
        await bot.change_nickname(ctx.message.server.me, "")
        await asyncio.sleep(0.3)
        msg = await bot.edit_message(ctx.message, "Your nickname on this server has been reset.")
    await asyncio.sleep(5)
    await bot.delete_message(ctx.message)
	
@bot.command(pass_context=True, name="print")
async def _print(ctx, asdf):
    print(asdf.encode("ascii","backslashreplace").decode())
    ez = await bot.edit_message(ctx.message, "`Task Executed..`")
    await asyncio.sleep(3)
    await bot.delete_message(ez)
	
@bot.command(pass_context=True)
async def test(ctx):
    await bot.say("`The selfbot is active.`")
	
@bot.command(pass_context=True)
async def kill(ctx):
    await bot.say("`Killed.`")
    await asyncio.sleep(1)
    await bot.logout()

@bot.command(pass_context=True)
async def quote(ctx, m : discord.Member, *, asdf):
    if type(ctx.message.channel) == discord.PrivateChannel:
            em = discord.Embed(description=asdf, colour=0xFFFFFF)
            em.set_author(name=m.display_name, icon_url=m.avatar_url)
            await bot.edit_message(ctx.message, "​", embed=em)
    else:
        if ctx.message.server.me.permissions_in(ctx.message.channel).embed_links == True:
            em = discord.Embed(description=asdf, colour=ctx.message.author.color)
            em.set_author(name=m.display_name, icon_url=m.avatar_url)
            await bot.edit_message(ctx.message, "​", embed=em)
        else:
            await bot.say("I need the `embed links` permission to send an embed.")
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

@bot.command(pass_context=True)
async def clean(ctx, number: int, match_pattern: str = None):
    channel = ctx.message.channel
    author = ctx.message.author
    r = await bot.edit_message(ctx.message, "`Deleting messages...`")
    to_delete = []

    def content_match(_):
        return True

    def check(m):
        if m.author.id != bot.user.id:
            return False
        elif content_match(m.content):
            return True
        return False

    tries_left = 5
    tmp = ctx.message

    while tries_left and len(to_delete) < number:
        async for message in bot.logs_from(channel, limit=100, before=tmp):
            if len(to_delete) < number and check(message):
                to_delete.append(message)
            tmp = message
        tries_left -= 1
    to_delete.append(ctx.message)
    await slow_deletion(to_delete)
    r = await bot.say("`Task executed succesfully.`")
    await asyncio.sleep(5)
    await bot.delete_message(r)


# Added for extra future use
async def slow_deletion(messages):
    for message in messages:
        try:
            await bot.delete_message(message)
        except:
            pass

@bot.command(pass_context=True, name='eval')
async def _eval(ctx, *, code : str):
    """Evaluates code."""
    if advancedmode == "True":
        code = code.strip('` ')
        if code == "email":
            await bot.say("You probably don't want to show your email. If you really do, please write {}eval str(email).".format(invoker))
        else:
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
    print("Exiting.")
    cursor.show()
except:
    print("There was a problem logging in.\nCheck your internet connection.\nIf you haven't already, please add your credentials in config.json,\nand make sure they're correct.")
    time.sleep(5)
    sys.exit()