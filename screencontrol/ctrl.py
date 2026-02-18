from pynput import mouse, keyboard
import requests
import pyautogui
from os import system as sys

paused=True ######################################## shud b false
SERVER_URL = "http://localhost:5000/"
size = pyautogui.size()

def on_move(x, y):
	global paused
	try:
		data = (x/size()[0], y/size()[1])
		if not paused:
			response = requests.post(SERVER_URL+"mouse", json=data, timeout=0.001)
			# print(f"Sent move: {data} | Status: {response.status_code}")
	except Exception as e:
		# print(type(e), ": ", e)
		print(pyautogui.position()[0]/size[0], pyautogui.position()[1]/size[1])

def on_click(x, y, button, pressed):
	global paused
	try:
		data = (x/size()[0], y/size()[1])
		if not paused:
			response = requests.post(SERVER_URL+"click", json=data, timeout=0.001)
			# print(f"Sent move: {data} | Status: {response.status_code}")
	except Exception as e:
		# print(type(e), ": ", e)
		print(str(button)[7:],pressed)

def on_scroll(x, y, dx, dy):
	global paused
	if not paused:
		print(f"Scrolled {'down' if dy < 0 else 'up'} at {(dx, dy)}")

def on_press(key):
	global paused
	if key == keyboard.Key.scroll_lock:
		paused = not paused
		print(f"Set paused to {paused}")
	elif key == keyboard.Key.esc and paused:
		print("🛑 Esc pressed — stopping listener...")
		mouse_listener.stop()
		return False  # stop keyboard listener too
	# else:
	# 	print(key)


def on_release(key):
	print("release", key)


mouse_listener = mouse.Listener(
	on_move=on_move,
	on_click=on_click,
	on_scroll=on_scroll)
mouse_listener.start()

# Start keyboard listener (waits until Esc is pressed)
with keyboard.Listener(on_press=on_press, on_release=on_release) as kb_listener:
	kb_listener.join()