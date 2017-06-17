#! /usr/bin/python3.5
# Embedbot 2.0 made by -Kiwi Catnip ♡#1540, @isy#4506, @HYP3RD34TH#2104 @Nikitaw99#4332.
# Thanks to @Dav999#3322 for helping with the code a lot.
# Thanks to @Info Teddy#3737 for the help code that I stole from [\].
# Oops.
botversion = "2.0" # displayed in the info command
changes = "It now supports the d.py rewrite."

# argument parsing
import argparse
print("Imported argparse...")
parser = argparse.ArgumentParser(
    description='embedbot by -Kiwi Catnip ♡#1540, @isy#4506, @HYP3RD34TH#2104 @Nikitaw99#4332')
parser.add_argument("config", type=str, help="config file.", nargs="?", default="config.json")
parser.add_argument("-l", "--loadmode", type=int,
                    help="loadmode. 0 is dotdotdot, 1 is spinny line")
parser.add_argument("-d", "--debug", type=str,
                    help="logging level. defaults to WARNING", choices=["DEBUG", "INFO", "WARNING",
                                                                        "ERROR", "CRITICAL"])
print("Parsing arguments...")
global passedargs
passedargs = parser.parse_args()
print("Arguments parsed.")

# logging set up
import logging
loglevel = None
if passedargs.debug:
    if passedargs.debug == "DEBUG":
        loglevel = logging.DEBUG
    elif passedargs.debug == "INFO":
        loglevel = logging.INFO
    elif passedargs.debug == "WARNING":
        loglevel = logging.WARNING
    elif passedargs.debug == "ERROR":
        loglevel = logging.ERROR
    elif passedargs.debug == "CRITICAL":
        loglevel = logging.CRITICAL
else:
    loglevel = logging.WARNING
logging.basicConfig(filename='embedbot.log', level=loglevel)
print("Imported logging...")
print("Log started! Log will be saved into embedbot.log")

# tons of imports
import codecs
logging.info("Imported codecs...")
import subprocess as sp
logging.info("Imported subprocess...")
import asyncio # you need this for discord.py
logging.info("Imported asyncio...")
import inspect
logging.info("Imported inspect...")
import io
logging.info("Imported io...")
from contextlib import redirect_stdout
logging.info("Imported redirect_stdout from contextlib...")
import os # essential here for interacting with the OS
logging.info("Imported os...")
import datetime # used for telling the time and date, i guess
logging.info("Imported datetime...")
import platform # used for telling what OS you are using (i guess)
logging.info("Imported platform...")
import sys # again, essential python stuff for OS and internal python stuff
logging.info("Imported sys...")
import traceback
logging.info("Imported traceback...")
import json # for teh config
logging.info("Imported json...")
import time # like datetime, for telling time
logging.info("Imported time...")
import requests # CATS
logging.info("Imported requests...")
try:
    import threading
    logging.info("Imported threading...")
except ImportError:
    import dummy_threading as threading
    logging.warning("Threading not installed! Using dummy_threading...")
import itertools # probably iterator stuff? was used in loading screen (spinny line/dot dot dot)
logging.info("Imported itertools...")
import urllib.request # internet download stuff
logging.info("Imported urllib.request...")
import textwrap # for wrapping the bee movie script
logging.info("Imported textwrap...")
import random # mostly for *shuffle, which doesnt work anyways
logging.info("Imported random...")
import pip # for installing packages
logging.info("Imported pip...")
import aiohttp
logging.info("Import aiohttp...")
def install(package):
    """Install a package using pip"""
    pip.main(['install', package])
current_os = platform.system()
installlist = [] # list of things to install (i guess)
needinstall = False
try:
    import psutil
    logging.info("Imported psutil...")
except ImportError:
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        pip_os = "pip3"
    if current_os == "Windows":
        pip_os = "pip"
    installlist.append("psutil")
    logging.warning("Please run \"{} install psutil\".".format(pip_os))
    needinstall = True
# Colorama
# guessing from the name, it's used for coloring terminal text
try:
    from colorama import Fore, Back, Style
    import colorama
    colorama.init(autoreset=True)
    logging.info("Imported colorama...")
except ImportError:
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        pip_os = "pip3"
    if current_os == "Windows":
        pip_os = "pip"
    installlist.append("colorama")
    logging.warning("Please run \"{} install colorama\".".format(pip_os))
    needinstall = True
# PIL
# image manipulation
try:
    from PIL import Image
    import PIL.ImageOps
    from PIL import ImageFilter
    from PIL import ImageFont
    from PIL import ImageDraw
    logging.info("Imported pillow...")
except ImportError:
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        pip_os = "pip3"
    if current_os == "Windows":
        pip_os = "pip"
    installlist.append("pillow")
    logging.warning("Please run \"{} install pillow\".".format(pip_os))
    needinstall = True
# cursor
# ...i dont even know
try:
    import cursor
    logging.info("Imported cursor...")
except ImportError:
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        pip_os = "pip3"
    if current_os == "Windows":
        pip_os = "pip"
    installlist.append("Cursor")
    logging.warning("Please run \"{} install Cursor\".".format(pip_os))
    needinstall = True
# And here's where the installing begins.
instimporterror = False
if needinstall:
    logging.warning("Attempting to install the missing modules.")
    for module in installlist:
        install(module)
    x = "If there were any errors, please run embedbot with admininstrator privileges"
    y = ", or please use pip to install them."
    z = "\nIf there was no errors, you can now run embedbot normally."
    logging.warning(x + y + z)
    del x, y, z
    time.sleep(3)
    sys.exit()
