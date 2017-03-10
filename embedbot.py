# Embedbot 1.7 made by -Kiwi Catnip ♡#1540, @isy#0669, @HYP3RD34TH#2104 @Nikitaw99#4332.
# Thanks to @Dav999#3322 for helping with the code a lot.
# Thanks to @Info Teddy#3737 for the help code that I stole from [\].
# Oops.
botversion = "1.7" # displayed in the info command
changes = "better command-line argument parsing"

# argument parsing
import argparse
print("Imported argparse...")
x = 'embedbot by -Kiwi Catnip ♡#1540, @isy#0669, @HYP3RD34TH#2104 @Nikitaw99#4332'
parser = argparse.ArgumentParser(description=x)
parser.add_argument("config", type=str, help="config file. defaults to config.json")
x = "loadmode. 0 is dotdotdot, 1 is spinny line"
parser.add_argument("-l", "--loadmode", type=int, help=x)
x = "logging level. defaults to WARNING"
y = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
parser.add_argument("-d", "--debug", type=str, help=x, choices=y)
print("Parsing arguments...")
passedargs = parser.parse_args()
print("Arguments parsed.")
del x, y

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
import threading
logging.info("Imported threading...")
import itertools # probably iterator stuff? was used in loading screen (spinny line/dot dot dot)
logging.info("Imported itertools...")
import urllib.request
logging.info("Imported urllib.request...")
import textwrap # for wrapping the bee movie script
logging.info("Imported textwrap...")
import random # mostly for *shuffle, which doesnt work anyways
logging.info("Imported random...")
import pip # for installing packages
logging.info("Imported pip...")
import psutil
logging.info("Imported psutil...")
def install(package):
    """Install a package using pip"""
    pip.main(['install', package])
current_os = platform.system()
installlist = [] # list of things to install (i guess)
needinstall = False
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

del I

def clear_screen():
    """Clear stdout."""
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        tmp = sp.call('clear', shell=True)
    if current_os == "Windows":
        tmp = sp.call('cls', shell=True)

# some important stuff so that pip works
if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
    tmp = sp.call('clear', shell=True)
    pip_os = "pip3"
if current_os == "Windows":
    tmp = sp.call('cls', shell=True)
    pip_os = "pip"

starttime = datetime.datetime.now() # the current date + time

try:
    assert sys.version_info >= (3, 5) # bot incompatible with 3.4 and below
    from discord.ext import commands # ew, discord ext ~Nikitaw99
    import discord # guess what this is for
except ImportError: # if discord.py aint installed
    a = "install discord.py"
    print("Discord.py is not installed.")
    print("Please install it using {}{} {}.".format(Fore.GREEN, pip_os, a))
    print("Also, you can install the dev versions from here:")
    print("https://github.com/Rapptz/discord.py")
    print("Note: If you get an error saying pip doesn't exist, try this:")
    print("\"Your python installation path\\Scripts\\pip.exe install discord.py\" (On Windows).")
    print("Also make sure you are running command prompt (or whatever you're using)\nas admin.")
    sys.exit()
except AssertionError: # bot incompatible with 3.4 and below
    print("Embedbot needs Python 3.5 or superior.")
    sys.exit()
x = ">>> from __future__ import barry_as_FLUFL\n>>> True != False\n"
y = "  File \"<stdin>\", line 1\n    True != False"
z = "\n          ^\nSyntaxError: invalid syntax\n>>> True <> False\nTrue"
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
    x+y+z
]
del x, y, z
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

# Config loading
try:
    customconfig = passedargs.config
except OSError:
    try:
        customconfig = "config.json" # config doesnt exist? then the bot will use default one.
    except OSError:
        print("Uh oh. The default config seems to be missing.")
        print("Attempting to fetch config from github...")
        # now let's download dat config
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
        token = jsonhandler['token'] # token
        email = jsonhandler['email'] # email
        password = jsonhandler['password'] # password
        invoker = jsonhandler['invoker'] # invoker, * by default
        textargs = jsonhandler['textargs']
        rminvokermsg = jsonhandler['autoremoveinvokermessage']
        advancedmode = jsonhandler['advancedmode'] # enables eval
        silent = jsonhandler['silentmode']

except json.JSONDecodeError:
    x = "There was a problem with your config file. Make sure that everything is up to date."
    y = "\nIf it still doesn't work, try deleting the config file and creating it again. "
    z = "Don't use notepad for editing, use notepad++!"
    print(x+y+z)
    del x, y, z

print(random.choice(starttext))
if passedargs.loadmode:
    if loadmode == 0:
        load = itertools.cycle(['.  ', '.. ', '...', '   '])
    elif loadmode == 1:
        load = itertools.cycle(['|', '/', '-', '\\'])
    else:
        print("Invalid loadmode argument. Using default...")
        load = itertools.cycle(['.  ', '.. ', '...', '   '])
