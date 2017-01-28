# Embedbot 1.5.2 made by -Kiwi Catnip ♡#1540, @isy#0669 and @HYP3RD34TH#2104.
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
current_os = platform.system()
try:
    import cursor
except ImportError:
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        pip_os = "pip3"
    if current_os == "Windows":
        pip_os = "pip"
    print("Please run \"{} install Cursor\".".format(pip_os))
    sys.exit()
logged_in = False
try:
    passedargs = sys.argv[1]
except:
    passedargs = None

botversion = "1.5.2"


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


def clear_screen():
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        tmp = sp.call('clear', shell=True)
    if current_os == "Windows":
        tmp = sp.call('cls', shell=True)

if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
    tmp = sp.call('clear', shell=True)
    pip_os = "pip3"
if current_os == "Windows":
    tmp = sp.call('cls', shell=True)
    pip_os = "pip"


try:
    import clint
    from clint.textui import colored
    clintexists = True
except ImportError:
    clintexists = False
    pass

starttime = datetime.datetime.now()

try:
    assert sys.version_info >= (3, 5)
    from discord.ext import commands
    import discord
except ImportError:
    if clintexists:
        a = "install discord.py"
        print("Discord.py is not installed.")
        print("Please install it using {}.".format(colored.green('{} {}'.format(pip_os, a))))
        print("Also, you can install the dev versions from here:")
        print("https://github.com/Rapptz/discord.py")
    else:
        print("Discord.py is not installed.")
        print("Please install it using {} install discord.py.".format(pip_os))
        print("Also, you can install the dev versions from here:")
        print("https://github.com/Rapptz/discord.py")
    print("Note: If you get an error saying pip doesn't exist, try this:")
    print("\"Your python installation path\\Scripts\\pip.exe install discord.py\" (On Windows).")
    print("Also make sure you are running command prompt (or whatever you're using)\nas admin.")
    sys.exit()
except AssertionError:
    print("Embedbot needs Python 3.5 or superior.")
    sys.exit()
load = itertools.cycle(['.  ', '.. ', '...', '   '])
sys.stdout.write('Logging in to Discord')
cursor.hide()
def fuck():
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        for i in range(0, 4):
            sys.stdout.write(load.__next__())
            sys.stdout.flush()
            sys.stdout.write('\b\b\b')
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

try:
    with open(customconfig) as c:
        jsonhandler = json.load(c)
        token = jsonhandler['token']
        email = jsonhandler['email']
        password = jsonhandler['password']
        invoker = jsonhandler['invoker']
        textargs = jsonhandler['textargs']
        rminvokermsg = jsonhandler['autoremoveinvokermessage']
        advancedmode = jsonhandler['advancedmode']
        silent = jsonhandler['silentmode']
except:
    print("There was a problem with you config file. Make sure that everything is up to date.")

bot = commands.Bot(command_prefix=invoker, self_bot=True)
invite_url = "https://discord.gg/KFYAUyw"
# Bot Loading

@bot.event
async def on_ready():
    thread.do_run = False
    thread.join()
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        tmp = sp.call('clear', shell=True)
    if current_os == "Windows":
        tmp = sp.call('cls', shell=True)
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    login_time = datetime.datetime.now() - starttime
    login_time = login_time.seconds + login_time.microseconds/1E6
    print("-----------------------------------------------------------------")
    print("                 -Embedbot - Discord Selfbot-")
    print("   Made by -Kiwi Catnip \\u2661#1540, isy#0669 and HYP3RD34TH#2104.")
    print("-----------------------------------------------------------------")
    print("Login time         : {} milliseconds".format(login_time))
    print("Logged in as       : {} ({})".format(str(bot.user).encode("ascii", "backslashreplace").decode(), bot.user.id))
    print("Connected to       : {} servers and {} channels".format(servers, channels))
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("Python version     : {}.{}.{}".format(*os.sys.version_info[:3]))
    print("Discord.py version : {}".format(discord.__version__))
    print("Embedbot version   : {}".format(botversion))
    print("-----------------------------------------------------------------")
    c = "install clint"
    if silent == "True" or rminvokermsg == "True" or clintexists:
        if silent == "True" and rminvokermsg == "True":
            if clintexists:
                print(colored.yellow('Silentmode is not implemented yet.'))
                print(colored.yellow('Autoremove invoker message is not implemented yet.'))
            else:
                print('  Silentmode is not implemented yet.')
                print('  Autoremove invoker message is not implemented yet.')
                print('  Clint is not installed (use "{} {}" to install clint)'.format(pip_os, c))
        elif silent == "True" and rminvokermsg == "False":
            if clintexists:
                print(colored.yellow('Silentmode is not implemented yet.'))
            else:
                print('  Silentmode is not implemented yet.')
                print('  Clint is not installed (use "{} {}" to install clint)'.format(pip_os, c))
        elif silent == "False" and rminvokermsg == "True":
            if clintexists:
                print(colored.yellow('Autoremove invoker message is not fully implemented yet.'))
            else:
                print('  Autoremove invoker message is not fully implemented yet.')
                print('  Clint is not installed (use "{} {}" to install clint)'.format(pip_os, c))
        else:
            pass
        print("-----------------------------------------------------------------")
        print(colored.green('  If you get any errors, please join our support server with \n  the', bold=True),
              colored.blue('{}support'.format(invoker), bold=True),
              colored.green('command to complain about how we can\'t code.', bold=True))
    else:
        print('   If you get any errors, please join our support server with')
        print('   the "{}support" command to complain about how we can\'t code.'.format(invoker))
    print("-----------------------------------------------------------------")
    bot.remove_command("help")
    bot.remove_command("HelpFormatter")