print("Done.")
time.sleep(1)
logged_in = False

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

# ===== more bad code starts here =====
sessions = set()

del I, there, do

async def say(messageobject, message=None, emb=None): #copy pasted from nekobot
    try:
        if emb != None:
            object = await messageobject.channel.send(
                message,
                embed=emb,
            )
            if message == None:
                messagea = emb.description
            else:
                messagea = message
            #print("NekoBotBeta: {}".format(str(messagea).encode("ascii","backslashreplace").decode()))
            return object
        else:
            object = await messageobject.channel.send(message)
            if message == None:
                messagea = emb.description
            else:
                messagea = message
            #print("NekoBotBeta: {}".format(str(messagea).encode("ascii","backslashreplace").decode()))
            return object
    except(discord.errors.HTTPException, discord.errors.Forbidden) as e:
        raise

def clear_screen():
    """Clear stdout."""
    sys.stdout.write("\033[2J")
    sys.stdout.flush()

def color(color):
    if colorterm == "True":
        return eval("Fore.{}".format(color))
    else:
        return ""
# some important stuff so that pip works
if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
    pip_os = "pip3"
if current_os == "Windows":
    pip_os = "pip"
clear_screen()

starttime = datetime.datetime.now() # the current date + time

response = urllib.request.urlopen("https://raw.githubusercontent.com/Luigimaster1/embedbot/master/botinfo.json")
data = response.read().decode("utf-8")

if json.loads(data)["version"] > botversion:
    if json.loads(data)["forceupdate"] == "true":
        print("Updating...")
        import platform
        try:
            from git import Repo
        except ImportError:
            print("Please install the module gitpython.".format(pip_os))
            sys.exit()
        import shutil
        from distutils.dir_util import copy_tree
        import stat
        try:
            os.remove("oldconfig.json")
        except OSError:
            pass
        try:
            os.rename("config.json", "oldconfig.json")
        except FileNotFoundError:
            pass
        os.remove("embedbot.py") #lol r i p embedbot if this doesn't work r i p my work
        try:
            os.remove("README.md")
        except FileNotFoundError:
            pass
        try:
            os.remove("requirements.txt")
        except FileNotFoundError:
            pass
        repo_url = "https://www.github.com/Luigimaster1/embedbot.git"
        local_dir = "./tempupdate/"
        Repo.clone_from(repo_url, local_dir)
        def del_rw(action, name, exc):
            os.chmod(name, stat.S_IWRITE)
            os.remove(name)
        shutil.rmtree("./tempupdate/.git/", onerror=del_rw)
        copy_tree(local_dir, ".")
        shutil.rmtree("./tempupdate/", onerror=del_rw)
        os.remove("botinfo.json")
        passedargsa = str(passedargs.config)
        print("Restarting...")
        time.sleep(1)
        if current_os == "Windows":
            if passedargsa == None:
                os.system('"' + __file__ + '"')
            else:
                os.system('"' + __file__ + '" ' + passedargsa)
        if current_os == "Linux":
            if passedargsa == None:
                os.system('''sudo bash -c "python3 {}"'''.format('"' + __file__ + '"'))
            else:
                os.system('''sudo bash -c "python3 {} {}"'''.format('"' + __file__ + '" ' + passedargsa))
        sys.exit()

# Config loading
try:
    customconfig = passedargs.config
except OSError:
    try:
        # config doesnt exist? then the bot will use default one.
        customconfig = "config.json"
    except OSError:
        # but if it doesnt exist...
        print("Uh oh. The default config seems to be missing.")
        print("Attempting to fetch config from github...")
        # ...we will download the one from hte github
        url = "https://github.com/Luigimaster1/embedbot/blob/master/config.json"
        filename = "config.json"
        urllib.request.urlretrieve(url, filename)
        print("Config file fetched! Please fill up the config file properly.")
        customconfig = filename
        del url, filename
        sys.exit()

try:
    with open(customconfig) as c:
        jsonhandler = json.load(c)
        token = jsonhandler['token'] # user token (CTRL+SHIFT+I > Applications > LocalStorage)
        invoker = jsonhandler['invoker'] # command prefix, * by default
        textargs = jsonhandler['textargs']
        rminvokermsg = jsonhandler['autoremoveinvokermessage']
        advancedmode = jsonhandler['advancedmode'] # enables eval and repl
        silent = jsonhandler['silentmode']
        colorterm = jsonhandler['color'] # if you want colored messages or not
except json.JSONDecodeError:
    print("There was a problem with your config file. Make sure that everything is up to date.\n"
          "If it still doesn't work, try deleting the config file and creating it again.\n"
          "Don't use notepad for editing, use notepad++!")
    sys.exit()

try:
    assert sys.version_info >= (3, 5) # bot incompatible with 3.4 and below
    from discord.ext import commands # nice, discord ext ~Nikitaw99
    import discord # guess what this is for
except ImportError: # if discord.py aint installed
    a = "install discord.py"
    print("Discord.py is not installed.")
    print("Please install it using {}{} {}.".format(color("GREEN"), pip_os, a))
    print("Also, you can install the dev versions from here:")
    print("https://github.com/Rapptz/discord.py")
    print("Note: If you get an error saying pip doesn't exist, try this:")
    print("\"Your python installation path\\Scripts\\pip.exe install discord.py\" (On Windows).")
    print("Also make sure you are running command prompt (or whatever you're using)\nas admin.")
    sys.exit()
