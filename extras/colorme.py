# Colorme made by -Kiwi Catnip ♡#1540, built off Embedbot made by -Kiwi Catnip ♡#1540, @isy#0669, @HYP3RD34TH#2104 and @Nikitaw99#4332.
print("Warning! Colorme doesn't have anything like module checks, like embedbot.")
print("Embedbot is MUCH easier to use than this.")
print("If you don't understand how to use this, you probably shouldn't.")
print("You have been warned.")
from discord.ext import commands
import discord
import subprocess as sp
import asyncio
import os
import sys
import json
import time
import threading
import random
from colorama import Fore, Back, Style
import colorama
import platform
import itertools
colorama.init(autoreset=True)
current_os = platform.system()
try:
    with open("config.json") as c:
        jsonhandler = json.load(c)
        token = jsonhandler['token'] # token
        email = jsonhandler['email'] # email
        password = jsonhandler['password'] # password
        invoker = jsonhandler['invoker'] # invoker, * by default
        rolename = jsonhandler['rolename'] # name of the role
        cserver = jsonhandler['cserver'] # server
except json.JSONDecodeError:
    x = "There was a problem with your config file. Make sure that everything is up to date."
    y = "\nIf it still doesn't work, try deleting the config file and creating it again. "
    z = "Don't use notepad for editing, use notepad++!"
    print(x+y+z)
    del x, y, z

load = itertools.cycle(['.  ', '.. ', '...', '   '])
sys.stdout.write('Logging in to Discord')

def loggingin():
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        for i in range(0, 4):
            sys.stdout.write(load.__next__())
            sys.stdout.flush()
            sys.stdout.write('\b\b\b')
            time.sleep(0.5)
            if not getattr(t, "do_run", True):
                break
thread = threading.Thread(target=loggingin)
thread.start()

bot = commands.Bot(command_prefix=invoker, self_bot=True)
# Bot Loading
colorlist = [
"discord.Colour.default()",
"discord.Colour.teal()",
"discord.Colour.dark_teal()",
"discord.Colour.green()",
"discord.Colour.dark_green()",
"discord.Colour.blue()",
"discord.Colour.dark_blue()",
"discord.Colour.purple()",
"discord.Colour.dark_purple()",
"discord.Colour.magenta()",
"discord.Colour.dark_magenta()",
"discord.Colour.gold()",
"discord.Colour.dark_gold()",
"discord.Colour.orange()",
"discord.Colour.dark_orange()",
"discord.Colour.red()",
"discord.Colour.dark_red()",
"discord.Colour.lighter_grey()",
"discord.Colour.dark_grey()",
"discord.Colour.light_grey()",
"discord.Colour.darker_grey()"
]
async def colorloop():
    await bot.wait_until_ready()
    colorserver = discord.utils.get(bot.servers, id=cserver)
    colorrole = discord.utils.get(colorserver.roles, name=rolename)
    while not bot.is_closed:
        randcolor = random.choice(colorlist)
        await bot.edit_role(colorserver, colorrole, color=eval(randcolor))
        await asyncio.sleep(30)

@bot.event
async def on_ready():
    thread.do_run = False
    thread.join()
    print("\nStarted " + Fore.LIGHTCYAN_EX + "colorme.")
    print('Logged in as')
    print(bot.user.name.encode("ascii", "backslashreplace").decode())
    print(bot.user.id)
    print('------')
    bot.remove_command("help")
    bot.remove_command("HelpFormatter")

@bot.event
async def on_message(message):
    # Do something? idk
    pass

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
async def test(ctx):
    await bot.edit_message(ctx.message, "`The selfbot is active.`")

    
@bot.command(pass_context=True)
async def kill(ctx):
    await bot.edit_message(ctx.message, "`Killed.`")
    await asyncio.sleep(1)
    await bot.logout()

try:
    if token == "None": # For People that use Email and Password.
                        # "None" because json doesn't have None.
    
        if "@" not in email or email == "None": # Checks email.
            thread.do_run = False
            thread.join()
            print("Invalid email or none provided.")
            print("Please check your credentials.")
        bot.loop.create_task(colorloop())
        bot.run(email, password, bot=False)
    else:
        if len(token) < 50: # Checking Token's Length.
            thread.do_run = False
            thread.join()
            print("Token is to short.")
            print("Try using your email and password instead.\n")
            if "@" not in email: # Checks email.
                print("Invalid email or none provided.")
                print("Please check your credentials.")
                sys.exit()
            else:
                bot.loop.create_task(colorloop())
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
                bot.loop.create_task(colorloop())
                bot.run(email, password, bot=False)
        else:
            bot.loop.create_task(colorloop())
            bot.run(token, bot=False)
except:
    print("There was a problem logging in.")
    print("Check your internet connection.")
    print("If you haven't already, please add your credentials in config.json,")
    print("and make sure they're correct.")
    time.sleep(5)
    sys.exit()