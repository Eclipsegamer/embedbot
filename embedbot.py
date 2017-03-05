# Embedbot 1.6 made by -Kiwi Catnip ♡#1540, @isy#0669 and @HYP3RD34TH#2104.
# Thanks to @Dav999#3322 for helping with the code a lot.
# Thanks to @Info Teddy#3737 for the help code that I stole from [\].
# Oops.
botversion = "1.6"
changes = "*Edited the help command to use a json file instead of a elif chain."
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
import urllib.request
import textwrap
import random
import pip
from urllib import request
def install(package):
    pip.main(['install', package])
current_os = platform.system()
installlist = []
needinstall = False
try:
    from colorama import Fore, Back, Style
    import colorama
    colorama.init(autoreset=True)
    print("Imported colorama...")
except ImportError:
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        pip_os = "pip3"
    if current_os == "Windows":
        pip_os = "pip"
    installlist.append("colorama")
    print("Please run \"{} install colorama\".".format(pip_os))
    needinstall = True
try:
    from PIL import Image
    import PIL.ImageOps
    from PIL import ImageFilter
    from PIL import ImageFont
    from PIL import ImageDraw
    print("Imported pillow...")
except ImportError:
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        pip_os = "pip3"
    if current_os == "Windows":
        pip_os = "pip"
    installlist.append("pillow")
    print("Please run \"{} install pillow\".".format(pip_os))
    needinstall = True
try:
    import cursor
    print("Imported cursor...")
except ImportError:
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        pip_os = "pip3"
    if current_os == "Windows":
        pip_os = "pip"
    installlist.append("Cursor")
    print("Please run \"{} install Cursor\".".format(pip_os))
    needinstall = True
instimporterror = False
if needinstall:
    print("Attempting to install them.")
    for pipinstall in installlist:
            install(pipinstall)
    print("If there were any errors, please run embedbot with admininstrator privileges, or please use pip to install them.\nIf there was no errors, you can now run embedbot normally.")
    time.sleep(3)
    sys.exit()
print("Done.")
time.sleep(1)
logged_in = False
try:
    passedargs = sys.argv[1]
except:
    passedargs = None

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

starttime = datetime.datetime.now()

try:
    assert sys.version_info >= (3, 5)
    from discord.ext import commands
    import discord
except ImportError:
    a = "install discord.py"
    print("Discord.py is not installed.")
    print("Please install it using {}{} {}.".format(Fore.GREEN, pip_os, a))
    print("Also, you can install the dev versions from here:")
    print("https://github.com/Rapptz/discord.py")
    print("Note: If you get an error saying pip doesn't exist, try this:")
    print("\"Your python installation path\\Scripts\\pip.exe install discord.py\" (On Windows).")
    print("Also make sure you are running command prompt (or whatever you're using)\nas admin.")
    sys.exit()
except AssertionError:
    print("Embedbot needs Python 3.5 or superior.")
    sys.exit()
starttext = [
    "According to all laws of aviation...",
    "IT'S THE",
    "Uh oh!",
    "Now look at this net",
    "Deleting C drive...",
    "Installing Bonzi Buddy...",
    "Welcome back!",
    "Readying the felines...",
    "\"What are you saying you don't know how to code?\"",
    "Bad code awaits you.",
    "You ready for this?",
    "*Crunch* NO DON'T TOUCH THAT!",
    "BetterDiscord more like sweaterdiscord because nobody wants it"
]
# Strings loading
def loadstrings():
    # Totally not copied from [\]
    # sorry info
	stringsf = open('.\Resources\strings.json', 'r')
	stringsfr = stringsf.read()
	strings = json.loads(stringsfr)
	global cmds
	cmds = strings['cmds']

loadstrings()

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
        loadmode = jsonhandler['loadmode']
except:
    print("There was a problem with your config file. Make sure that everything is up to date.")

print(random.choice(starttext))
if loadmode == "0":
    load = itertools.cycle(['.  ', '.. ', '...', '   '])
    sys.stdout.write('Logging in to Discord')
else:
    load = itertools.cycle(['|', '/', '-', '\\'])
    sys.stdout.write('Logging in to Discord ')
cursor.hide()
def loggingin():
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        for i in range(0, 4):
            sys.stdout.write(load.__next__())
            sys.stdout.flush()
            if loadmode == "0":
                sys.stdout.write('\b\b\b')
            else:
                sys.stdout.write('\b')
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
				returnage += '\n\n__`{}:`__ - For command descriptions: **`\help {}`**'.format(cat['cat_name'], cat['cat_slug'])
			else:
				if cat['cat_desc'] != '':
					returnage += cat['cat_desc']
				returnage += '\n__`{}:`__'.format(cat['cat_name'])

			first = True
			for cmd in cat['commands']:
				if onlycat == None:
					if first:
						returnage += '\n`\{}`'.format(cmd['name'])
						first = False
					else:
						returnage += '   `\{}`'.format(cmd['name'])
				else:
					returnage += '\n`\{}` - {}'.format(cmd['name'], cmd['short'])
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
    if silent == "True" or rminvokermsg == "True":
        if silent == "True" and rminvokermsg == "True":
            print(Fore.YELLOW + 'Silentmode is not implemented yet.')
            print(Fore.YELLOW + 'Autoremove invoker message is not implemented yet.')
        elif silent == "True" and rminvokermsg == "False":
            print(Fore.YELLOW + 'Silentmode is not implemented yet.')
        elif silent == "False" and rminvokermsg == "True":
            print(Fore.YELLOW + 'Autoremove invoker message is not fully implemented yet.')
        else:
            pass
    print(Fore.LIGHTGREEN_EX + 'If you get any errors, please join our support server with \n  the ' + Fore.LIGHTCYAN_EX + '{}support '.format(invoker) + Fore.LIGHTGREEN_EX + 'command to complain about how we can\'t code.')
    print("-----------------------------------------------------------------")
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
                em.add_field(name="Helpful/technical commands:", value="info, update, cls, support, kill, restart, print, test", inline=True)
                em.add_field(name="Profile commands:", value="game, nick, status", inline=True)
                em.add_field(name="Useless commands:", value="blur, undertext, invert, f, memberundertale", inline=True)
                em.add_field(name="Advanced mode commands:", value="eval", inline=True)
                em.set_footer(text="You can use {}help (command) to get the information of that command.".format(invoker))
                await bot.send_message(ctx.message.channel, embed=em)
        if helpf == True:
            content = (helplist(cmds))

            # General
            if cmdarg == None:
                pass
            else:
                matched = False
                for cat in (cmds):
                    for cmd in cat['commands']: # Maybe have a nested try-except KeyError instead of looping through every command
                        if cmdarg == cmd['name']:
                            try:
                                content = '`{}{}` - {}'.format(invoker, cmd['name'], cmd['extrafull'])
                            except KeyError:
                                content = '`{}{}` - {}\n{}'.format(invoker, cmd['name'], cmd['short'], cmd['extra'])
                            matched = True
                            break
                    if matched:
                        break

                if not matched:
                    content = 'Invalid arguments passed, or the command is not in the help list.'
            if type(ctx.message.channel) == discord.PrivateChannel:
                embed = discord.Embed(description=content.format(invoker), colour=0xFFFFFF)
            elif ctx.message.server.me.permissions_in(ctx.message.channel).embed_links == True:
                embed = discord.Embed(description=content.format(invoker), colour=ctx.message.author.color)
            await bot.send_message(ctx.message.channel, embed=embed)