except AssertionError: # bot incompatible with 3.4 and below
    print("Embedbot needs Python 3.5 or superior.")
    sys.exit()
# all the loading messages
starttext = [
    "According to all known laws of aviation...",
    "IT'S THE",
    "Uh oh!",
    "Now look at this net",
    "Deleting {} drive...".format(psutil.disk_partitions()[0][0]),
    "Installing Bonzi Buddy...",
    "Welcome back!",
    "Readying the felines...",
    "\"What are you saying you don't know how to code?\"",
    "Bad code awaits you.",
    "You ready for this?",
    "*Crunch* NO DON'T TOUCH THAT!",
    "BetterDiscord more like sweaterdiscord because nobody wants it",
    "import antigravity",
    "from __future__ import braces",
    "import this",
    "import that",
    "Please wait, would you prefer chicken, steak, or tofu?",
    "Please wait, pay no attention to the man behind the curtain",
    "Please wait, and enjoy the elevator music",
    "Please wait, and dream of faster computers",
    "Please wait, would you like fries with that?",
    "Please wait, go ahead -- hold your breath",
    "Please wait, at least you're not on hold",
    "Please wait, you're not in Kansas any more",
    "Please wait, the guild is powered by a lemon and two electrodes",
    "Please wait, we love you just the way you are",
    "Please wait, we're testing your patience",
    "Please wait, as if you had any other choice",
    "Please wait, take a moment to sign up for our lovely prizes",
    "Please wait, don't think of purple hippos",
    "Please wait, follow the white rabbit",
    "Please wait, why don't you order a sandwich?",
    "Please wait, while the satellite moves into position",
    "Please wait, the bits are flowing slowly today",
    "Counting backwards from infinity...",
    "Commencing infinite loop (this may take some time)",
    "Go get a coffee or something. This is going to take a while.",
    "Very funny Scotty. Now beam down my clothes.",
    "Measuring the cable length to fetch your data...",
    "Loading completed, press F13 to continue.",
    "Keyboard not found, press Y to continue..."
]
# Strings loading
def loadstrings():
    # Totally not copied from [\]
    # sorry info
    stringsf = open(r".\Resources\strings.json", 'r')
    stringsfr = stringsf.read()
    strings = json.loads(stringsfr)
    global cmds
    cmds = strings['cmds']

loadstrings()

print(random.choice(starttext))
if passedargs.loadmode:
    if loadmode == 0:
        load = itertools.cycle(['.  ', '.. ', '...', '   '])
    elif loadmode == 1:
        load = itertools.cycle([' |', ' /', ' -', ' \\'])
    else:
        logging.warning("Invalid loadmode argument. Using default...")
        load = itertools.cycle(['.  ', '.. ', '...', '   '])
else:
    load = itertools.cycle(['.  ', '.. ', '...', '   '])

# if passedargs.loadmode:
#     if passedargs.loadmode == 0:
#         load = itertools.cycle(['.  ', '.. ', '...', '   '])
#     else:
#         load = itertools.cycle(['|', '/', '-', '\\'])
# else:
#     load = itertools.cycle(['.  ', '.. ', '...', '   '])

sys.stdout.write('Logging in to Discord')
cursor.hide()
def loggingin():
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        for i in range(0, 4):
            sys.stdout.write(load.__next__())
            sys.stdout.flush()
            if passedargs.loadmode:
                if passedargs.loadmode == 0:
                    sys.stdout.write('\b\b\b')
                else:
                    sys.stdout.write('\b\b')
            else:
                sys.stdout.write('\b\b\b')
            time.sleep(0.5)
            if not getattr(t, "do_run", True):
                break
thread = threading.Thread(target=loggingin) # tbh i like multiprocessing more than threading
thread.start()

bot = commands.Bot(command_prefix=invoker, self_bot=True)
invite_url = "https://discord.gg/KFYAUyw"
# Bot Loading


def helplist(cats, onlycat=None):
    returnage = ''
    for cat in cats:
        if (onlycat == None and cat['cat_shown']) or onlycat == cat['cat_slug']:
            if onlycat == None:
                x = '\n\n__`{}:`__ - For command descriptions: **`\\help {}`**'
                y = x.format(cat['cat_name'], cat['cat_slug'])
                returnage += y
                del x, y
            else:
                if cat['cat_desc'] != '':
                    returnage += cat['cat_desc']
                returnage += '\n__`{}:`__'.format(cat['cat_name'])

            first = True
            for cmd in cat['commands']:
                if onlycat == None:
                    if first:
                        returnage += '\n`\\{}`'.format(cmd['name'])
                        first = False
                    else:
                        returnage += '   `\\{}`'.format(cmd['name'])
                else:
                    returnage += '\n`\\{}` - {}'.format(cmd['name'], cmd['short'])
    return returnage