else:
    load = itertools.cycle(['.  ', '.. ', '...', '   '])

if passedargs.loadmode:
    if passedargs.loadmode == 0:
        load = itertools.cycle(['.  ', '.. ', '...', '   '])
    else:
        load = itertools.cycle(['|', '/', '-', '\\'])
else:
    load = itertools.cycle(['.  ', '.. ', '...', '   '])

sys.stdout.write('Logging in to Discord ')
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
                    sys.stdout.write('\b')
            else:
                sys.stdout.write('\b\b\b')
            time.sleep(0.5)
            if not getattr(t, "do_run", True):
                break
thread = threading.Thread(target=loggingin)
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
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        tmp = sp.call('clear', shell=True)
    if current_os == "Windows":
        tmp = sp.call('cls', shell=True)
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    login_time = datetime.datetime.now() - starttime
    login_time = login_time.seconds + login_time.microseconds/1E6
    print("=================================================================")
    print("                 -Embedbot - Discord Selfbot-")
    print("   By -Kiwi Catnip \\u2661#1540, isy#0669, HYP3RD34TH#2104.")
    print("                      and Nikitaw99#4332")
    print("=================================================================")
    print("Login time         : {} milliseconds".format(login_time))
    x = "Logged in as       : {} ({})"
    y = x.format(str(bot.user).encode("ascii", "backslashreplace").decode(), bot.user.id)
    print(y)
    del x, y
    print("Connected to       : {} servers and {} channels".format(servers, channels))
    print("-----------------------------------------------------------------")
    print("Python version     : {}.{}.{}".format(*os.sys.version_info[:3]))
    print("Discord.py version : {}".format(discord.__version__))
    print("Embedbot version   : {}".format(botversion))
    print("-----------------------------------------------------------------")
    c = "install clint"
    if silent == "True" or rminvokermsg == "True":
        if silent == "True" and rminvokermsg == "True":
            print(Fore.YELLOW + 'Silentmode is not implemented yet.')
            print(Fore.YELLOW + 'Autoremove invoker message is not implemented yet.')
            print("-----------------------------------------------------------------")
        elif silent == "True" and rminvokermsg == "False":
            print(Fore.YELLOW + 'Silentmode is not implemented yet.')
            print("-----------------------------------------------------------------")
        elif silent == "False" and rminvokermsg == "True":
            print(Fore.YELLOW + 'Autoremove invoker message is not fully implemented yet.')
            print("-----------------------------------------------------------------")
        else:
            pass
    x = Fore.LIGHTGREEN_EX + '  If you get any errors, please join our support server with \n  the '
    y = Fore.LIGHTCYAN_EX + '{}support '.format(invoker) + Fore.LIGHTGREEN_EX
    z = 'command to complain about how we can\'t code.'
    print(x+y+z)
    del x, y, z
    print("=================================================================")
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
            if type(ctx.message.channel) == discord.PrivateChannel:
                embedsendable = True
                em = discord.Embed(description="Help", colour=0xFFFFFF)
            elif ctx.message.server.me.permissions_in(ctx.message.channel).embed_links == True:
                em = discord.Embed(description="Help", colour=ctx.message.author.color)
                embedsendable = True
            else:
                embedsendable = False
            if embedsendable:
                em.add_field(name="Normal commands:", value="embeds, quote, clean", inline=True)
                x = "info, update, cls, support, kill, restart, print, test"
                em.add_field(name="Helpful/technical commands:", value=x, inline=True)
                em.add_field(name="Profile commands:", value="game, nick, status", inline=True)
                x = "blur, undertext, invert, f, memberundertale"
                em.add_field(name="Useless commands:", value=x, inline=True)
                em.add_field(name="Advanced mode commands:", value="eval, repl", inline=True)
                x = "You can use {}help (command) to get the information of that command."
                em.set_footer(text=x.format(invoker))
                del x
                await bot.send_message(ctx.message.channel, embed=em)
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
            if type(ctx.message.channel) == discord.PrivateChannel:
                embed = discord.Embed(description=content.format(invoker), colour=0xFFFFFF)
            elif ctx.message.server.me.permissions_in(ctx.message.channel).embed_links == True:
                x = ctx.message.author.color
                embed = discord.Embed(description=content.format(invoker), colour=x)
                del x
            await bot.send_message(ctx.message.channel, embed=embed)

