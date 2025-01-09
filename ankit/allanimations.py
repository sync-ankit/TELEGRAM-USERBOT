import asyncio
from telethon import events 
import time
import random
import ankit.client
client = ankit.client.client

M = ("___________ \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　／￣￣＼| \n"
"＜ ´･ 　　 |＼ \n"
"　|　３　 | 丶＼ \n"
"＜ 、･　　|　　＼ \n"
"　＼＿＿／∪ _ ∪) \n"
"　　　　　 Ｕ Ｕ\n")
    
C = ("_/﹋\_\n"
"(҂`_´)\n"
"<,︻╦╤─ ҉ - - - 🤯\n"
"_/﹋\_\n")

A = ("▄███████▄\n"
"█▄█████▄█\n"
"█▼▼▼▼▼█\n"
"██________█▌\n"
"█▲▲▲▲▲█\n"
"█████████\n"
"_████\n\n")

B = ("┈┈┏━╮╭━┓┈╭━━━━╮\n"
"┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
"┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
"┈╭━┻╮╲┗━━━━╮╭╮┈\n"
"┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
"┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
"┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
"┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")

D = ("░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄\n"
"░███████████████████████ \n"
"░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ \n"
"░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░\n"
"░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░\n"
"░░█▓▓▓▓▓▌░░░░░░░░░░\n"
"░▐█▓▓▓▓▓░░░░░░░░░░░\n"
"░▐██████▌░░░░░░░░░░\n")

E = ("╥━━━━━━━━╭━━╮━━┳\n"
"╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
"╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
"╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
"╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
"╨━━┗┛┗┛━━┗┛┗┛━━┻\n")
F = ("╔┓┏╦━╦┓╔┓╔━━╗\n" 
"║┗┛║┗╣┃║┃║X X║\n"
"║┏┓║┏╣┗╣┗╣╰╯║\n"
"╚┛┗╩━╩━╩━╩━━╝\n\n")
G = ("▬▬▬.◙.▬▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, My Friend :D \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")

H = ("┳┻┳┻╭━━━━╮╱▔▔▔╲\n"
"┻┳┻┳┃╯╯╭━┫▏╰╰╰▕\n"
"┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮\n"
"┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯\n"
"┳┻┳┻┏╯╯┃╭━╯┳━┳╯\n"
"┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲\n"
"┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕\n"
"┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱\n"
"┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯\n"
"┻┳┻┳┻┏╯▔'''╰┓┣━┳┫\n"
"┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃\n"
"┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃\n"
"┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃\n"
"┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃.\n"
"┳┻┳┻┳┻┣╋┫'''┊┣━╋┫\n"
"┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮\n"
"**I Love You 💕** \n\n")

I = ("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⣠⣾⣿⡿⠋⠀⠀⠉⠻⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠃⠀⠀⣀⡀⠀⢹⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡄⠀⠙⠻⠋⠀⠀⣸⣿⣿⠀⠀⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⣿⠟⠀⢠⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠛⠛⠒⠶⠾⢿⣿⣿⣷⣄⣾⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡀⠀⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⠀⠀⠀⠉⠉⠛⠛⠛⠶⢶⣤⣼⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠁⠀⣾⣿⣷⡄⠀⢼⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⡿⠀⠈⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣇⠀⠀⠉⠋⠁⠀⢠⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠿⢷⣤⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠉⠉⠛⢻⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⠻⣀⣀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠁⠀⣀⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣷⡀⠘⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡄⠈⢻⡇⠀⡿⠃⠀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣷⣄⢸⡇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠉⠉⠑⠒⠲⠿⢿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢺⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠉⠉⠙⠋⠀⠀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣤⣤⣀⣀⡀⠀⠀⣰⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢀⣤⡄⠀⡀⠀⢹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣿⡄⠈⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡆⠀⢹⡇⠀⠟⠁⢀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣦⣸⡇⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\n")

K = ("───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
"───█▒▒░░░░░░░░░▒▒█───\n"
"────█░░█░░░░░█░░█────\n"
"─▄▄──█░░░▀█▀░░░█──▄▄─\n"
"█░░█─▀▄░░░░░░░▄▀─█░░█\n"
"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
"█░░║║║╠─║─║─║║║║║╠─░░█\n"
"█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
"█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n\n")

L = ("░░░░▓\n"
"░░░▓▓\n"
"░░█▓▓█\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓███\n"
"░░░░██▓▓████\n"
"░░░░░██▓▓█████\n"
"░░░░░░██▓▓██████\n"
"░░░░░░███▓▓███████\n"
"░░░░░████▓▓████████\n"
"░░░░█████▓▓█████████\n"
"░░░█████░░░█████●███\n"
"░░████░░░░░░░███████\n"
"░░███░░░░░░░░░██████\n"
"░░██░          ░████\n"
"░░░░░░░░░░░░░░░░███\n"
"░░░░░░░░░░░░░░░░░░░\n\n")