@bot.event
async def on_ready():
    thread.do_run = False
    thread.join()
    clear_screen()
    guilds = len(bot.guilds)
    channels = len([c for c in bot.get_all_channels()])
    login_time = datetime.datetime.now() - starttime
    login_time = login_time.seconds + login_time.microseconds/1E6
    print("=================================================================")
    print("                 -Embedbot - Discord Selfbot-")
    print("   By -Kiwi Catnip \\u2661#1540, isy#4506, HYP3RD34TH#2104.")
    print("                      and Nikitaw99#4332")
    print("=================================================================")
    print("Login time         : {} milliseconds".format(login_time))
    x = "Logged in as       : {} ({})"
    y = x.format(str(bot.user).encode("ascii", "backslashreplace").decode(), bot.user.id)
    print(y)
    del x, y
    print("Connected to       : {} guilds and {} channels".format(guilds, channels))
    print("-----------------------------------------------------------------")
    print("Python version     : {}.{}.{}".format(*os.sys.version_info[:3]))
    print("Discord.py version : {}".format(discord.__version__))
    print("Embedbot version   : {}".format(botversion))
    print("-----------------------------------------------------------------")
    c = "install clint"
    if silent == "True" or rminvokermsg == "True":
        if silent == "True" and rminvokermsg == "True":
            print(color("YELLOW") + 'Silentmode is not implemented yet.')
            print(color("YELLOW") + 'Autoremove invoker message is not implemented yet.')
            print("-----------------------------------------------------------------")
        elif silent == "True" and rminvokermsg == "False":
            print(color("YELLOW") + 'Silentmode is not implemented yet.')
            print("-----------------------------------------------------------------")
        elif silent == "False" and rminvokermsg == "True":
            print(color("YELLOW") + 'Autoremove invoker message is not fully implemented yet.')
            print("-----------------------------------------------------------------")
        else:
            pass
    x = color("LIGHTGREEN_EX") + '  If you get any errors, please join our support guild with \n  the '
    y = color("LIGHTCYAN_EX") + '{}support '.format(invoker) + color("LIGHTGREEN_EX")
    z = 'command to complain about how we can\'t code.'
    print(x+y+z)
    del x, y, z
    print("=================================================================")
    response = urllib.request.urlopen("https://raw.githubusercontent.com/Luigimaster1/embedbot/master/botinfo.json")
    data = response.read().decode("utf-8")
    if json.loads(data)["version"] > botversion:
        print(color("LIGHTYELLOW_EX") + "Update available! Latest version: {}".format(json.loads(data)["version"]))
    bot.remove_command("help")
    bot.remove_command("HelpFormatter")
    @bot.group(pass_context=True)
    async def help(ctx):
        # Also copied from [\]
        # sorry info
        try:
            cmdarg = ctx.message.content.split(" ", 1)[1]
            helpf = True
        except IndexError:
            helpf = False
            if ctx.message.guild == None:
                embedsendable = True
                em = discord.Embed(description="Help", colour=0xFFFFFF)
            elif ctx.message.guild.me.permissions_in(ctx.message.channel).embed_links == True:
                em = discord.Embed(description="Help", colour=ctx.message.author.color)
                embedsendable = True
            else:
                embedsendable = False
            if embedsendable:
                em.add_field(name="Normal commands:", value="embeds, quote, clean", inline=True)
                x = "info, update, cls, support, kill, restart, print, test, brainfuck"
                em.add_field(name="Helpful/technical commands:", value=x, inline=True)
                em.add_field(name="Profile commands:", value="game, nick, status", inline=True)
                x = "blur, undertext, invert, f, memberundertale, cat"
                em.add_field(name="Useless commands:", value=x, inline=True)
                em.add_field(name="Advanced mode commands:", value="eval, repl", inline=True)
                x = "You can use {}help (command) to get the information of that command."
                em.set_footer(text=x.format(invoker))
                del x
                await say(ctx.message, emb=em)
        if helpf == True:
            content = (helplist(cmds))

            # General
            if cmdarg == None:
                pass
            else:
                matched = False
                for cat in cmds:
                    # Maybe have a nested try-except KeyError
                    # instead of looping through every command
                    for cmd in cat['commands']:
                        if cmdarg == cmd['name']:
                            try:
                                x = '`{}{}` - {}'
                                y = x.format(invoker, cmd['name'], cmd['extrafull'])
                                content = y
                                del x, y
                            except KeyError:
                                x = '`{}{}` - {}\n{}'
                                y = x.format(invoker, cmd['name'], cmd['short'], cmd['extra'])
                                content = y
                                del x, y
                            matched = True
                            break
                    if matched:
                        break

                if not matched:
                    content = 'Invalid arguments passed, or the command is not in the help list.'
            if ctx.message.guild == None:
                embed = discord.Embed(description=content.format(invoker), colour=0xFFFFFF)
            elif ctx.message.guild.me.permissions_in(ctx.message.channel).embed_links == True:
                x = ctx.message.author.color
                embed = discord.Embed(description=content.format(invoker), colour=x)
                del x
            await say(ctx.message, emb=embed)

@bot.event
async def on_message(message):
    if textargs == "True":
        if message.author == bot.user:
            x = message.content.replace("{hug}","\\\\(^.^\\\\)").replace("{shrug}","¯\\_(ツ)_/¯")
            y = x.replace("{lenny}","( ͡° ͜ʖ ͡°)").replace("{disapprove}","ಠ\\_ಠ")
            z = y.replace("{tableflip}","(╯°□°）╯︵ ┻━┻").replace("{unflip}","┬─┬﻿ ノ( ゜-゜ノ)")
            x = z.replace("{unflip2}","​┬─┬ノ( º ⁓ ºノ)").replace("{unflip3}","┬─┬ノ( º _ ºノ)")
            y = x.replace("{cute}","(◕‿◕✿)").replace("{zwsp}","​").replace("{rtl}","\u202e")
            z = y.replace("{shurg}","¯\\\_( )ツ\_/¯").replace("{lenmon}","[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]​").replace("{pika}","ϞϞ(๑⚈ ․̫ ⚈๑)∩")
            messagereplace = z
            del x, y, z
            if not message.content == messagereplace:
                await message.edit(content=messagereplace)
    await bot.process_commands(message)