@bot.event
async def on_message(message):
    if textargs == "True":
        if message.author == bot.user:
            x = message.content.replace("{hug}","\\\\(^.^\\\\)").replace("{shrug}","¯\\_(ツ)_/¯")
            y = x.replace("{lenny}","( ͡° ͜ʖ ͡°)").replace("{disapprove}","ಠ\\_ಠ")
            z = y.replace("{tableflip}","(╯°□°）╯︵ ┻━┻").replace("{unflip}","┬─┬﻿ ノ( ゜-゜ノ)")
            x = z.replace("{unflip2}","​┬─┬ノ( º ⁓ ºノ)").replace("{unflip3}","┬─┬ノ( º _ ºノ)")
            y = x.replace("{cute}","(◕‿◕✿)").replace("{zwsp}","​").replace("{rtl}","\u202e")
            messagereplace = y
            del x, y, z
            if not message.content == messagereplace:
                await bot.edit_message(message, messagereplace)
    await bot.process_commands(message)
    
@bot.command(pass_context=True)
async def info(ctx):
    if type(ctx.message.channel) == discord.PrivateChannel:
        embedsendable = True
        em = discord.Embed(description="Embedbot information", colour=0xFFFFFF)
    elif ctx.message.server.me.permissions_in(ctx.message.channel).embed_links == True:
        em = discord.Embed(description="Embedbot information", colour=ctx.message.author.color) 
        embedsendable = True
    else:
        embedsendable = False
    if embedsendable:
        em.add_field(name="Discord.py version:", value="{}.{}.{} {}".format(discord.version_info[0], discord.version_info[1], discord.version_info[2], discord.version_info[3]), inline=True)
        em.add_field(name="Embedbot version:", value=botversion, inline=True)
        em.add_field(name="Made by:", value="-Kiwi Catnip ♡#1540, isy#0669, HYP3RD34TH#2104 and @Nikitaw99#4332.", inline=True)     
        em.add_field(name="According to all known laws of aviation,", value="a bee should not be able to fly.", inline=True)
        em.add_field(name="Github project:", value="https://www.github.com/Luigimaster1/embedbot", inline=True)
    try:
        await bot.edit_message(ctx.message, "​", embed=em)
    except:
        await bot.say("Discord.py version: {}.{}.{} {}\n",
        "Embedbot version: {}\n",
        "Made by: -Kiwi Catnip ♡#1540, isy#0669 and HYP3RD34TH#2104.\n",
        "According to all known laws of aviation, a bee should not be able to fly.\n",
        "Github project: https://www.github.com/Luigimaster1/embedbot"
        .format(discord.version_info[0], discord.version_info[1], discord.version_info[2], discord.version_info[3], botversion))

@bot.command(pass_context=True)
async def update(ctx):
    await bot.say("Updating...")
    import platform
    try:
        from git import Repo
    except ImportError:
        await bot.say("Please install the module gitpython.".format(pip_os))
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
    await bot.say("The bot has been updated. Please restart the bot.")
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
            os.system('"' + __file__ + '"')
        else:
            os.system('"' + __file__ + '" ' + passedargs)
    if current_os == "Linux":
        if passedargs == None:
            os.system('''sudo bash -c "python3 {}"'''.format('"' + __file__ + '"'))
        else:
            os.system('''sudo bash -c "python3 {} {}"'''.format('"' + __file__ + '" ' + passedargs))
    await bot.logout()

@bot.command(pass_context=True)
async def nick(ctx):
    try:
        cmdarg = ctx.message.content.split(" ", 1)[1]
        try:
            await bot.change_nickname(ctx.message.server.me, cmdarg)
            await asyncio.sleep(0.3)
            await bot.edit_message(ctx.message, "Your nickname on this server has been changed to **{}**.".format(cmdarg))
            await asyncio.sleep(3)
            await bot.delete_message(ctx.message)
        except:
            await bot.edit_message(ctx.message, "Your nickname could not be changed on this server.")
        await asyncio.sleep(3)
        await bot.delete_message(ctx.message)
    except IndexError:
        await bot.change_nickname(ctx.message.server.me, "")
        await asyncio.sleep(0.3)
        await bot.edit_message(ctx.message, "Your nickname on this server has been reset.")
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
async def quote(ctx, *, asdf):
    asdf = discord.utils.get(bot.messages, id=asdf)
    if asdf.content is not None:
        if type(ctx.message.channel) == discord.PrivateChannel:
            em = discord.Embed(description=asdf.content, timestamp=asdf.timestamp, colour=0xFFFFFF)
            em.set_author(name=asdf.author.display_name, icon_url=asdf.author.avatar_url)
            await bot.edit_message(ctx.message, "​", embed=em)
        else:
            if ctx.message.server.me.permissions_in(ctx.message.channel).embed_links == True:
                if asdf.author.colour == "#000000":
                    colour = "0xFFFFFF"
                else:
                    colour = asdf.author.colour
                em = discord.Embed(description=asdf.content, timestamp=asdf.timestamp, colour=colour)
                em.set_author(name=asdf.author.display_name, icon_url=asdf.author.avatar_url)
                await bot.edit_message(ctx.message, "​", embed=em)
            else:
                await bot.edit_message(ctx.message,
                                       "I need the `embed links` permission to send an embed.")
    else:
        await bot.edit_message(ctx.message, "`Could not find the message specified.`")


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
    await bot.edit_message(ctx.message, "`Deleting messages...`")
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
    await bot.edit_message(ctx.message, "`Task completed...`")
    await asyncio.sleep(3)
    await bot.delete_message(ctx.message)
    

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