@bot.event
async def on_message(message):
    if textargs == "True":
        if message.author == bot.user:
            messagereplace = message.content.replace("{hug}","\\\\(^.^\\\\)").replace("{shrug}","¯\\_(ツ)_/¯").replace("{lenny}","( ͡° ͜ʖ ͡°)").replace("{disapprove}","ಠ\_ಠ").replace("{tableflip}","(╯°□°）╯︵ ┻━┻").replace("{unflip}","┬─┬﻿ ノ( ゜-゜ノ)").replace("{unflip2}","​┬─┬ノ( º ⁓ ºノ)").replace("{unflip3}","┬─┬ノ( º _ ºノ)").replace("{cute}","(◕‿◕✿)").replace("{zwsp}","​").replace("{rtl}","\u202e") # This long ass line makes me want to kms ~ Hyp3r
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
        em.add_field(name="Made by:", value="-Kiwi Catnip ♡#1540, isy#0669 and HYP3RD34TH#2104.", inline=True)	 
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
    except:
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
        beemovie = "According to all known laws of aviation,\nthere is no way a bee should be able to fly.\nIts wings are too small to get its fat little body off the ground.\nThe bee, of course, flies anyway\nbecause bees don't care what humans think is impossible.\nYellow, black. Yellow, black. Yellow, black. Yellow, black.\nOoh, black and yellow! Let's shake it up a little.\nBarry! Breakfast is ready!\nOoming!\nHang on a second.\nHello?\n- Barry? - Adam?\n- Can you believe this is happening? - I can't. I'll pick you up.\nLooking sharp.\nUse the stairs. Your father paid good money for those.\nSorry. I'm excited.\nHere's the graduate. We're very proud of you, son.\nA perfect report card, all B's.\nVery proud.\nMa! I got a thing going here.\n- You got lint on your fuzz. - Ow! That's me!\n- Wave to us! We'll be in row 118,000. - Bye!\nBarry, I told you, stop flying in the house!\n- Hey, Adam. - Hey, Barry.\n- Is that fuzz gel? - A little. Special day, graduation.\nNever thought I'd make it.\nThree days grade school, three days high school.\nThose were awkward.\nThree days college. I'm glad I took a day and hitchhiked around the hive.\nYou did come back different.\n- Hi, Barry. - Artie, growing a mustache? Looks good.\n- Hear about Frankie? - Yeah.\n- You going to the funeral? - No, I'm not going.\nEverybody knows, sting someone, you die.\nDon't waste it on a squirrel. Such a hothead.\nI guess he could have just gotten out of the way.\nI love this incorporating an amusement park into our day.\nThat's why we don't need vacations.\nBoy, quite a bit of pomp... under the circumstances.\n- Well, Adam, today we are men. - We are!\n- Bee-men. - Amen!\nHallelujah!\nStudents, faculty, distinguished bees,\nplease welcome Dean Buzzwell.\nWelcome, New Hive Oity graduating class of...\n...9:15.\nThat concludes our ceremonies.\nAnd begins your career at Honex Industries!\nWill we pick ourjob today?\nI heard it's just orientation.\nHeads up! Here we go.\nKeep your hands and antennas inside the tram at all times.\n- Wonder what it'll be like? - A little scary.\nWelcome to Honex, a division of Honesco\nand a part of the Hexagon Group.\nThis is it!\nWow.\nWow.\nWe know that you, as a bee, have worked your whole life\nto get to the point where you can work for your whole life.\nHoney begins when our valiant Pollen Jocks bring the nectar to the hive.\nOur top-secret formula\nis automatically color-corrected, scent-adjusted and bubble-contoured\ninto this soothing sweet syrup\nwith its distinctive golden glow you know as...\nHoney!\n- That girl was hot. - She's my cousin!\n- She is? - Yes, we're all cousins.\n- Right. You're right. - At Honex, we constantly strive\nto improve every aspect of bee existence.\nThese bees are stress-testing a new helmet technology.\n- What do you think he makes? - Not enough.\nHere we have our latest advancement, the Krelman.\n- What does that do? - Oatches that little strand of honey\nthat hangs after you pour it. Saves us millions.\nCan anyone work on the Krelman?\nOf course. Most bee jobs are small ones. But bees know\nthat every small job, if it's done well, means a lot.\nBut choose carefully\nbecause you'll stay in the job you pick for the rest of your life.\nThe same job the rest of your life? I didn't know that.\nWhat's the difference?\nYou'll be happy to know that bees, as a species, haven't had one day off\nin 27 million years.\nSo you'll just work us to death?\nWe'll sure try.\nWow! That blew my mind!\n\"What's the difference?\" How can you say that?\nOne job forever? That's an insane choice to have to make.\nI'm relieved. Now we only have to make one decision in life.\nBut, Adam, how could they never have told us that?\nWhy would you question anything? We're bees.\nWe're the most perfectly functioning society on Earth.\nYou ever think maybe things work a little too well here?\nLike what? Give me one example.\nI don't know. But you know what I'm talking about.\nPlease clear the gate. Royal Nectar Force on approach.\nWait a second. Oheck it out.\n- Hey, those are Pollen Jocks! - Wow.\nI've never seen them this close.\nThey know what it's like outside the hive.\nYeah, but some don't come back.\n- Hey, Jocks! - Hi, Jocks!\nYou guys did great!\nYou're monsters! You're sky freaks! I love it! I love it!\n- I wonder where they were. - I don't know.\nTheir day's not planned.\nOutside the hive, flying who knows where, doing who knows what.\nYou can'tjust decide to be a Pollen Jock. You have to be bred for that.\nRight.\nLook. That's more pollen than you and I will see in a lifetime.\nIt's just a status symbol. Bees make too much of it.\nPerhaps. Unless you're wearing it and the ladies see you wearing it.\nThose ladies? Aren't they our cousins too?\nDistant. Distant.\nLook at these two.\n- Oouple of Hive Harrys. - Let's have fun with them.\nIt must be dangerous being a Pollen Jock.\nYeah. Once a bear pinned me against a mushroom!\nHe had a paw on my throat, and with the other, he was slapping me!\n- Oh, my! - I never thought I'd knock him out.\nWhat were you doing during this?\nTrying to alert the authorities.\nI can autograph that.\nA little gusty out there today, wasn't it, comrades?\nYeah. Gusty.\nWe're hitting a sunflower patch six miles from here tomorrow.\n- Six miles, huh? - Barry!\nA puddle jump for us, but maybe you're not up for it.\n- Maybe I am. - You are not!\nWe're going 0900 at J-Gate.\nWhat do you think, buzzy-boy? Are you bee enough?\nI might be. It all depends on what 0900 means.\nHey, Honex!\nDad, you surprised me.\nYou decide what you're interested in?\n- Well, there's a lot of choices. - But you only get one.\nDo you ever get bored doing the same job every day?\nSon, let me tell you about stirring.\nYou grab that stick, and you just move it around, and you stir it around.\nYou get yourself into a rhythm. It's a beautiful thing.\nYou know, Dad, the more I think about it,\nmaybe the honey field just isn't right for me.\nYou were thinking of what, making balloon animals?\nThat's a bad job for a guy with a stinger.\nJanet, your son's not sure he wants to go into honey!\n- Barry, you are so funny sometimes. - I'm not trying to be funny.\nYou're not funny! You're going into honey. Our son, the stirrer!\n- You're gonna be a stirrer? - No one's listening to me!\nWait till you see the sticks I have.\nI could say anything right now. I'm gonna get an ant tattoo!\nLet's open some honey and celebrate!\nMaybe I'll pierce my thorax. Shave my antennae.\nShack up with a grasshopper. Get a gold tooth and call everybody \"dawg\"!\nI'm so proud.\n- We're starting work today! - Today's the day.\nOome on! All the good jobs will be gone.\nYeah, right.\nPollen counting, stunt bee, pouring, stirrer, front desk, hair removal...\n- Is it still available? - Hang on. Two left!\nOne of them's yours! Oongratulations! Step to the side.\n- What'd you get? - Picking crud out. Stellar!\nWow!\nOouple of newbies?\nYes, sir! Our first day! We are ready!\nMake your choice.\n- You want to go first? - No, you go.\nOh, my. What's available?\nRestroom attendant's open, not for the reason you think.\n- Any chance of getting the Krelman? - Sure, you're on.\nI'm sorry, the Krelman just closed out.\nWax monkey's always open.\nThe Krelman opened up again.\nWhat happened?\nA bee died. Makes an opening. See? He's dead. Another dead one.\nDeady. Deadified. Two more dead.\nDead from the neck up. Dead from the neck down. That's life!\nOh, this is so hard!\nHeating, cooling, stunt bee, pourer, stirrer,\nhumming, inspector number seven, lint coordinator, stripe supervisor,\nmite wrangler. Barry, what do you think I should... Barry?\nBarry!\nAll right, we've got the sunflower patch in quadrant nine...\nWhat happened to you? Where are you?\n- I'm going out. - Out? Out where?\n- Out there. - Oh, no!\nI have to, before I go to work for the rest of my life.\nYou're gonna die! You're crazy! Hello?\nAnother call coming in.\nIf anyone's feeling brave, there's a Korean deli on 83rd\nthat gets their roses today.\nHey, guys.\n- Look at that. - Isn't that the kid we saw yesterday?\nHold it, son, flight deck's restricted.\nIt's OK, Lou. We're gonna take him up.\nReally? Feeling lucky, are you?\nSign here, here. Just initial that.\n- Thank you. - OK.\nYou got a rain advisory today,\nand as you all know, bees cannot fly in rain.\nSo be careful. As always, watch your brooms,\nhockey sticks, dogs, birds, bears and bats.\nAlso, I got a couple of reports of root beer being poured on us.\nMurphy's in a home because of it, babbling like a cicada!\n- That's awful. - And a reminder for you rookies,\nbee law number one, absolutely no talking to humans!\nAll right, launch positions!\nBuzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz!\nBlack and yellow!\nHello!\nYou ready for this, hot shot?\nYeah. Yeah, bring it on.\nWind, check.\n- Antennae, check. - Nectar pack, check.\n- Wings, check. - Stinger, check.\nScared out of my shorts, check.\nOK, ladies,\nlet's move it out!\nPound those petunias, you striped stem-suckers!\nAll of you, drain those flowers!\nWow! I'm out!\nI can't believe I'm out!\nSo blue.\nI feel so fast and free!\nBox kite!\nWow!\nFlowers!\nThis is Blue Leader. We have roses visual.\nBring it around 30 degrees and hold.\nRoses!\n30 degrees, roger. Bringing it around.\nStand to the side, kid. It's got a bit of a kick.\nThat is one nectar collector!\n- Ever see pollination up close? - No, sir.\nI pick up some pollen here, sprinkle it over here. Maybe a dash over there,\na pinch on that one. See that? It's a little bit of magic.\nThat's amazing. Why do we do that?\nThat's pollen power. More pollen, more flowers, more nectar, more honey for us.\nOool.\nI'm picking up a lot of bright yellow. Oould be daisies. Don't we need those?\nOopy that visual.\nWait. One of these flowers seems to be on the move.\nSay again? You're reporting a moving flower?\nAffirmative.\nThat was on the line!\nThis is the coolest. What is it?\nI don't know, but I'm loving this color.\nIt smells good. Not like a flower, but I like it.\nYeah, fuzzy.\nOhemical-y.\nOareful, guys. It's a little grabby.\nMy sweet lord of bees!\nCandy-brain, get off there!\nProblem!\n- Guys! - This could be bad.\nAffirmative.\nVery close.\nGonna hurt.\nMama's little boy.\nYou are way out of position, rookie!\nOoming in at you like a missile!\nHelp me!\nI don't think these are flowers.\n- Should we tell him? - I think he knows.\nWhat is this?!\nMatch point!\nYou can start packing up, honey, because you're about to eat it!\nYowser!\nGross.\nThere's a bee in the car!\n- Do something! - I'm driving!\n- Hi, bee. - He's back here!\nHe's going to sting me!\nNobody move. If you don't move, he won't sting you. Freeze!\nHe blinked!\nSpray him, Granny!\nWhat are you doing?!\nWow... the tension level out here is unbelievable.\nI gotta get home.\nCan't fly in rain.\nCan't fly in rain.\nCan't fly in rain.\nMayday! Mayday! Bee going down!\nKen, could you close the window please?\nKen, could you close the window please?\nOheck out my new resume. I made it into a fold-out brochure.\nYou see? Folds out.\nOh, no. More humans. I don't need this.\nWhat was that?\nMaybe this time. This time. This time. This time! This time! This...\nDrapes!\nThat is diabolical.\nIt's fantastic. It's got all my special skills, even my top-ten favorite movies.\nWhat's number one? Star Wars?\nNah, I don't go for that...\n...kind of stuff.\nNo wonder we shouldn't talk to them. They're out of their minds.\nWhen I leave a job interview, they're flabbergasted, can't believe what I say.\nThere's the sun. Maybe that's a way out.\nI don't remember the sun having a big 75 on it.\nI predicted global warming.\nI could feel it getting hotter. At first I thought it was just me.\nWait! Stop! Bee!\nStand back. These are winter boots.\nWait!\nDon't kill him!\nYou know I'm allergic to them! This thing could kill me!\nWhy does his life have less value than yours?\nWhy does his life have any less value than mine? Is that your statement?\nI'm just saying all life has value. You don't know what he's capable of feeling.\nMy brochure!\nThere you go, little guy.\nI'm not scared of him. It's an allergic thing.\nPut that on your resume brochure.\nMy whole face could puff up.\nMake it one of your special skills.\nKnocking someone out is also a special skill.\nRight. Bye, Vanessa. Thanks.\n- Vanessa, next week? Yogurt night? - Sure, Ken. You know, whatever.\n- You could put carob chips on there. - Bye.\n- Supposed to be less calories. - Bye.\nI gotta say something.\nShe saved my life. I gotta say something.\nAll right, here it goes.\nNah.\nWhat would I say?\nI could really get in trouble.\nIt's a bee law. You're not supposed to talk to a human.\nI can't believe I'm doing this.\nI've got to.\nOh, I can't do it. Oome on!\nNo. Yes. No.\nDo it. I can't.\nHow should I start it? \"You like jazz?\" No, that's no good.\nHere she comes! Speak, you fool!\nHi!\nI'm sorry.\n- You're talking. - Yes, I know.\nYou're talking!\nI'm so sorry.\nNo, it's OK. It's fine. I know I'm dreaming.\nBut I don't recall going to bed.\nWell, I'm sure this is very disconcerting.\nThis is a bit of a surprise to me. I mean, you're a bee!\nI am. And I'm not supposed to be doing this,\nbut they were all trying to kill me.\nAnd if it wasn't for you...\nI had to thank you. It's just how I was raised.\nThat was a little weird.\n- I'm talking with a bee. - Yeah.\nI'm talking to a bee. And the bee is talking to me!\nI just want to say I'm grateful. I'll leave now.\n- Wait! How did you learn to do that? - What?\nThe talking thing.\nSame way you did, I guess. \"Mama, Dada, honey.\" You pick it up.\n- That's very funny. - Yeah.\nBees are funny. If we didn't laugh, we'd cry with what we have to deal with.\nAnyway...\nCan I...\n...get you something? - Like what?\nI don't know. I mean... I don't know. Ooffee?\nI don't want to put you out.\nIt's no trouble. It takes two minutes.\n- It's just coffee. - I hate to impose.\n- Don't be ridiculous! - Actually, I would love a cup.\nHey, you want rum cake?\n- I shouldn't. - Have some.\n- No, I can't. - Oome on!\nI'm trying to lose a couple micrograms.\n- Where? - These stripes don't help.\nYou look great!\nI don't know if you know anything about fashion.\nAre you all right?\nNo.\nHe's making the tie in the cab as they're flying up Madison.\nHe finally gets there.\nHe runs up the steps into the church. The wedding is on.\nAnd he says, \"Watermelon? I thought you said Guatemalan.\nWhy would I marry a watermelon?\"\nIs that a bee joke?\nThat's the kind of stuff we do.\nYeah, different.\nSo, what are you gonna do, Barry?\nAbout work? I don't know.\nI want to do my part for the hive, but I can't do it the way they want.\nI know how you feel.\n- You do? - Sure.\nMy parents wanted me to be a lawyer or a doctor, but I wanted to be a florist.\n- Really? - My only interest is flowers.\nOur new queen was just elected with that same campaign slogan.\nAnyway, if you look...\nThere's my hive right there. See it?\nYou're in Sheep Meadow!\nYes! I'm right off the Turtle Pond!\nNo way! I know that area. I lost a toe ring there once.\n- Why do girls put rings on their toes? - Why not?\n- It's like putting a hat on your knee. - Maybe I'll try that.\n- You all right, ma'am? - Oh, yeah. Fine.\nJust having two cups of coffee!\nAnyway, this has been great. Thanks for the coffee.\nYeah, it's no trouble.\nSorry I couldn't finish it. If I did, I'd be up the rest of my life.\nAre you...?\nCan I take a piece of this with me?\nSure! Here, have a crumb.\n- Thanks! - Yeah.\nAll right. Well, then... I guess I'll see you around.\nOr not.\nOK, Barry.\nAnd thank you so much again... for before.\nOh, that? That was nothing.\nWell, not nothing, but... Anyway...\nThis can't possibly work.\nHe's all set to go. We may as well try it.\nOK, Dave, pull the chute.\n- Sounds amazing. - It was amazing!\nIt was the scariest, happiest moment of my life.\nHumans! I can't believe you were with humans!\nGiant, scary humans! What were they like?\nHuge and crazy. They talk crazy.\nThey eat crazy giant things. They drive crazy.\n- Do they try and kill you, like on TV? - Some of them. But some of them don't.\n- How'd you get back? - Poodle.\nYou did it, and I'm glad. You saw whatever you wanted to see.\nYou had your \"experience.\" Now you can pick out yourjob and be normal.\n- Well... - Well?\nWell, I met someone.\nYou did? Was she Bee-ish?\n- A wasp?! Your parents will kill you! - No, no, no, not a wasp.\n- Spider? - I'm not attracted to spiders.\nI know it's the hottest thing, with the eight legs and all.\nI can't get by that face.\nSo who is she?\nShe's... human.\nNo, no. That's a bee law. You wouldn't break a bee law.\n- Her name's Vanessa. - Oh, boy.\nShe's so nice. And she's a florist!\nOh, no! You're dating a human florist!\nWe're not dating.\nYou're flying outside the hive, talking to humans that attack our homes\nwith power washers and M-80s! One-eighth a stick of dynamite!\nShe saved my life! And she understands me.\nThis is over!\nEat this.\nThis is not over! What was that?\n- They call it a crumb. - It was so stingin' stripey!\nAnd that's not what they eat. That's what falls off what they eat!\n- You know what a Oinnabon is? - No.\nIt's bread and cinnamon and frosting. They heat it up...\nSit down!\n...really hot! - Listen to me!\nWe are not them! We're us. There's us and there's them!\nYes, but who can deny the heart that is yearning?\nThere's no yearning. Stop yearning. Listen to me!\nYou have got to start thinking bee, my friend. Thinking bee!\n- Thinking bee. - Thinking bee.\nThinking bee! Thinking bee! Thinking bee! Thinking bee!\nThere he is. He's in the pool.\nYou know what your problem is, Barry?\nI gotta start thinking bee?\nHow much longer will this go on?\nIt's been three days! Why aren't you working?\nI've got a lot of big life decisions to think about.\nWhat life? You have no life! You have no job. You're barely a bee!\nWould it kill you to make a little honey?\nBarry, come out. Your father's talking to you.\nMartin, would you talk to him?\nBarry, I'm talking to you!\nYou coming?\nGot everything?\nAll set!\nGo ahead. I'll catch up.\nDon't be too long.\nWatch this!\nVanessa!\n- We're still here. - I told you not to yell at him.\nHe doesn't respond to yelling!\n- Then why yell at me? - Because you don't listen!\nI'm not listening to this.\nSorry, I've gotta go.\n- Where are you going? - I'm meeting a friend.\nA girl? Is this why you can't decide?\nBye.\nI just hope she's Bee-ish.\nThey have a huge parade of flowers every year in Pasadena?\nTo be in the Tournament of Roses, that's every florist's dream!\nUp on a float, surrounded by flowers, crowds cheering.\nA tournament. Do the roses compete in athletic events?\nNo. All right, I've got one. How come you don't fly everywhere?\nIt's exhausting. Why don't you run everywhere? It's faster.\nYeah, OK, I see, I see. All right, your turn.\nTiVo. You can just freeze live TV? That's insane!\nYou don't have that?\nWe have Hivo, but it's a disease. It's a horrible, horrible disease.\nOh, my.\nDumb bees!\nYou must want to sting all those jerks.\nWe try not to sting. It's usually fatal for us.\nSo you have to watch your temper.\nVery carefully. You kick a wall, take a walk,\nwrite an angry letter and throw it out. Work through it like any emotion:\nAnger, jealousy, lust.\nOh, my goodness! Are you OK?\nYeah.\n- What is wrong with you?! - It's a bug.\nHe's not bothering anybody. Get out of here, you creep!\nWhat was that? A Pic 'N' Save circular?\nYeah, it was. How did you know?\nIt felt like about 10 pages. Seventy-five is pretty much our limit.\nYou've really got that down to a science.\n- I lost a cousin to Italian Vogue. - I'll bet.\nWhat in the name of Mighty Hercules is this?\nHow did this get here? Oute Bee, Golden Blossom,\nRay Liotta Private Select?\n- Is he that actor? - I never heard of him.\n- Why is this here? - For people. We eat it.\nYou don't have enough food of your own?\n- Well, yes. - How do you get it?\n- Bees make it. - I know who makes it!\nAnd it's hard to make it!\nThere's heating, cooling, stirring. You need a whole Krelman thing!\n- It's organic. - It's our-ganic!\nIt's just honey, Barry.\nJust what?!\nBees don't know about this! This is stealing! A lot of stealing!\nYou've taken our homes, schools, hospitals! This is all we have!\nAnd it's on sale?! I'm getting to the bottom of this.\nI'm getting to the bottom of all of this!\nHey, Hector.\n- You almost done? - Almost.\nHe is here. I sense it.\nWell, I guess I'll go home now\nand just leave this nice honey out, with no one around.\nYou're busted, box boy!\nI knew I heard something. So you can talk!\nI can talk. And now you'll start talking!\nWhere you getting the sweet stuff? Who's your supplier?\nI don't understand. I thought we were friends.\nThe last thing we want to do is upset bees!\nYou're too late! It's ours now!\nYou, sir, have crossed the wrong sword!\nYou, sir, will be lunch for my iguana, Ignacio!\nWhere is the honey coming from?\nTell me where!\nHoney Farms! It comes from Honey Farms!\nOrazy person!\nWhat horrible thing has happened here?\nThese faces, they never knew what hit them. And now\nthey're on the road to nowhere!\nJust keep still.\nWhat? You're not dead?\nDo I look dead? They will wipe anything that moves. Where you headed?\nTo Honey Farms. I am onto something huge here.\nI'm going to Alaska. Moose blood, crazy stuff. Blows your head off!\nI'm going to Tacoma.\n- And you? - He really is dead.\nAll right.\nUh-oh!\n- What is that?! - Oh, no!\n- A wiper! Triple blade! - Triple blade?\nJump on! It's your only chance, bee!\nWhy does everything have to be so doggone clean?!\nHow much do you people need to see?!\nOpen your eyes! Stick your head out the window!\nFrom NPR News in Washington, I'm Oarl Kasell.\nBut don't kill no more bugs!\n- Bee! - Moose blood guy!!\n- You hear something? - Like what?\nLike tiny screaming.\nTurn off the radio.\nWhassup, bee boy?\nHey, Blood.\nJust a row of honey jars, as far as the eye could see.\nWow!\nI assume wherever this truck goes is where they're getting it.\nI mean, that honey's ours.\n- Bees hang tight. - We're all jammed in.\nIt's a close community.\nNot us, man. We on our own. Every mosquito on his own.\n- What if you get in trouble? - You a mosquito, you in trouble.\nNobody likes us. They just smack. See a mosquito, smack, smack!\nAt least you're out in the world. You must meet girls.\nMosquito girls try to trade up, get with a moth, dragonfly.\nMosquito girl don't want no mosquito.\nYou got to be kidding me!\nMooseblood's about to leave the building! So long, bee!\n- Hey, guys! - Mooseblood!\nI knew I'd catch y'all down here. Did you bring your crazy straw?\nWe throw it in jars, slap a label on it, and it's pretty much pure profit.\nWhat is this place?\nA bee's got a brain the size of a pinhead.\nThey are pinheads!\nPinhead.\n- Oheck out the new smoker. - Oh, sweet. That's the one you want.\nThe Thomas 3000!\nSmoker?\nNinety puffs a minute, semi-automatic. Twice the nicotine, all the tar.\nA couple breaths of this knocks them right out.\nThey make the honey, and we make the money.\n\"They make the honey, and we make the money\"?\nOh, my!\nWhat's going on? Are you OK?\nYeah. It doesn't last too long.\nDo you know you're in a fake hive with fake walls?\nOur queen was moved here. We had no choice.\nThis is your queen? That's a man in women's clothes!\nThat's a drag queen!\nWhat is this?\nOh, no!\nThere's hundreds of them!\nBee honey.\nOur honey is being brazenly stolen on a massive scale!\nThis is worse than anything bears have done! I intend to do something.\nOh, Barry, stop.\nWho told you humans are taking our honey? That's a rumor.\nDo these look like rumors?\nThat's a conspiracy theory. These are obviously doctored photos.\nHow did you get mixed up in this?\nHe's been talking to humans.\n- What? - Talking to humans?!\nHe has a human girlfriend. And they make out!\nMake out? Barry!\nWe do not.\n- You wish you could. - Whose side are you on?\nThe bees!\nI dated a cricket once in San Antonio. Those crazy legs kept me up all night.\nBarry, this is what you want to do with your life?\nI want to do it for all our lives. Nobody works harder than bees!\nDad, I remember you coming home so overworked\nyour hands were still stirring. You couldn't stop.\nI remember that.\nWhat right do they have to our honey?\nWe live on two cups a year. They put it in lip balm for no reason whatsoever!\nEven if it's true, what can one bee do?\nSting them where it really hurts.\nIn the face! The eye!\n- That would hurt. - No.\nUp the nose? That's a killer.\nThere's only one place you can sting the humans, one place where it matters.\nHive at Five, the hive's only full-hour action news source.\nNo more bee beards!\nWith Bob Bumble at the anchor desk.\nWeather with Storm Stinger.\nSports with Buzz Larvi.\nAnd Jeanette Ohung.\n- Good evening. I'm Bob Bumble. - And I'm Jeanette Ohung.\nA tri-county bee, Barry Benson,\nintends to sue the human race for stealing our honey,\npackaging it and profiting from it illegally!\nTomorrow night on Bee Larry King,\nwe'll have three former queens here in our studio, discussing their new book,\nOlassy Ladies, out this week on Hexagon.\nTonight we're talking to Barry Benson.\nDid you ever think, \"I'm a kid from the hive. I can't do this\"?\nBees have never been afraid to change the world.\nWhat about Bee Oolumbus? Bee Gandhi? Bejesus?\nWhere I'm from, we'd never sue humans.\nWe were thinking of stickball or candy stores.\nHow old are you?\nThe bee community is supporting you in this case,\nwhich will be the trial of the bee century.\nYou know, they have a Larry King in the human world too.\nIt's a common name. Next week...\nHe looks like you and has a show and suspenders and colored dots...\nNext week...\nGlasses, quotes on the bottom from the guest even though you just heard 'em.\nBear Week next week! They're scary, hairy and here live.\nAlways leans forward, pointy shoulders, squinty eyes, very Jewish.\nIn tennis, you attack at the point of weakness!\nIt was my grandmother, Ken. She's 81.\nHoney, her backhand's a joke! I'm not gonna take advantage of that?\nQuiet, please. Actual work going on here.\n- Is that that same bee? - Yes, it is!\nI'm helping him sue the human race.\n- Hello. - Hello, bee.\nThis is Ken.\nYeah, I remember you. Timberland, size ten and a half. Vibram sole, I believe.\nWhy does he talk again?\nListen, you better go 'cause we're really busy working.\nBut it's our yogurt night!\nBye-bye.\nWhy is yogurt night so difficult?!\nYou poor thing. You two have been at this for hours!\nYes, and Adam here has been a huge help.\n- Frosting... - How many sugars?\nJust one. I try not to use the competition.\nSo why are you helping me?\nBees have good qualities.\nAnd it takes my mind off the shop.\nInstead of flowers, people are giving balloon bouquets now.\nThose are great, if you're three.\nAnd artificial flowers.\n- Oh, those just get me psychotic! - Yeah, me too.\nBent stingers, pointless pollination.\nBees must hate those fake things!\nNothing worse than a daffodil that's had work done.\nMaybe this could make up for it a little bit.\n- This lawsuit's a pretty big deal. - I guess.\nYou sure you want to go through with it?\nAm I sure? When I'm done with the humans, they won't be able\nto say, \"Honey, I'm home,\" without paying a royalty!\nIt's an incredible scene here in downtown Manhattan,\nwhere the world anxiously waits, because for the first time in history,\nwe will hear for ourselves if a honeybee can actually speak.\nWhat have we gotten into here, Barry?\nIt's pretty big, isn't it?\nI can't believe how many humans don't work during the day.\nYou think billion-dollar multinational food companies have good lawyers?\nEverybody needs to stay behind the barricade.\n- What's the matter? - I don't know, I just got a chill.\nWell, if it isn't the bee team.\nYou boys work on this?\nAll rise! The Honorable Judge Bumbleton presiding.\nAll right. Oase number 4475,\nSuperior Oourt of New York, Barry Bee Benson v. the Honey Industry\nis now in session.\nMr. Montgomery, you're representing the five food companies collectively?\nA privilege.\nMr. Benson... you're representing all the bees of the world?\nI'm kidding. Yes, Your Honor, we're ready to proceed.\nMr. Montgomery, your opening statement, please.\nLadies and gentlemen of the jury,\nmy grandmother was a simple woman.\nBorn on a farm, she believed it was man's divine right\nto benefit from the bounty of nature God put before us.\nIf we lived in the topsy-turvy world Mr. Benson imagines,\njust think of what would it mean.\nI would have to negotiate with the silkworm\nfor the elastic in my britches!\nTalking bee!\nHow do we know this isn't some sort of\nholographic motion-picture-capture Hollywood wizardry?\nThey could be using laser beams!\nRobotics! Ventriloquism! Oloning! For all we know,\nhe could be on steroids!\nMr. Benson?\nLadies and gentlemen, there's no trickery here.\nI'm just an ordinary bee. Honey's pretty important to me.\nIt's important to all bees. We invented it!\nWe make it. And we protect it with our lives.\nUnfortunately, there are some people in this room\nwho think they can take it from us\n'cause we're the little guys! I'm hoping that, after this is all over,\nyou'll see how, by taking our honey, you not only take everything we have\nbut everything we are!\nI wish he'd dress like that all the time. So nice!\nOall your first witness.\nSo, Mr. Klauss Vanderhayden of Honey Farms, big company you have.\nI suppose so.\nI see you also own Honeyburton and Honron!\nYes, they provide beekeepers for our farms.\nBeekeeper. I find that to be a very disturbing term.\nI don't imagine you employ any bee-free-ers, do you?\n- No. - I couldn't hear you.\n- No. - No.\nBecause you don't free bees. You keep bees. Not only that,\nit seems you thought a bear would be an appropriate image for a jar of honey.\nThey're very lovable creatures.\nYogi Bear, Fozzie Bear, Build-A-Bear.\nYou mean like this?\nBears kill bees!\nHow'd you like his head crashing through your living room?!\nBiting into your couch! Spitting out your throw pillows!\nOK, that's enough. Take him away.\nSo, Mr. Sting, thank you for being here. Your name intrigues me.\n- Where have I heard it before? - I was with a band called The Police.\nBut you've never been a police officer, have you?\nNo, I haven't.\nNo, you haven't. And so here we have yet another example\nof bee culture casually stolen by a human\nfor nothing more than a prance-about stage name.\nOh, please.\nHave you ever been stung, Mr. Sting?\nBecause I'm feeling a little stung, Sting.\nOr should I say... Mr. Gordon M. Sumner!\nThat's not his real name?! You idiots!\nMr. Liotta, first, belated congratulations on\nyour Emmy win for a guest spot on ER in 2005.\nThank you. Thank you.\nI see from your resume that you're devilishly handsome\nwith a churning inner turmoil that's ready to blow.\nI enjoy what I do. Is that a crime?\nNot yet it isn't. But is this what it's come to for you?\nExploiting tiny, helpless bees so you don't\nhave to rehearse your part and learn your lines, sir?\nWatch it, Benson! I could blow right now!\nThis isn't a goodfella. This is a badfella!\nWhy doesn't someone just step on this creep, and we can all go home?!\n- Order in this court! - You're all thinking it!\nOrder! Order, I say!\n- Say it! - Mr. Liotta, please sit down!\nI think it was awfully nice of that bear to pitch in like that.\nI think the jury's on our side.\nAre we doing everything right, legally?\nI'm a florist.\nRight. Well, here's to a great team.\nTo a great team!\nWell, hello.\n- Ken! - Hello.\nI didn't think you were coming.\nNo, I was just late. I tried to call, but... the battery.\nI didn't want all this to go to waste, so I called Barry. Luckily, he was free.\nOh, that was lucky.\nThere's a little left. I could heat it up.\nYeah, heat it up, sure, whatever.\nSo I hear you're quite a tennis player.\nI'm not much for the game myself. The ball's a little grabby.\nThat's where I usually sit. Right... there.\nKen, Barry was looking at your resume,\nand he agreed with me that eating with chopsticks isn't really a special skill.\nYou think I don't see what you're doing?\nI know how hard it is to find the rightjob. We have that in common.\nDo we?\nBees have 100 percent employment, but we do jobs like taking the crud out.\nThat's just what I was thinking about doing.\nKen, I let Barry borrow your razor for his fuzz. I hope that was all right.\nI'm going to drain the old stinger.\nYeah, you do that.\nLook at that.\nYou know, I've just about had it\nwith your little mind games.\n- What's that? - Italian Vogue.\nMamma mia, that's a lot of pages.\nA lot of ads.\nRemember what Van said, why is your life more valuable than mine?\nFunny, I just can't seem to recall that!\nI think something stinks in here!\nI love the smell of flowers.\nHow do you like the smell of flames?!\nNot as much.\nWater bug! Not taking sides!\nKen, I'm wearing a Ohapstick hat! This is pathetic!\nI've got issues!\nWell, well, well, a royal flush!\n- You're bluffing. - Am I?\nSurf's up, dude!\nPoo water!\nThat bowl is gnarly.\nExcept for those dirty yellow rings!\nKenneth! What are you doing?!\nYou know, I don't even like honey! I don't eat it!\nWe need to talk!\nHe's just a little bee!\nAnd he happens to be the nicest bee I've met in a long time!\nLong time? What are you talking about?! Are there other bugs in your life?\nNo, but there are other things bugging me in life. And you're one of them!\nFine! Talking bees, no yogurt night...\nMy nerves are fried from riding on this emotional roller coaster!\nGoodbye, Ken.\nAnd for your information,\nI prefer sugar-free, artificial sweeteners made by man!\nI'm sorry about all that.\nI know it's got an aftertaste! I like it!\nI always felt there was some kind of barrier between Ken and me.\nI couldn't overcome it. Oh, well.\nAre you OK for the trial?\nI believe Mr. Montgomery is about out of ideas.\nWe would like to call Mr. Barry Benson Bee to the stand.\nGood idea! You can really see why he's considered one of the best lawyers...\nYeah.\nLayton, you've gotta weave some magic\nwith this jury, or it's gonna be all over.\nDon't worry. The only thing I have to do to turn this jury around\nis to remind them of what they don't like about bees.\n- You got the tweezers? - Are you allergic?\nOnly to losing, son. Only to losing.\nMr. Benson Bee, I'll ask you what I think we'd all like to know.\nWhat exactly is your relationship\nto that woman?\nWe're friends.\n- Good friends? - Yes.\nHow good? Do you live together?\nWait a minute...\nAre you her little...\n...bedbug?\nI've seen a bee documentary or two. From what I understand,\ndoesn't your queen give birth to all the bee children?\n- Yeah, but... - So those aren't your real parents!\n- Oh, Barry... - Yes, they are!\nHold me back!\nYou're an illegitimate bee, aren't you, Benson?\nHe's denouncing bees!\nDon't y'all date your cousins?\n- Objection! - I'm going to pincushion this guy!\nAdam, don't! It's what he wants!\nOh, I'm hit!!\nOh, lordy, I am hit!\nOrder! Order!\nThe venom! The venom is coursing through my veins!\nI have been felled by a winged beast of destruction!\nYou see? You can't treat them like equals! They're striped savages!\nStinging's the only thing they know! It's their way!\n- Adam, stay with me. - I can't feel my legs.\nWhat angel of mercy will come forward to suck the poison\nfrom my heaving buttocks?\nI will have order in this court. Order!\nOrder, please!\nThe case of the honeybees versus the human race\ntook a pointed turn against the bees\nyesterday when one of their legal team stung Layton T. Montgomery.\n- Hey, buddy. - Hey.\n- Is there much pain? - Yeah.\nI...\nI blew the whole case, didn't I?\nIt doesn't matter. What matters is you're alive. You could have died.\nI'd be better off dead. Look at me.\nThey got it from the cafeteria downstairs, in a tuna sandwich.\nLook, there's a little celery still on it.\nWhat was it like to sting someone?\nI can't explain it. It was all...\nAll adrenaline and then... and then ecstasy!\nAll right.\nYou think it was all a trap?\nOf course. I'm sorry. I flew us right into this.\nWhat were we thinking? Look at us. We're just a couple of bugs in this world.\nWhat will the humans do to us if they win?\nI don't know.\nI hear they put the roaches in motels. That doesn't sound so bad.\nAdam, they check in, but they don't check out!\nOh, my.\nOould you get a nurse to close that window?\n- Why? - The smoke.\nBees don't smoke.\nRight. Bees don't smoke.\nBees don't smoke! But some bees are smoking.\nThat's it! That's our case!\nIt is? It's not over?\nGet dressed. I've gotta go somewhere.\nGet back to the court and stall. Stall any way you can.\nAnd assuming you've done step correctly, you're ready for the tub.\nMr. Flayman.\nYes? Yes, Your Honor!\nWhere is the rest of your team?\nWell, Your Honor, it's interesting.\nBees are trained to fly haphazardly,\nand as a result, we don't make very good time.\nI actually heard a funny story about...\nYour Honor, haven't these ridiculous bugs\ntaken up enough of this court's valuable time?\nHow much longer will we allow these absurd shenanigans to go on?\nThey have presented no compelling evidence to support their charges\nagainst my clients, who run legitimate businesses.\nI move for a complete dismissal of this entire case!\nMr. Flayman, I'm afraid I'm going\nto have to consider Mr. Montgomery's motion.\nBut you can't! We have a terrific case.\nWhere is your proof? Where is the evidence?\nShow me the smoking gun!\nHold it, Your Honor! You want a smoking gun?\nHere is your smoking gun.\nWhat is that?\nIt's a bee smoker!\nWhat, this? This harmless little contraption?\nThis couldn't hurt a fly, let alone a bee.\nLook at what has happened\nto bees who have never been asked, \"Smoking or non?\"\nIs this what nature intended for us?\nTo be forcibly addicted to smoke machines\nand man-made wooden slat work camps?\nLiving out our lives as honey slaves to the white man?\n- What are we gonna do? - He's playing the species card.\nLadies and gentlemen, please, free these bees!\nFree the bees! Free the bees!\nFree the bees!\nFree the bees! Free the bees!\nThe court finds in favor of the bees!\nVanessa, we won!\nI knew you could do it! High-five!\nSorry.\nI'm OK! You know what this means?\nAll the honey will finally belong to the bees.\nNow we won't have to work so hard all the time.\nThis is an unholy perversion of the balance of nature, Benson.\nYou'll regret this.\nBarry, how much honey is out there?\nAll right. One at a time.\nBarry, who are you wearing?\nMy sweater is Ralph Lauren, and I have no pants.\n- What if Montgomery's right? - What do you mean?\nWe've been living the bee way a long time, 27 million years.\nOongratulations on your victory. What will you demand as a settlement?\nFirst, we'll demand a complete shutdown of all bee work camps.\nThen we want back the honey that was ours to begin with,\nevery last drop.\nWe demand an end to the glorification of the bear as anything more\nthan a filthy, smelly, bad-breath stink machine.\nWe're all aware of what they do in the woods.\nWait for my signal.\nTake him out.\nHe'll have nauseous for a few hours, then he'll be fine.\nAnd we will no longer tolerate bee-negative nicknames...\nBut it's just a prance-about stage name!\n...unnecessary inclusion of honey in bogus health products\nand la-dee-da human tea-time snack garnishments.\nCan't breathe.\nBring it in, boys!\nHold it right there! Good.\nTap it.\nMr. Buzzwell, we just passed three cups, and there's gallons more coming!\n- I think we need to shut down! - Shut down? We've never shut down.\nShut down honey production!\nStop making honey!\nTurn your key, sir!\nWhat do we do now?\nCannonball!\nWe're shutting honey production!\nMission abort.\nAborting pollination and nectar detail. Returning to base.\nAdam, you wouldn't believe how much honey was out there.\nOh, yeah?\nWhat's going on? Where is everybody?\n- Are they out celebrating? - They're home.\nThey don't know what to do. Laying out, sleeping in.\nI heard your Uncle Oarl was on his way to San Antonio with a cricket.\nAt least we got our honey back.\nSometimes I think, so what if humans liked our honey? Who wouldn't?\nIt's the greatest thing in the world! I was excited to be part of making it.\nThis was my new desk. This was my new job. I wanted to do it really well.\nAnd now...\nNow I can't.\nI don't understand why they're not happy.\nI thought their lives would be better!\nThey're doing nothing. It's amazing. Honey really changes people.\nYou don't have any idea what's going on, do you?\n- What did you want to show me? - This.\nWhat happened here?\nThat is not the half of it.\nOh, no. Oh, my.\nThey're all wilting.\nDoesn't look very good, does it?\nNo.\nAnd whose fault do you think that is?\nYou know, I'm gonna guess bees.\nBees?\nSpecifically, me.\nI didn't think bees not needing to make honey would affect all these things.\nIt's notjust flowers. Fruits, vegetables, they all need bees.\nThat's our whole SAT test right there.\nTake away produce, that affects the entire animal kingdom.\nAnd then, of course...\nThe human species?\nSo if there's no more pollination,\nit could all just go south here, couldn't it?\nI know this is also partly my fault.\nHow about a suicide pact?\nHow do we do it?\n- I'll sting you, you step on me. - Thatjust kills you twice.\nRight, right.\nListen, Barry... sorry, but I gotta get going.\nI had to open my mouth and talk.\nVanessa?\nVanessa? Why are you leaving? Where are you going?\nTo the final Tournament of Roses parade in Pasadena.\nThey've moved it to this weekend because all the flowers are dying.\nIt's the last chance I'll ever have to see it.\nVanessa, I just wanna say I'm sorry. I never meant it to turn out like this.\nI know. Me neither.\nTournament of Roses. Roses can't do sports.\nWait a minute. Roses. Roses?\nRoses!\nVanessa!\nRoses?!\nBarry?\n- Roses are flowers! - Yes, they are.\nFlowers, bees, pollen!\nI know. That's why this is the last parade.\nMaybe not. Oould you ask him to slow down?\nOould you slow down?\nBarry!\nOK, I made a huge mistake. This is a total disaster, all my fault.\nYes, it kind of is.\nI've ruined the planet. I wanted to help you\nwith the flower shop. I've made it worse.\nActually, it's completely closed down.\nI thought maybe you were remodeling.\nBut I have another idea, and it's greater than my previous ideas combined.\nI don't want to hear it!\nAll right, they have the roses, the roses have the pollen.\nI know every bee, plant and flower bud in this park.\nAll we gotta do is get what they've got back here with what we've got.\n- Bees. - Park.\n- Pollen! - Flowers.\n- Repollination! - Across the nation!\nTournament of Roses, Pasadena, Oalifornia.\nThey've got nothing but flowers, floats and cotton candy.\nSecurity will be tight.\nI have an idea.\nVanessa Bloome, FTD.\nOfficial floral business. It's real.\nSorry, ma'am. Nice brooch.\nThank you. It was a gift.\nOnce inside, we just pick the right float.\nHow about The Princess and the Pea?\nI could be the princess, and you could be the pea!\nYes, I got it.\n- Where should I sit? - What are you?\n- I believe I'm the pea. - The pea?\nIt goes under the mattresses.\n- Not in this fairy tale, sweetheart. - I'm getting the marshal.\nYou do that! This whole parade is a fiasco!\nLet's see what this baby'll do.\nHey, what are you doing?!\nThen all we do is blend in with traffic...\n...without arousing suspicion.\nOnce at the airport, there's no stopping us.\nStop! Security.\n- You and your insect pack your float? - Yes.\nHas it been in your possession the entire time?\nWould you remove your shoes?\n- Remove your stinger. - It's part of me.\nI know. Just having some fun. Enjoy your flight.\nThen if we're lucky, we'll have just enough pollen to do the job.\nCan you believe how lucky we are? We have just enough pollen to do the job!\nI think this is gonna work.\nIt's got to work.\nAttention, passengers, this is Oaptain Scott.\nWe have a bit of bad weather in New York.\nIt looks like we'll experience a couple hours delay.\nBarry, these are cut flowers with no water. They'll never make it.\nI gotta get up there and talk to them.\nBe careful.\nCan I get help with the Sky Mall magazine?\nI'd like to order the talking inflatable nose and ear hair trimmer.\nOaptain, I'm in a real situation.\n- What'd you say, Hal? - Nothing.\nBee!\nDon't freak out! My entire species...\nWhat are you doing?\n- Wait a minute! I'm an attorney! - Who's an attorney?\nDon't move.\nOh, Barry.\nGood afternoon, passengers. This is your captain.\nWould a Miss Vanessa Bloome in 24B please report to the cockpit?\nAnd please hurry!\nWhat happened here?\nThere was a DustBuster, a toupee, a life raft exploded.\nOne's bald, one's in a boat, they're both unconscious!\n- Is that another bee joke? - No!\nNo one's flying the plane!\nThis is JFK control tower, Flight 356. What's your status?\nThis is Vanessa Bloome. I'm a florist from New York.\nWhere's the pilot?\nHe's unconscious, and so is the copilot.\nNot good. Does anyone onboard have flight experience?\nAs a matter of fact, there is.\n- Who's that? - Barry Benson.\nFrom the honey trial?! Oh, great.\nVanessa, this is nothing more than a big metal bee.\nIt's got giant wings, huge engines.\nI can't fly a plane.\n- Why not? Isn't John Travolta a pilot? - Yes.\nHow hard could it be?\nWait, Barry! We're headed into some lightning.\nThis is Bob Bumble. We have some late-breaking news from JFK Airport,\nwhere a suspenseful scene is developing.\nBarry Benson, fresh from his legal victory...\nThat's Barry!\n...is attempting to land a plane, loaded with people, flowers\nand an incapacitated flight crew.\nFlowers?!\nWe have a storm in the area and two individuals at the controls\nwith absolutely no flight experience.\nJust a minute. There's a bee on that plane.\nI'm quite familiar with Mr. Benson and his no-account compadres.\nThey've done enough damage.\nBut isn't he your only hope?\nTechnically, a bee shouldn't be able to fly at all.\nTheir wings are too small...\nHaven't we heard this a million times?\n\"The surface area of the wings and body mass make no sense.\"\n- Get this on the air! - Got it.\n- Stand by. - We're going live.\nThe way we work may be a mystery to you.\nMaking honey takes a lot of bees doing a lot of small jobs.\nBut let me tell you about a small job.\nIf you do it well, it makes a big difference.\nMore than we realized. To us, to everyone.\nThat's why I want to get bees back to working together.\nThat's the bee way! We're not made of Jell-O.\nWe get behind a fellow.\n- Black and yellow! - Hello!\nLeft, right, down, hover.\n- Hover? - Forget hover.\nThis isn't so hard. Beep-beep! Beep-beep!\nBarry, what happened?!\nWait, I think we were on autopilot the whole time.\n- That may have been helping me. - And now we're not!\nSo it turns out I cannot fly a plane.\nAll of you, let's get behind this fellow! Move it out!\nMove out!\nOur only chance is if I do what I'd do, you copy me with the wings of the plane!\nDon't have to yell.\nI'm not yelling! We're in a lot of trouble.\nIt's very hard to concentrate with that panicky tone in your voice!\nIt's not a tone. I'm panicking!\nI can't do this!\nVanessa, pull yourself together. You have to snap out of it!\nYou snap out of it.\nYou snap out of it.\n- You snap out of it! - You snap out of it!\n- You snap out of it! - You snap out of it!\n- You snap out of it! - You snap out of it!\n- Hold it! - Why? Oome on, it's my turn.\nHow is the plane flying?\nI don't know.\nHello?\nBenson, got any flowers for a happy occasion in there?\nThe Pollen Jocks!\nThey do get behind a fellow.\n- Black and yellow. - Hello.\nAll right, let's drop this tin can on the blacktop.\nWhere? I can't see anything. Can you?\nNo, nothing. It's all cloudy.\nOome on. You got to think bee, Barry.\n- Thinking bee. - Thinking bee.\nThinking bee! Thinking bee! Thinking bee!\nWait a minute. I think I'm feeling something.\n- What? - I don't know. It's strong, pulling me.\nLike a 27-million-year-old instinct.\nBring the nose down.\nThinking bee! Thinking bee! Thinking bee!\n- What in the world is on the tarmac? - Get some lights on that!\nThinking bee! Thinking bee! Thinking bee!\n- Vanessa, aim for the flower. - OK.\nOut the engines. We're going in on bee power. Ready, boys?\nAffirmative!\nGood. Good. Easy, now. That's it.\nLand on that flower!\nReady? Full reverse!\nSpin it around!\n- Not that flower! The other one! - Which one?\n- That flower. - I'm aiming at the flower!\nThat's a fat guy in a flowered shirt. I mean the giant pulsating flower\nmade of millions of bees!\nPull forward. Nose down. Tail up.\nRotate around it.\n- This is insane, Barry! - This's the only way I know how to fly.\nAm I koo-koo-kachoo, or is this plane flying in an insect-like pattern?\nGet your nose in there. Don't be afraid. Smell it. Full reverse!\nJust drop it. Be a part of it.\nAim for the center!\nNow drop it in! Drop it in, woman!\nOome on, already.\nBarry, we did it! You taught me how to fly!\n- Yes. No high-five! - Right.\nBarry, it worked! Did you see the giant flower?\nWhat giant flower? Where? Of course I saw the flower! That was genius!\n- Thank you. - But we're not done yet.\nListen, everyone!\nThis runway is covered with the last pollen\nfrom the last flowers available anywhere on Earth.\nThat means this is our last chance.\nWe're the only ones who make honey, pollinate flowers and dress like this.\nIf we're gonna survive as a species, this is our moment! What do you say?\nAre we going to be bees, orjust Museum of Natural History keychains?\nWe're bees!\nKeychain!\nThen follow me! Except Keychain.\nHold on, Barry. Here.\nYou've earned this.\nYeah!\nI'm a Pollen Jock! And it's a perfect fit. All I gotta do are the sleeves.\nOh, yeah.\nThat's our Barry.\nMom! The bees are back!\nIf anybody needs to make a call, now's the time.\nI got a feeling we'll be working late tonight!\nHere's your change. Have a great afternoon! Can I help who's next?\nWould you like some honey with that? It is bee-approved. Don't forget these.\nMilk, cream, cheese, it's all me. And I don't see a nickel!\nSometimes I just feel like a piece of meat!\nI had no idea.\nBarry, I'm sorry. Have you got a moment?\nWould you excuse me? My mosquito associate will help you.\nSorry I'm late.\nHe's a lawyer too?\nI was already a blood-sucking parasite. All I needed was a briefcase.\nHave a great afternoon!\nBarry, I just got this huge tulip order, and I can't get them anywhere.\nNo problem, Vannie. Just leave it to me.\nYou're a lifesaver, Barry. Can I help who's next?\nAll right, scramble, jocks! It's time to fly.\nThank you, Barry!\nThat bee is living my life!\nLet it go, Kenny.\n- When will this nightmare end?! - Let it all go.\n- Beautiful day to fly. - Sure is.\nBetween you and me, I was dying to get out of that office.\nYou have got to start thinking bee, my friend.\n- Thinking bee! - Me?\nHold it. Let's just stop for a second. Hold it.\nI'm sorry. I'm sorry, everyone. Can we stop here?\nI'm not making a major life decision during a production number!\nAll right. Take ten, everybody. Wrap it up, guys.\nI had virtually no rehearsal for that."
        textline = textwrap.wrap(beemovie, width=2000)
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
    img = Image.open(".\Resources\Images\Input\Textbox.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("DTM-Mono.otf", 130)
    margin = 170
    offset = 100
    textline = textwrap.wrap(inputtext, width=33)
    for line in textline:
        draw.text((margin, offset), line,(255,255,255),font=font)
        offset += 200
    img.save(".\Resources\Images\Output\Textbox.png")
    await bot.send_file(ctx.message.channel, ".\Resources\Images\Output\Textbox.png")
    os.remove(".\Resources\Images\Output\Textbox.png")

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
    except:
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