@bot.command(pass_context=True)
async def info(ctx):
    if ctx.message.guild == None:
        embedsendable = True
        em = discord.Embed(description="Embedbot information", colour=0xFFFFFF)
    elif ctx.message.guild.me.permissions_in(ctx.message.channel).embed_links == True:
        em = discord.Embed(description="Embedbot information", colour=ctx.message.author.color)
        embedsendable = True
    else:
        embedsendable = False
    if embedsendable:
        em.add_field(name="Discord.py version:", value="{}.{}.{} {}".format(discord.version_info[0], discord.version_info[1], discord.version_info[2], discord.version_info[3]), inline=True)
        em.add_field(name="Embedbot version:", value=botversion, inline=True)
        em.add_field(name="Made by:", value="-Kiwi Catnip ♡#1540, isy#4506, HYP3RD34TH#2104 and @Nikitaw99#4332.", inline=True)
        em.add_field(name="According to all known laws of aviation,", value="a bee should not be able to fly.", inline=True)
        em.add_field(name="Github project:", value="https://www.github.com/Luigimaster1/embedbot", inline=True)
    try:
        await ctx.message.edit(content="​", embed=em)
    except:
        await say(ctx.message, "Discord.py version: {}.{}.{} {}\n",
        "Embedbot version: {}\n",
        "Made by: -Kiwi Catnip ♡#1540, isy#4506 and HYP3RD34TH#2104.\n",
        "According to all known laws of aviation, a bee should not be able to fly.\n",
        "Github project: https://www.github.com/Luigimaster1/embedbot"
        .format(discord.version_info[0], discord.version_info[1], discord.version_info[2], discord.version_info[3], botversion))

@bot.command(pass_context=True)
async def update(ctx):
    await say(ctx.message, "Updating...")
    import platform
    try:
        from git import Repo
    except ImportError:
        await say(ctx.message, "Please install the module gitpython.".format(pip_os))
        return
    import shutil
    from distutils.dir_util import copy_tree
    import stat
    try:
        os.remove("oldconfig.json")
    except OSError:
        pass
    os.rename("config.json", "oldconfig.json")
    os.remove("embedbot.py") #lol r i p embedbot if this doesn't work r i p my work
    os.remove("README.md")
    os.remove("requirements.txt")
    repo_url = "https://www.github.com/Luigimaster1/embedbot.git"
    local_dir = "./tempupdate/"
    Repo.clone_from(repo_url, local_dir)
    def del_rw(action, name, exc):
        os.chmod(name, stat.S_IWRITE)
        os.remove(name)
    shutil.rmtree("./tempupdate/.git/", onerror=del_rw)
    copy_tree(local_dir, ".")
    shutil.rmtree("./tempupdate/", onerror=del_rw)
    os.remove("botinfo.json")
    await say(ctx.message, "The bot has been updated. Please restart the bot.")
@bot.command(pass_context=True)
async def cls(ctx):
    clear_screen()
    ctx.message.edit(content="`Cleared console.`")
    await asyncio.sleep(3)
    await ctx.message.delete()

@bot.command(name="support", pass_context=True)
async def _join_support(ctx):
    await ctx.message.edit(content=invite_url)

@bot.command(pass_context=True)
async def game(ctx, *, game=None):
    guild = ctx.message.guild
    current_status = guild.me.status if guild is not None else None
    if game:
        game = game.strip()
        await bot.change_presence(game=discord.Game(name=game), status=current_status)
        await ctx.message.edit(content='Playing status changed to **{}**.'.format(game))
    else:
        await bot.change_presence(game=None, status=current_status)
        await ctx.message.edit(content="`Cleared playing status.`")
    await asyncio.sleep(3)
    await ctx.message.delete()


@bot.command(pass_context=True)
async def status(ctx, *, status=None):
    statuses = {
        "online"    : discord.Status.online,
        "idle"      : discord.Status.idle,
        "dnd"       : discord.Status.dnd,
        "invisible" : discord.Status.invisible,
        "offline"   : discord.Status.invisible
        }
    guild = ctx.message.guild
    current_game = guild.me.game if guild is not None else None
    if status is None:
        await bot.change_presence(status=discord.Status.online, game=current_game)
        await ctx.message.edit(content="`Status reset.`")

    else:
        status = statuses.get(status.lower(), None)
        await bot.change_presence(status=status, game=current_game)
        await ctx.message.edit(content="Status set to **{}**.".format(status))
    await asyncio.sleep(3)
    await ctx.message.delete()

@bot.command(pass_context=True)
async def restart(ctx):
    #passedargsa = ""
    #for i in vars(passedargs):
    #    passedargsa = passedargsa + i + " "
    passedargsa = str(passedargs.config)
    await ctx.message.edit(content="`Restarting...`")
    print("Restarting...")
    await asyncio.sleep(2)
    ctx.message.delete()
    if current_os == "Windows":
        if passedargsa == None:
            os.system('"' + __file__ + '"')
        else:
            os.system('"' + __file__ + '" ' + passedargsa)
    if current_os == "Linux":
        if passedargsa == None:
            os.system('''sudo bash -c "python3 {}"'''.format('"' + __file__ + '"'))
        else:
            os.system('''sudo bash -c "python3 {} {}"'''.format('"' + __file__ + '" ' + passedargsa))
    await bot.logout()
    sys.exit()

