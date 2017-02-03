print("Embedbot updater - for if the update command doesn't work.")
import platform
import sys
import time
current_os = platform.system()
try:
    from git import Repo
except ImportError:
    if current_os == "Linux" or current_os == "Darwin": # Linux / OSX Fix
        pip_os = "pip3"
    if current_os == "Windows":
        pip_os = "pip"
    print("Please run \"{} install gitpython\".".format(pip_os))
    sys.exit()
import shutil
from distutils.dir_util import copy_tree
import os
import stat
print("Updating embedbot.")
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
print("Updated!")
print("Your config file has been renamed to oldconfig.json, because the config might have been changed in the new version.")
print("You can update your oldconfig.json file, and rename oldconfig.json back to config.json.")
print("If you use a custom config like in the examples, nothing will be replaced, but you will still have the oldconfig.json.")
print("You can ignore that, and delete it.")
print("\n\n\n\nEmbedbot updater version 1.0, horribly coded by -Kiwi Catnip \\u2661#1540.\nProbably no rights reserved.")
time.sleep(5)