@bot.command(pass_context=True, name='repl')
async def repl(ctx):
    if advancedmode == "True":
        msg = ctx.message
        variables = {
            'ctx': ctx,
            'bot': bot,
            'message': msg,
            'server': msg.server,
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
            await bot.edit_message(msg,
                                   'Already running a REPL session in this channel. Exit it with `quit`.')
            return

        sessions.add(msg.channel.id)
        await bot.edit_message(msg,
                               'Enter code to execute or evaluate. `exit()` or `quit` to exit.')
        while True:
            response = await bot.wait_for_message(author=msg.author, channel=msg.channel,
                                                  check=lambda m: m.content.startswith('`'))

            cleaned = cleanup_code(response.content)

            if cleaned in ('quit', 'exit', 'exit()'):
                await bot.say('Exiting.')
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
                    await bot.edit_message(response, aaa)
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
                        await bot.edit_message(response, 'Content too big to be printed.')
                    else:
                        fmt = "**input:**```py\n{}```**output:**{}".format(cleaned,
                                                                            fmt)
                        await bot.edit_message(response, fmt)
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
                await bot.edit_message(response, uwotm8)       
    else:
        r = await bot.edit_message(msg, "This command is an `advanced mode` command.")
        await asyncio.sleep(3)
        await bot.delete_message(r)        
        
        
        
@bot.command(pass_context=True)
async def memberundertale(ctx):
    haswith = ['Frisk', 'Flowey', 'Toriel', 'Papyrus', 'Sans', 'Undyne', 'Mettaton', 'Alphys', 'ASGORE', 'Asriel', 'Chara', 'Gaster', 'Temmie', 'Grillby']
    people = []

    for i in haswith:
        for member in ctx.message.server.members:
            if i.lower() in member.display_name.lower():
                people.append(member)

    await bot.edit_message(ctx.message, "{} out of {} member(s) of this server have undertale related nicknames or usernames.".format(len(people), len(ctx.message.server.members)))

    
@bot.command(pass_context=True)
async def getinvite(ctx, *, invitearg = None):
    if invitearg: 
        #servera = discord.utils.get(bot.servers, name=invitearg)
        servera = discord.utils.get(bot.servers, name=invitearg)
        if not servera == None:
            invitea = await bot.create_invite(servera)
        else:
            invitea = "That server doesn't exist."
        await bot.say(invitea)
        return
    invite = await bot.create_invite(ctx.message.server)
    await bot.say(invite)

@bot.command(pass_context=True)
async def changelog(ctx):
    await bot.say("Changes for {}:\n{}".format(botversion, changes))
# ----- Non useful commands ----- #

@bot.command(pass_context=True, name="**beemovie***")
async def _beemovie(ctx):
    #If you use this, rest in... you're dumb if you use this.
    if ctx.message.author.id == "155651120344203265":
        with open(r".\Resources\beemovie.txt", 'r') as beem:
            beemoviet = beem.read()
            textline = textwrap.wrap(beemoviet, width=2000)
            for line in textline:
                await bot.say(line)
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
            await bot.send_file(ctx.message.channel, "result.png")
            os.remove("result.png")
        else:
            await bot.say("Please enter a link after the command.")
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
        await bot.send_file(ctx.message.channel, "result.png")
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
    await bot.send_file(ctx.message.channel, "%Resources$Images$Output$Textbox.png".replace("%", p2).replace("$", p1))
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
            await bot.send_file(ctx.message.channel, "result.png")
            os.remove("result.png")
        else:
            await bot.say("Please enter a link after the command.")
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
        await bot.send_file(ctx.message.channel, "result.png")
        os.remove("result.png")

@bot.command(pass_context=True)
async def f(ctx):
    await bot.edit_message(ctx.message, "`Respects have been paid.`")
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
        await bot.edit_message(ctx.message, charreplace("ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ１２３４５６７８９０ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ －＝［］＼＇／．，＜＞？：；｜＋＿）（＊＆＾％＄＃＠！＂｛｝", arg))
    except IndexError:
        pass

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
        elif len(token) > 90: # Checking Token's Length.
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
        else:
            bot.run(token, bot=False)
except:
    print("There was a problem logging in.")
    print("Check your internet connection.")
    print("If you haven't already, please add your credentials in config.json,")
    print("and make sure they're correct.")
    time.sleep(5)
    sys.exit()