@bot.event
async def on_message(message):
    if textargs == "True":
        if message.author == bot.user:
            messagereplace = message.content.replace("{hug}","\\\\(^.^\\\\)").replace("{shrug}","¯\\_(ツ)_/¯").replace("{lenny}","( ͡° ͜ʖ ͡°)").replace("{disapprove}","ಠ\_ಠ").replace("{tableflip}","(╯°□°）╯︵ ┻━┻").replace("{unflip}","┬─┬﻿ ノ( ゜-゜ノ)").replace("{unflip2}","​┬─┬ノ( º ⁓ ºノ)").replace("{unflip3}","┬─┬ノ( º _ ºノ)").replace("{cute}","(◕‿◕✿)").replace("{zwsp}","​").replace("{rtl}","\u202e") # This long ass line makes me want to kms ~ Hyp3r
            if not message.content == messagereplace:
                await bot.edit_message(message, messagereplace)
    await bot.process_commands(message)

@bot.command(pass_context=True)
async def cls(ctx):
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        tmp = sp.call('clear', shell=True)
        await bot.edit_message(ctx.message, "`Cleared console`")
    if current_os == "Windows":
        tmp = sp.call('cls' , shell=True)
        bot.edit_message(ctx.message, "`Cleared console.`")
    await asyncio.sleep(3)
    await bot.delete_message(ctx.message)

@bot.command(name="support", pass_context=True)
async def _join_support(ctx):
    edit = bot.edit_message
    try:
        await bot.accept_invite(invite_url)
        await edit(ctx.message, "`Joined support server. (Alexia's Hangout)`\n"
                                "`Check your server list.`")
        if rminvokermsg == "True":
            await asyncio.sleep(3)
            bot.delete_message(ctx.message)
        else:
            pass
    except discord.NotFound:
        await edit(ctx.message, "`The invite was invalid or expired.`\n"
                                "`Please go to our github page shown in the console.`")
        print("Github page: https://goo.gl/kXy1oM")
    except discord.HTTPException:
        await edit(ctx.message, "`[ERROR]: wasn't able to join the server.`\n"
                                "`Try again later.`")
    await asyncio.sleep(3)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def game(ctx, *, game=None):
    server = ctx.message.server
    current_status = server.me.status if server is not None else None
    if game:
        game = game.strip()
        await bot.change_presence(game=discord.Game(name=game), status=current_status)
        await bot.edit_message(ctx.message, 'Playing status changed to **{}**.'.format(game))
    else:
        await bot.change_presence(game=None, status=current_status)
        await bot.edit_message(ctx.message, "`Cleared playing status.`")
    await asyncio.sleep(3)
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def status(ctx, *, status=None):
    statuses = {
        "online"    : discord.Status.online,
        "idle"      : discord.Status.idle,
        "dnd"       : discord.Status.dnd,
        "invisible" : discord.Status.invisible,
        "offline"   : discord.Status.invisible
        }
    server = ctx.message.server
    current_game = server.me.game if server is not None else None
    if status is None:
        await bot.change_presence(status=discord.Status.online, game=current_game)
        await bot.edit_message(ctx.message, "`Status reset.`")

    else:
        status = statuses.get(status.lower(), None)
        await bot.change_presence(status=status, game=current_game)
        await bot.edit_message(ctx.message, "Status set to **{}**.".format(status))
    await asyncio.sleep(3)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def restart(ctx):
    await bot.edit_message(ctx.message, "`Restarting...`")
    print("Restarting...")
    await asyncio.sleep(2)
    bot.delete_message(ctx.message)
    if current_os == "Windows":
        if passedargs == None:
            os.system(__file__)
        else:
            os.system(__file__ + " " + passedargs)
    if current_os == "Linux":
        if passedargs == None:
            os.system('''sudo bash -c "python3 {}"'''.format(__file__))
        else:
            os.system('''sudo bash -c "python3 {} {}"'''.format(__file__, passedargs))
    if current_os == "Linux":
        if passedargs == None:
            os.system('''sudo bash "python3 {}"'''.format(__file__))
        else:
            os.system('''sudo bash "python3 {} {}"'''.format(__file__, passedargs))
    await bot.logout()