@bot.command(pass_context=True)
async def nick(ctx):
    try:
        cmdarg = ctx.message.content.split(" ", 1)[1]
        try:
            await bot.change_nickname(ctx.message.guild.me, cmdarg)
            await asyncio.sleep(0.3)
            await ctx.message.edit(content="Your nickname on this guild has been changed to **{}**.".format(cmdarg))
            await asyncio.sleep(3)
            await ctx.message.delete()
        except:
            await ctx.message.edit(content="Your nickname could not be changed on this guild.")
        await asyncio.sleep(3)
        await ctx.message.delete()
    except IndexError:
        await bot.change_nickname(ctx.message.guild.me, "")
        await asyncio.sleep(0.3)
        await ctx.message.edit(content="Your nickname on this guild has been reset.")
        await asyncio.sleep(3)
        await ctx.message.delete()

@bot.command(pass_context=True, name="print")
async def _print(ctx, asdf):
    print(asdf.encode("ascii", "backslashreplace").decode())
    await ctx.message.edit(content="`Task Executed..`")
    await asyncio.sleep(3)
    await ctx.message.delete()

@bot.command(pass_context=True)
async def test(ctx):
    await ctx.message.edit(content="`The selfbot is active.`")
    await asyncio.sleep(3)
    await ctx.message.delete()


@bot.command(pass_context=True)
async def kill(ctx):
    await ctx.message.edit(content="`Killed.`")
    await asyncio.sleep(1)
    await bot.logout()

@bot.command(pass_context=True)
async def quote(ctx, *, asdf):
    asdf = discord.utils.get(bot.messages, id=asdf)
    if asdf.content is not None:
        if ctx.message.guild == None:
            em = discord.Embed(description=asdf.content, timestamp=asdf.timestamp, colour=0xFFFFFF)
            em.set_author(name=asdf.author.display_name, icon_url=asdf.author.avatar_url)
            await ctx.message.edit(content="​", embed=em)
        else:
            if ctx.message.guild.me.permissions_in(ctx.message.channel).embed_links == True:
                if asdf.author.colour == "#000000":
                    colour = "0xFFFFFF"
                else:
                    colour = asdf.author.colour
                em = discord.Embed(description=asdf.content, timestamp=asdf.timestamp, colour=colour)
                em.set_author(name=asdf.author.display_name, icon_url=asdf.author.avatar_url)
                await ctx.message.edit(content="​", embed=em)
            else:
                await ctx.message.edit(
                                       "I need the `embed links` permission to send an embed.")
    else:
        await ctx.message.edit(content="`Could not find the message specified.`")


@bot.command(pass_context=True)
async def embeds(ctx, *, asdf):
    if ctx.message.guild == None:
        if asdf.split(" ")[0].startswith("--image=") == True:
            em = discord.Embed(description=asdf.split("--image=" + asdf.split(" ")[0].split("--image=")[1] + " ", 1)[1], colour=0xFFFFFF)
            em.set_image(url=asdf.split(" ")[0].split("--image=")[1])
        else:
            em = discord.Embed(description=asdf, colour=0xFFFFFF)
        await ctx.message.edit(content="​", embed=em)
    elif ctx.message.guild.me.permissions_in(ctx.message.channel).embed_links == True:
        if asdf.split(" ")[0].startswith("--image=") == True:
            em = discord.Embed(description=asdf.split("--image=" + asdf.split(" ")[0].split("--image=")[1] + " ", 1)[1], colour=ctx.message.author.color)
            em.set_image(url=asdf.split(" ")[0].split("--image=")[1])
        else:
            em = discord.Embed(description=asdf, colour=ctx.message.author.color)
        await ctx.message.edit(content="​", embed=em)
    else:
        await ctx.message.edit(
                               "I need the `embed links` permission to send an embed.")



@bot.command(pass_context=True)
async def clean(ctx, number: int, match_pattern: str=None):
    channel = ctx.message.channel
    author = ctx.message.author
    await ctx.message.edit(content="`Deleting messages...`")
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
    await slow_deletion(to_delete)
    await ctx.message.delete()


# Added for extra future use
async def slow_deletion(messages):
    for message in messages:
        try:
            await bot.message.delete()
        except:
            pass

@bot.command(pass_context=True, name='eval')
async def _eval(ctx, *, code: str):
    """Evaluates code."""
    if advancedmode == "True":
        code = code.strip('` ')
        if code == "token":
            await say(ctx.message, "You probably don't want to show your token.".format(invoker))
        elif code == "email":
            await say(ctx.message, "You probably don't want to show your email."
                          " If you really do, please write {}eval str(email).".format(invoker))
        elif code == "password":
            await say(ctx.message, "You probably don't want to show your password.".format(invoker))
        else:
            python = '```py\n{}\n```'
            result = None

            env = {
                'ctx': ctx,
                'message': ctx.message,
                'guild': ctx.message.guild,
                'channel': ctx.message.channel,
                'author': ctx.message.author
            }

            env.update(globals())

            try:
                result = eval(code, env)
                if inspect.isawaitable(result):
                    result = await result
            except Exception as e:
                await say(python.format(type(e).__name__ + ': ' + str(e)))
                return
            em = discord.Embed(description=python.format(result))
            await ctx.message.edit(embed=em)
    else:
        r = await say(ctx.message, "This command is an `advanced mode` command.")
        await asyncio.sleep(3)
        await bot.delete_message(r)

def replcheck(msg):
    return msg.content.startswith('`') and msg.author==msg.guild.me