N = ("────██──────▀▀▀██\n"
"──▄▀█▄▄▄─────▄▀█▄▄▄\n"
"▄▀──█▄▄──────█─█▄▄\n"
"─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
"─▀───────▀▀─▀───────▀▀\n🚶🏻‍♂️🚶🏻‍♂️ɮʏɛ ʄʀɨɛռɖֆ..")

O = ("╭━━━┳╮╱╱╭╮╱╭━━━┳━━━╮\n"
"┃╭━╮┃┃╱╭╯╰╮┃╭━╮┃╭━╮┃\n"
"┃╰━━┫╰━╋╮╭╯┃┃╱┃┃╰━━╮\n"
"╰━━╮┃╭╮┣┫┃╱┃┃╱┃┣━━╮┃\n"
"┃╰━╯┃┃┃┃┃╰╮┃╰━╯┃╰━╯┃\n"
"╰━━━┻╯╰┻┻━╯╰━━━┻━━━╯\n\n")


P = ("███████▄▄███████████▄\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓███░░░░░░░░░░░░█\n"
"██████▀░░█░░░░██████▀\n"
"░░░░░░░░░█░░░░█\n"
"░░░░░░░░░░█░░░█\n"
"░░░░░░░░░░░█░░█\n"
"░░░░░░░░░░░█░░█\n"
"░░░░░░░░░░░░▀▀\n\n")


@events.register(events.NewMessage(pattern=r".monster"))
async def animmonster(monster):
    await monster.edit(A)

@events.register(events.NewMessage(pattern=r".pig"))
async def animpig(pig):
    await pig.edit(B)

@events.register(events.NewMessage(pattern=r".killer"))
async def animkiller(killer):
    await killer.edit(C)

@events.register(events.NewMessage(pattern=r".gun"))
async def animgun(gun):
    await gun.edit(D)

@events.register(events.NewMessage(pattern=r".dog"))
async def animdog(dog):
    await dog.edit(E)    

@events.register(events.NewMessage(pattern=r".hello"))
async def animhello(hello):
    await hello.edit(F)

@events.register(events.NewMessage(pattern=r".hmf"))
async def animhmf(hmf):
    await hmf.edit(G)

@events.register(events.NewMessage(pattern=r".couple"))
async def couple(e):
    await e.edit(H)

@events.register(events.NewMessage(pattern=r".sup$"))
async def superme(e):
    await e.edit(I)

@events.register(events.NewMessage(pattern=r".welc"))
async def welcome(e):
    await e.edit(K)

@events.register(events.NewMessage(pattern=r".asnake"))
async def snake(e):
    await e.edit(L) 

@events.register(events.NewMessage(pattern=r".cat"))
async def cat(e):
    await e.edit(M)

@events.register(events.NewMessage(pattern=r".bye"))
async def bye(e):
    await e.edit(N)

@events.register(events.NewMessage(pattern=r".shitos"))
async def shitos(e):
    await e.edit(O)

@events.register(events.NewMessage(pattern=r".dislike"))
async def dislike(e):
    await e.edit(P)

@events.register(events.NewMessage(pattern=f".hypno$"))
async def snku(ult):
    ult = await ult.edit("`>>>`")
    animation_interval = 0.3
    animation_ttl = range(0, 15)
    await ult.edit("hypo....")
    animation_chars = [
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬛⬜⬛⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛",
        "⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬛\n⬛⬜⬛⬜⬛\n⬛⬜⬜⬜⬛\n⬛⬛⬛⬛⬛",
        "⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜",
        "[👉🔴👈])",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 15])
@events.register(events.NewMessage(pattern=f".squ$"))
async def squ(ult):
    ult = await ult.edit("╔═══════════════════╗ \n  \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n \t░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ \t░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░\n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░\n╚═══════════════════╝")
    await asyncio.sleep(6)


@events.register(events.NewMessage(pattern=".kiler( (.*)|$)"))
async def kiler(ult):
    name = ult.pattern_match.group(1)
    if not name:
        name = "die"
    animation_interval = 0.7
    animation_ttl = range(9)
    DEFAULTUSER = name
    ult = await ult.edit(f"**Ready Commando ** {DEFAULTUSER}....")
    animation_chars = [
        "Ｆｉｉｉｉｉｒｅ",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉  - \n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉     - \n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n<,︻╦╤─ ҉        - \n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉   - \n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉      - \n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n<,︻╦╤─ ҉        - \n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉        {name}\n _/﹋\_\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 9])