@bot.command(pass_context=True)
async def nick(ctx):
    try:
        cmdarg = ctx.message.content.split(" ", 1)[1]
        try:
            await bot.change_nickname(ctx.message.server.me, cmdarg)
            await asyncio.sleep(0.3)
            m = await bot.edit_message(ctx.message, "Your nickname on this server has been changed"
                                                    " to **{}**.".format(cmdarg))
            if rminvokermsg == "True":
                await asyncio.sleep(3)
                bot.delete_message(ctx.message)
            else:
                pass
        except:
            m = await bot.edit_message(ctx.message, "Your nickname could not be",
                                       " changed on this server.")
        await asyncio.sleep(3)
        await bot.delete_message(ctx.message)
    except IndexError:
        await bot.change_nickname(ctx.message.server.me, "")
        await asyncio.sleep(0.3)
        msg = await bot.edit_message(ctx.message, "Your nickname on this server has been reset.")
        await asyncio.sleep(3)
        await bot.delete_message(ctx.message)
	
@bot.command(pass_context=True, name="print")
async def _print(ctx, asdf):
    print(asdf.encode("ascii", "backslashreplace").decode())
    await bot.edit_message(ctx.message, "`Task Executed..`")
    await asyncio.sleep(3)
    await bot.delete_message(ctx.message)
	
@bot.command(pass_context=True)
async def test(ctx):
    await bot.edit_message(ctx.message, "`The selfbot is active.`")
    await asyncio.sleep(3)
    await bot.delete_message(ctx.message)

	
@bot.command(pass_context=True)
async def kill(ctx):
    await bot.edit_message(ctx.message, "`Killed.`")
    await asyncio.sleep(1)
    await bot.logout()

@bot.command(pass_context=True)
async def quote(ctx, m: discord.Member, *, asdf):
    if type(ctx.message.channel) == discord.PrivateChannel:
        em = discord.Embed(description=asdf, colour=0xFFFFFF)
        em.set_author(name=m.display_name, icon_url=m.avatar_url)
        await bot.edit_message(ctx.message, "​", embed=em)
    else:
        if ctx.message.server.me.permissions_in(ctx.message.channel).embed_links == True:
            if ctx.message.author.colour == "#000000":
                colour = "0xFFFFFF"
            else:
                colour = ctx.message.author.colour
            em = discord.Embed(description=asdf, colour=colour)
            em.set_author(name=m.display_name, icon_url=m.avatar_url)
            await bot.edit_message(ctx.message, "​", embed=em)
        else:
            await bot.edit_message(ctx.message,
                                   "I need the `embed links` permission to send an embed.")
            await asyncio.sleep(3)


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
            await bot.edit_message(ctx.message,
                                   "I need the `embed links` permission to send an embed.")



@bot.command(pass_context=True)
async def clean(ctx, number: int, match_pattern: str=None):
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
    await asyncio.sleep(3)
    await bot.delete_message(r)
    

# Added for extra future use
async def slow_deletion(messages):
    for message in messages:
        try:
            await bot.delete_message(message)
        except:
            pass

@bot.command(pass_context=True, name='eval')
async def _eval(ctx, *, code: str):
    """Evaluates code."""
    if advancedmode == "True":
        code = code.strip('` ')
        if code == "token":
            await bot.say("You probably don't want to show your token.",
                          " If you really do, please write {}eval str(token).".format(invoker))
        elif code == "email":
            await bot.say("You probably don't want to show your email.",
                          " If you really do, please write {}eval str(email).".format(invoker))
        elif code == "password":
            await bot.say("You probably don't want to show your password.",
                          " If you really do, please write {}eval str(password).".format(invoker))
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
        r = await bot.say("This command is an `advanced mode` command.")
        await asyncio.sleep(3)
        await bot.delete_message(r)

# ----- Non useful commands ----- #

@bot.command(pass_context=True)
async def f(ctx):
    await bot.edit_message(ctx.message, "`Respects have been paid.`")
    await bot.add_reaction(ctx.message, '\U0001f1eb')

try:
    if token == "None": # For People that use Email and Password.
                        # "None" because json doesn't have None.
    
        if "@" not in email or email == "None": # Checks email.
            thread.do_run = False
            thread.join()
            clear_screen()
            print("Invalid email or none provided.")
            print("Please check your credentials.")
        bot.run(email, password, bot=False)
    else:
        if len(token) < 50: # Checking Token's Length.
            thread.do_run = False
            thread.join()
            clear_screen()
            print("Token is to short.")
            print("Try using your email and password instead.\n")
            if "@" not in email: # Checks email.
                print("Invalid email or none provided.")
                print("Please check your credentials.")
                sys.exit()
            else:
                bot.run(email, password, bot=False)
        elif len(token) > 60: # Checking Token's Length.
            thread.do_run = False
            thread.join()
            clear_screen()
            print("Token is to long.")
            print("Try using your email and password instead.\n")
            if "@" not in email: # Checks email.
                print("Invalid email or none provided.")
                print("Please check your credentials.")
                sys.exit()
            else: # 
                bot.run(email, password, bot=False)
        elif password == "None": # Checks if there is a Password provided.
            thread.do_run = False
            thread.join()
            clear_screen()
            print("No password provided.")
            print("Please check your credentials.")
            sys.exit()
        else:
            bot.run(token, bot=False)
except:
    print("There was a problem logging in.")
    print("Check your internet connection.")
    print("If you haven't already, please add your credentials in config.json,")
    print("and make sure they're correct.")
    time.sleep(5)
    sys.exit()
