from pynput import mouse, keyboard
import socket, json, pyautogui

paused = False
SERVER_IP = "192.168.1.5"  # change to your server’s LAN IP
SERVER_PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
size = pyautogui.size()

def on_move(x, y):
	global paused
	if not paused:
		data = {"action": "mouse", "data": (x/size[0], y/size[1])}
		sock.sendto(json.dumps(data).encode(), (SERVER_IP, SERVER_PORT))
		print("sent ", data)

def on_click(x, y, button, pressed):
	global paused
	if not paused:
		data = {"action": "click", "data": (str(button)[7:], pressed)}
		sock.sendto(json.dumps(data).encode(), (SERVER_IP, SERVER_PORT))
		print("sent ", data)

def on_scroll(x, y, dx, dy):
	global paused
	if not paused:
		data = {"action": "scroll", "data": (dx, dy)}
		sock.sendto(json.dumps(data).encode(), (SERVER_IP, SERVER_PORT))
		print("sent ", data)

def on_press(key):
	global paused
	if key == keyboard.Key.scroll_lock:
		paused = not paused
		print(f"Set paused to {paused}")
	elif key == keyboard.Key.esc and paused:
		print("🛑 Esc pressed — stopping listener...")
		mouse_listener.stop()
		data = {"action": "stop", "data": None}
		sock.sendto(json.dumps(data).encode(), (SERVER_IP, SERVER_PORT))
		return False
	else:
		if not paused:
			data = {"action": "press", "data": (str(key), True)}
			sock.sendto(json.dumps(data).encode(), (SERVER_IP, SERVER_PORT))
			print("sent ", data)

def on_release(key):
	global paused
	if not paused:
		data = {"action": "press", "data": (str(key), False)}
		sock.sendto(json.dumps(data).encode(), (SERVER_IP, SERVER_PORT))
		print("sent ", data)

mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
mouse_listener.start()

with keyboard.Listener(on_press=on_press, on_release=on_release) as kb_listener:
	kb_listener.join()