@events.register(events.NewMessage(pattern=r".train$"))
async def train(ult):
    animation_interval = 0.2
    animation_ttl = range(0, 30)
    ult = await ult.edit("train...")
    animation_chars = [
        "**r**",
        "**ra**",
        "**rap**",
        "**rape**",
        "**rape_**",
        "**rape_t**",
        "**rape_tr**",
        "**rape_tra**",
        "**rape_trai**",
        "**rape_train**",
        "**ape_train🚅**",
        "**pe_train🚅🚃🚃**",
        "**e_train🚅🚃🚃🚃**",
        "**_train🚅🚃🚃🚃🚃**",
        "**train🚅🚃🚃🚃🚃🚃**",
        "**rain🚅🚃🚃🚃🚃🚃🚃**",
        "**ain🚅🚃🚃🚃🚃🚃🚃🚃**",
        "**in🚅🚃🚃🚃🚃🚃🚃🚃🚃**",
        "**n🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
        "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃",
        "🚃🚃🚃",
        "🚃🚃",
        "🚃",
        "**Train**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 30])


@events.register(events.NewMessage(pattern=f".rocket$"))
async def alien(ult):
    animation_interval = 1
    animation_ttl = range(0, 24)
    ult = await ult.edit("Connecting..")
    animation_chars = [
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n🚀⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛🚀⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🚀⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚀⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚀⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛🚀\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "🛸⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n🛸⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛🛸⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🛸⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🛸⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛",
        "⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛🚶‍♂️\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n👽⬛⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛👽⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛👽🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
        "__Signal Lost....__",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 24])




@events.register(events.NewMessage(pattern=".hart( (.*)|$)"))
async def hert(event):
    animation_interval = 0.3
    animation_ttl = range(0, 400)
    animation_chars = ["🖤", "❤️", "🖤", "❤️",]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@events.register(events.NewMessage(pattern=".raped( (.*)|$)"))
async def raped(ult):
    ult = await ult.edit("...")
    animation_interval = 1
    animation_ttl = range(0, 11)
    animation_chars = [
        "😁",
        "😧",
        "😡",
        "😢",
        "😁",
        "😧",
        "😡",
        "😢",
        "__Good to See you Guys....__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 11])


@events.register(events.NewMessage(pattern=".fnl( (.*)|$)"))
async def fnl(ult):
    ult = await ult.edit("...")
    animation_interval = 2
    animation_ttl = range(0, 6)
    animation_chars = ["😁🏿", "😁🏾", "😁🏽", "😁🏼", "‎😁", "Good to See you Guys...."]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 6])


@events.register(events.NewMessage(pattern=".monkey( (.*)|$)"))
async def monkey(ult):
    ult = await ult.edit("...")
    animation_interval = 2
    animation_ttl = range(0, 6)
    animation_chars = ["🐵", "🙉", "🙈", "🙊", "💥🐵💥", "Good to See you Guys...."]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 6])

@events.register(events.NewMessage(pattern=".hands( (.*)|$)"))
async def hands(ult):
    ult = await ult.edit("...")
    animation_interval = 1
    animation_ttl = range(0, 14)
    animation_chars = [
        "👈",
        "👉",
        "☝️",
        "👆",
        "👇",
        "✌️",
        "🤞",
        "🖖",
        "🤘",
        "🤙",
        "🖐️",
        "👌",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 14])


@events.register(events.NewMessage(pattern=".count( (.*)|$)"))
async def count(ult):
    ult = await ult.edit("...")
    animation_interval = 1
    animation_ttl = range(0, 13)
    animation_chars = [
        "🔟",
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 13])

@events.register(events.NewMessage(pattern=".kf"))
async def bigf(event):
    anim = [
"""
╭━━━╮
┃╭━━╯
┃╰━━╮
┃╭━━╯
┃┃
╰╯
""","""
🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕
🌕🌕
🌕🌕
🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕
🌕🌕
🌕🌕
🌕🌕
🌕🌕
""", """
🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿
🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿
🇺🇿🇺🇿
🇺🇿🇺🇿
🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿
🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿
🇺🇿🇺🇿
🇺🇿🇺🇿
🇺🇿🇺🇿
🇺🇿🇺🇿
""", """
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️
❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️
❤️❤️
❤️❤️
❤️❤️
"""]
    an = random.choice(anim)
    return await event.edit(an)

@events.register(events.NewMessage(pattern=".f (.*)"))
async def payf(e):
    paytext = e.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 5,
        paytext * 5,
        paytext * 1,
        paytext * 1,
        paytext * 4,
        paytext * 4,
        paytext * 1,
        paytext * 1,
        paytext * 1,
    )
    await e.edit(pay)