@bot.command(pass_context=True, name='repl')
async def repl(ctx):
    if advancedmode == "True":
        msg = ctx.message
        variables = {
            'ctx': ctx,
            'bot': bot,
            'message': msg,
            'guild': msg.guild,
            'channel': msg.channel,
            'author': msg.author,
            '_': None,
        }

        def cleanup_code(content):
            """Automatically removes code blocks from the code."""
            # remove ```py\n```
            if content.startswith('```') and content.endswith('```'):
                return '\n'.join(content.split('\n')[1:-1])

            # remove `foo`
            return content.strip('` \n')

        def get_syntax_error(e):
            if e.text is None:
                return '```py\n{0.__class__.__name__}: {0}\n```'.format(e)
            return '```py\n{0.text}{1:>{0.offset}}\n{2}: {0}```'.format(e, '^', type(e).__name__)
        if msg.channel.id in sessions:
            await msg.edit(content='Already running a REPL session in this channel. Exit it with `quit`.')
            return

        sessions.add(msg.channel.id)
        await msg.edit(content='Enter code to execute or evaluate. `exit()` or `quit` to exit.')
        while True:
            response = await bot.wait_for('message', check=replcheck)

            cleaned = cleanup_code(response.content)

            if cleaned in ('quit', 'exit', 'exit()'):
                await say(ctx.message, 'Exiting.')
                sessions.remove(msg.channel.id)
                return

            executor = exec
            if cleaned.count('\n') == 0:
                # single statement, potentially 'eval'
                try:
                    code = compile(cleaned, '<repl session>', 'eval')
                except SyntaxError:
                    pass
                else:
                    executor = eval

            if executor is exec:
                try:
                    code = compile(cleaned, '<repl session>', 'exec')
                except SyntaxError as e:
                    aaa = "**input:**```py\n{}```**output:**{}".format(cleaned,
                                                                       get_syntax_error(e))
                    await response.edit(content=aaa)
                    continue

            variables['message'] = response

            fmt = None
            stdout = io.StringIO()

            try:
                with redirect_stdout(stdout):
                    result = executor(code, variables)
                    if inspect.isawaitable(result):
                        result = await result
            except Exception as e:
                value = stdout.getvalue()
                fmt = '```py\n{}{}\n```'.format(value, traceback.format_exc())
            else:
                value = stdout.getvalue()
                if result is not None:
                    fmt = '```py\n{}{}\n```'.format(value, result)
                    variables['_'] = result
                elif value:
                    fmt = '```py\n{}\n```'.format(value)

            try:
                if fmt is not None:
                    if len(fmt) > 2000:
                        await response.edit(content='Content too big to be printed.')
                    else:
                        em = discord.Embed(description=fmt)
                        await response.edit(embed=em)
                elif fmt is None:
                    try:
                        await bot.add_reaction(response, '\u2705')
                    except:
                        pass
            except discord.Forbidden:
                pass
            except discord.HTTPException as e:
                uwotm8 = "**input:**```py\n{}```**output:**```py\nUnexpected error: {}```".format(cleaned,
                                                                                                    e)
                await response.edit(content=uwotm8)
    else:
        r = await msg.edit(content="This command is an `advanced mode` command.")
        await asyncio.sleep(3)
        await bot.delete_message(r)



@bot.command(pass_context=True)
async def memberundertale(ctx):
    haswith = ['Frisk', 'Flowey', 'Toriel', 'Papyrus', 'Sans', 'Undyne', 'Mettaton', 'Alphys', 'ASGORE', 'Asriel', 'Chara', 'Gaster', 'Temmie', 'Grillby']
    people = []

    for i in haswith:
        for member in ctx.message.guild.members:
            if i.lower() in member.display_name.lower():
                people.append(member)

    await ctx.message.edit(content="{} out of {} member(s) of this guild have undertale related nicknames or usernames.".format(len(people), len(ctx.message.guild.members)))


@bot.command(pass_context=True)
async def getinvite(ctx, *, invitearg = None):
    if invitearg:
        #guilda = discord.utils.get(bot.guilds, name=invitearg)
        guilda = discord.utils.get(bot.guilds, name=invitearg)
        if not guilda == None:
            invitea = await bot.create_invite(guilda)
        else:
            invitea = "That guild doesn't exist."
        await say(invitea)
        return
    invite = await bot.create_invite(ctx.message.guild)
    await say(invite)

@bot.command(pass_context=True)
async def changelog(ctx):
    await say(ctx.message, "Changes for {}:\n{}".format(botversion, changes))
# ----- Non useful commands ----- #

@bot.command(pass_context=True)
async def changeavy(ctx):
    #wew
    if ctx.message.author.id == 155651120344203265:
        filename = random.choice(os.listdir(".\\Resources\\gla\\"))
        randavy = open(".\\Resources\\gla\\" + filename, 'rb')
        await bot.edit_profile(avatar=randavy.read(), password = password)
        await say(ctx.message, "Your avatar has been changed.")
    else:
        pass

@bot.command(pass_context=True, name="beemovie!")
async def _beemovie(ctx):
    #If you use this, rest in... don't use this.
    if ctx.message.author.id == 155651120344203265:
        with open(r".\Resources\beemovie.txt", 'r') as beem:
            beemoviet = beem.read()
            textline = textwrap.wrap(beemoviet, width=2000)
            for line in textline:
                await say(ctx.message, line.replace("\\n", "\n"))
                await asyncio.sleep(1)
    else:
        pass

