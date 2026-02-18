import socket
import json
import pyautogui

IP = "0.0.0.0"
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print(f"UDP server listening on {IP}:{PORT}")

size = pyautogui.size()
def mouse(x, y):
	pyautogui.moveTo(size[0]*x, size[1]*y)
	print('mouse: ', x, y)

def click(button, updown):
	if updown:
		pyautogui.mouseDown(button=button)
	else:
		pyautogui.mouseUp(button=button)
	print('click: ', button)

def scroll(hscroll, vscroll):
	pyautogui.hscroll(hscroll*100)
	pyautogui.scroll(vscroll*100)
	print('hscroll: ', scroll, vscroll)

def press(key, updown):
	print('press: ', key, updown)


while True:
	data, addr = sock.recvfrom(1024)
	try:
		msg = json.loads(data.decode())
		action = msg.get("action")
		payload = msg.get("data")
		if action=="mouse":
			mouse(*payload)
		elif action=="click":
			click(*payload)
		elif action=="scroll":
			scroll(*payload)
		elif action=="press":
			press(*payload)
		elif action=="stop":
			break
		else:
			print(f"[{addr}] {action}: {payload}")
	except Exception as e:
		print(f"Bad packet from {addr}: {data} | {e}")