@events.register(events.NewMessage(pattern=".bigoof"))
async def bigof(event):
    await event.edit(".")
    time.sleep(0.3)
    await event.edit("..")
    time.sleep(0.3)
    await event.edit("...")
    animation_interval = 0.1
    animation_ttl = range(0, 7)
    await event.edit(
        "┏━━━┓╋╋╋╋┏━━━┓ \n┃┏━┓┃╋╋╋╋┃┏━┓┃ \n┃┃╋┃┣┓┏┓┏┫┃╋┃┃ \n┃┃╋┃┃┗┛┗┛┃┃╋┃┃ \n┃┗━┛┣┓┏┓┏┫┗━┛┃ \n┗━━━┛┗┛┗┛┗━━━┛"
    )
    animation_chars = [
        "╭━━━╮╱╱╱╭━╮ \n┃╭━╮┃╱╱╱┃╭╯ \n┃┃╱┃┣━━┳╯╰╮ \n┃┃╱┃┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃┃┃ \n╰━━━┻━━╯╰╯ ",
        "╭━━━╮╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃┃┃ \n ╰━━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 7])


@events.register(events.NewMessage(pattern=".flower"))
async def flower(event):
    await event.edit(".")
    time.sleep(0.3)
    await event.edit("..")
    time.sleep(0.3)
    await event.edit("...")
    time.sleep(0.3)
    await event.edit("ㅤ\n         ▒▒▒▒▒▒▒▒▒\n      ▒▒▒▒▒▒▒▒▒▒▒▒\n  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒\n▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒\n▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒\n▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒\n  ▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒\n    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n       ▒▒▒▒▒▒▒▒▒▒▒▒▒\n         ▒▒▒▒▒▒▒▒▒▒\n              ▒▒▒▒▒▒\n                     ▓\n     ▓▓▓       ▓\n ▓▓▓▓▓▓  ▓\n▓▓            ▓▓\n ▓                 ▓     ▓▓▓▓▓\n ▓                 ▓     ▓▓▓▓▓\n                     ▓   ▓▓▓▓▓▓\n                     ▓▓           ▓▓\n                     ▓               ▓\n                     ▓\n     ████████████\n         █████████\n            ███████\n             ██████\n.................███..............\n")
        
        
        
@events.register(events.NewMessage(pattern=".vheart ?(.*)"))
async def vheart(event):
    await event.edit(".")
    time.sleep(0.3)
    await event.edit("..")
    time.sleep(0.3)
    await event.edit("...")
    time.sleep(0.3)
    await event.edit("..........###########\n......##############\n....################\n..##################.............########\n...##################.......#############\n....##################.....##############\n.....#################...################\n.......#################################\n.........###############################\n...........#############################\n..............##########################\n................########################\n...................#####################\n.....................##################\n.......................###############\n........................#############\n..........................##########\n...........................########\n............................######\n.............................#####\n..............................###\n...............................#")
  
 
 
@events.register(events.NewMessage(pattern=".luvart"))
async def luvart(event):
    await event.edit(".")
    time.sleep(0.3)
    await event.edit("..")
    time.sleep(0.3)
    await event.edit("...")
    time.sleep(0.3)
    await event.edit("✨✨✨✨✨✨✨✨✨✨✨✨✨\n✨✨✨💖💖💖💖💖💖💖✨✨✨\n✨✨✨✨✨💖💖💖✨✨✨✨✨\n✨✨✨✨✨💖💖💖✨✨✨✨✨\n✨✨✨✨✨💖💖💖✨✨✨✨✨\n✨✨✨✨✨💖💖💖✨✨✨✨✨\n✨✨✨💖💖💖💖💖💖💖✨✨✨\n✨✨✨✨✨✨✨✨✨✨✨✨✨\n💖💖💖💖💖💖💖💖💖💖💖💖💖\n💖💖✨✨✨💖💖💖✨✨✨💖💖\n💖✨✨✨✨✨💖✨✨✨✨✨💖\n💖✨✨✨✨✨✨✨✨✨✨✨💖\n💖💖✨✨✨✨✨✨✨✨✨💖💖\n💖💖💖✨✨✨✨✨✨✨💖💖💖\n💖💖💖💖✨✨✨✨✨💖💖💖💖\n💖💖💖💖💖✨✨✨💖💖💖💖💖\n💖💖💖💖💖💖✨💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖💖💖💖💖\n✨✨✨✨✨✨✨✨✨✨✨✨✨\n✨✨💖💖✨✨✨✨✨💖💖✨✨\n✨✨💖💖✨✨✨✨✨💖💖✨✨\n✨✨💖💖✨✨✨✨✨💖💖✨✨\n✨✨💖💖✨✨✨✨✨💖💖✨✨\n✨✨💖💖💖✨✨✨💖💖💖✨✨\n✨✨💖💖💖💖💖💖💖💖💖✨✨\n✨✨✨💖💖💖💖💖💖💖✨✨✨\n✨✨✨✨✨✨✨✨✨✨✨✨✨\nㅤ")