@bot.group(pass_context=True)
async def blur(ctx):
    if ctx.subcommand_passed is None:
        if ctx.message.attachments != []:
            attachtoretrieve = urllib.request.Request(
                ctx.message.attachments[0]['url'],
                data=None,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                    }
                )
            actuallyretrieving = urllib.request.urlopen(attachtoretrieve)
            with open("OhYes.png", 'wb') as f:
                f.write(actuallyretrieving.read())
                f.close()
                actuallyretrieving.close()
            image = Image.open('OhYes.png')
            inverted_image = image.filter(ImageFilter.GaussianBlur(radius=2))
            inverted_image.save('result.png')
            await ctx.message.channel.send(file=discord.File("result.png"))
            os.remove("result.png")
        else:
            await say(ctx.message, "Please enter a link after the command.")
    else:
        attachtoretrieve = urllib.request.Request(
            ctx.subcommand_passed,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                }
            )
        actuallyretrieving = urllib.request.urlopen(attachtoretrieve)
        with open("OhYes.png", 'wb') as f:
            f.write(actuallyretrieving.read())
            f.close()
            actuallyretrieving.close()
        image = Image.open('OhYes.png')
        inverted_image = image.filter(ImageFilter.GaussianBlur(radius=2))
        inverted_image.save('result.png')
        await ctx.message.channel.send(file=discord.File("result.png"))
        os.remove("result.png")

@bot.command(pass_context=True)
async def undertext(ctx, *, inputtext):
    def _path(): # Some temporary path fix (Since the Current method wont work on OS's other than windows)
        _os = platform.system()
        if _os == "Linux" or _os == "Darwin":
            return "/", " "
        if _os == "Windows":
            return "\\", ".\\"
    p1 = _path()[0]
    p2 = _path()[1]
    img = Image.open("%Resources$Images$Input$Textbox.png".replace("%", p2).replace("$", p1))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("%Resources$Fonts$DTM-Mono.otf".replace("%", p2).replace("$", p1), 130)
    margin = 170
    offset = 100
    textline = textwrap.wrap(inputtext, width=33)
    for line in textline:
        draw.text((margin, offset), line,(255,255,255),font=font)
        offset += 200
    img.save("%Resources$Images$Output$Textbox.png".replace("%", p2).replace("$", p1))
    await ctx.message.channel.send(file=discord.File("%Resources$Images$Output$Textbox.png".replace("%", p2).replace("$", p1)))
    os.remove("%Resources$Images$Output$Textbox.png".replace("%", p2).replace("$", p1))

@bot.group(pass_context=True)
async def invert(ctx):
    if ctx.subcommand_passed is None:
        if ctx.message.attachments != []:
            attachtoretrieve = urllib.request.Request(
                ctx.message.attachments[0]['url'],
                data=None,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                    }
                )
            actuallyretrieving = urllib.request.urlopen(attachtoretrieve)
            with open("OhYes.png", 'wb') as f:
                f.write(actuallyretrieving.read())
                f.close()
                actuallyretrieving.close()
            image = Image.open('OhYes.png')
            inverted_image = PIL.ImageOps.invert(image)
            inverted_image.save('result.png')
            await ctx.message.channel.send(file=discord.File("result.png"))
            os.remove("result.png")
        else:
            await say(ctx.message, "Please enter a link after the command.")
    else:
        attachtoretrieve = urllib.request.Request(
            ctx.subcommand_passed,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                }
            )
        actuallyretrieving = urllib.request.urlopen(attachtoretrieve)
        with open("OhYes.png", 'wb') as f:
            f.write(actuallyretrieving.read())
            f.close()
            actuallyretrieving.close()
        image = Image.open('OhYes.png')
        inverted_image = PIL.ImageOps.invert(image)
        inverted_image.save('result.png')
        await ctx.message.channel.send(file=discord.File("result.png"))
        os.remove("result.png")

@bot.command(pass_context=True)
async def f(ctx):
    await ctx.message.edit(content="`Respects have been paid.`")
    await bot.add_reaction(ctx.message, '\U0001f1eb')

def charreplace(charset, input):
    # Data Converter
    regular = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ -=[]\\'/.,<>?:;|+_)(*&^%$#@!\"{}"
    characterset = charset
    converter = dict((ord(x[0]), x[1]) for x in zip(regular, characterset))
    input = input.translate(converter)
    # Output Builder
    result = "" + input + ""
    # Final Task
    return result

@bot.command(pass_context=True)
async def aesthetics(ctx):
    """wewlad"""
    try:
        arg = ctx.message.clean_content.split(" ", 1)[1]
        await ctx.message.edit(content=charreplace("ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ１２３４５６７８９０ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ －＝［］＼＇／．，＜＞？：；｜＋＿）（＊＆＾％＄＃＠！＂｛｝", arg))
    except IndexError:
        pass

@bot.command(pass_context=True)
async def cat(ctx):
    """random cat"""
    r = requests.get('http://random.cat/meow')
    if r.status_code == 200:
        url = r.json()["file"]
        await say(ctx.message, "{}, Here's your cat!\n{}".format(ctx.message.author.mention, url))

@bot.command()
async def brainfuck(code : str):
    """runs brainfuck code"""
    x = "py -3.5 ./Resources/bfcomp.py {}".format(code)
    result = sp.run(x, stdout=sp.PIPE)
    result = codecs.decode(result.stdout)
    result = "```\n{}\n```".format(result)
    await say(result)

#try:
if token == "None": # For People that use Email and Password.
    print("Please enter your token into the config file.")
    sys.exit()
else:
    bot.run(token, bot=False)
#except:
#    print("There was a problem logging in.")
#    print("Check your internet connection.")
#    print("If you haven't already, please add your credentials in config.json,")
#    print("and make sure they're correct.")
#    time.sleep(5)
#    sys.exit()