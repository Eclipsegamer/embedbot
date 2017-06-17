#! /usr/bin/python3.5
import pip
import time
print("Installing discord.py...")
pip.main(['install', "git+https://github.com/Rapptz/discord.py@rewrite"])
print("Installing colorama...")
pip.main(['install', "colorama"])
print("Installing pillow...")
pip.main(['install', "pillow"])
print("Installing cursor...")
pip.main(['install', "cursor"])
print("Installing psutil...")
pip.main(['install', "psutil"])
print("Installing brainfuck...")
pip.main(['install', "brainfuck"])
print("Done.")
time.sleep(5)
