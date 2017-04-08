#! /usr/bin/python3.5
"""kiwi catnip's bad code"""
import os
import platform
import shutil
import stat
import sys
import time
from distutils.dir_util import copy_tree

print("Embedbot updater - for if the update command doesn't work.")

CURRENT_OS = platform.system()
try:
    from git import Repo
except ImportError:
    if CURRENT_OS == "Linux" or CURRENT_OS == "Darwin": # Linux / OSX Fix
        PIP_OS = "pip3"
    if CURRENT_OS == "Windows":
        PIP_OS = "pip"
    print("Please run \"{} install gitpython\".".format(PIP_OS))
    sys.exit()
print("Updating embedbot.")
try:
    os.remove("oldconfig.json")
    os.rename("config.json", "oldconfig.json")
    os.remove("embedbot.py") #lol r i p embedbot if this doesn't work r i p my work
    os.remove("README.md")
    os.remove("requirements.txt")
except OSError:
    pass
REPO_URL = "https://www.github.com/Luigimaster1/embedbot.git"
LOCAL_DIR = "./tempupdate/"
Repo.clone_from(REPO_URL, LOCAL_DIR)
def del_rw(action, name, exc):
    """kiwi catnip pls document this"""
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)
shutil.rmtree("./tempupdate/.git/", onerror=del_rw)
copy_tree(LOCAL_DIR, ".")
shutil.rmtree("./tempupdate/", onerror=del_rw)
os.remove("botinfo.json")
print("Updated!")
X = "Your config file has been renamed to oldconfig.json, "
Y = "because the config might have been changed in the new version."
print(X+Y)
print("You can update your oldconfig.json file, and rename oldconfig.json back to config.json.")
X = "If you use a custom config like in the examples, "
Y = "nothing will be replaced, but you will still have the oldconfig.json."
print(X+Y)
print("You can ignore that, and delete it.")
X = ", horribly coded by -Kiwi Catnip \\u2661#1540.\nProbably no rights reserved."
print("\n\n\n\nEmbedbot updater version 1.0"+X)
del X, Y
time.sleep(5)
