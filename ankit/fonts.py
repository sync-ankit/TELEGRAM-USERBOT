from telethon import events
import ankit.client
client = ankit.client

normiefont = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
weebyfont = ['卂','乃','匚','刀','乇','下','厶','卄','工','丁','长','乚','从','𠘨','口','尸','㔿','尺','丂','丅','凵','リ','山','乂','丫','乙']
tantextfont = ['Ꭿ','Ᏸ','Ꮳ','Ꮄ','Ꮛ','Ꮄ','Ꮆ','Ꮒ','i','Ꮰ','Ꮶ','l','m','Ꮑ','Ꮻ','Ꮅ','Ꮔ','ᖇ','Ꭶ','Ꮏ','Ꮜ','Ꮙ','Ꮿ','ﾒ','Ꭹ','Ꮓ']
linetextfont = ['𝔸','𝔹','ℂ','𝔻','𝔼','𝔽','𝔾','ℍ','𝕀','𝕁','𝕂','𝕃','𝕄','ℕ','𝕆','ℙ','ℚ','ℝ','𝕊','𝕋','𝕌','𝕍','𝕎','𝕏','𝕐','ℤ']
boxtextfont = ['🄰','🄱','🄲','🄳','🄴','🄵','🄶','🄷','🄸','🄹','🄺','🄻','🄼','🄽','🄾','🄿','🅀','🅁','🅂','🅃','🅄','🅅','🅆','🅇','🅈','🅉']
bubbletextfont = ['Ⓐ','Ⓑ','Ⓒ','Ⓓ','Ⓔ','Ⓕ','Ⓖ','Ⓗ','Ⓘ','Ⓙ','Ⓚ','Ⓛ','Ⓜ','Ⓝ','Ⓞ','Ⓟ','Ⓠ','Ⓡ','Ⓢ','Ⓣ','Ⓤ','Ⓥ','Ⓦ','Ⓧ','Ⓨ','Ⓩ']
cursivefont = ['𝓪','𝓫','𝓬','𝓭','𝓮','𝓯','𝓰','𝓱','𝓲','𝓳','𝓴','𝓵','𝓶','𝓷','𝓸','𝓹','𝓺','𝓻','𝓼','𝓽','𝓾','𝓿','𝔀','𝔁','𝔂','𝔃'
]

@events.register(events.NewMessage(pattern=".wb ?(.*)"))
async def weebify(text):
    args = text.pattern_match.group(1)
    if not args:
        get = await text.get_reply_message()
        args = get.text   
    if not args:
        await text.edit("What I am Supposed to Weebify? Please Give Text Sir")
        return
    string = ''.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await text.edit(string)
    

@events.register(events.NewMessage(pattern=".tnxt ?(.*)"))
async def tantxt(text):
    args = text.pattern_match.group(1)
    if not args:
        get = await text.get_reply_message()
        args = get.text   
    if not args:
        await text.edit("What I am Supposed to tanify? Please Give Text Sir")
        return
    string = ''.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            tanycharacter = tantextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, tanycharacter)
    await text.edit(string)


@events.register(events.NewMessage(pattern=".lnt ?(.*)"))
async def linetxt(text):
    args = text.pattern_match.group(1)
    if not args:
        get = await text.get_reply_message()
        args = get.text   
    if not args:
        await text.edit("What I am Supposed to linefy? Please Give Text Sir")
        return
    string = ''.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            linecharacter = linetextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, linecharacter)
    await text.edit(string)


@events.register(events.NewMessage(pattern=".bxt ?(.*)"))
async def boxtxt(text):
    args = text.pattern_match.group(1)
    if not args:
        get = await text.get_reply_message()
        args = get.text   
    if not args:
        await text.edit("What I am Supposed to boxify? Please Give Text Sir")
        return
    string = ''.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            boxcharacter = boxtextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, boxcharacter)
    await text.edit(string)


@events.register(events.NewMessage(pattern=".bbt ?(.*)"))
async def bubbletxt(text):
    args = text.pattern_match.group(1)
    if not args:
        get = await text.get_reply_message()
        args = get.text   
    if not args:
        await text.edit("What I am Supposed to bubblify? Please Give Text Sir")
        return
    string = ''.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            bubblecharacter = bubbletextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bubblecharacter)
    await text.edit(string)

@events.register(events.NewMessage(pattern=".crs ?(.*)"))
async def cursive(text):
        args = text.pattern_match.group(1)
        if not args:
            get = await text.get_reply_message()
            args = get.text
        if not args:
            await text.edit("What I am Supposed to write in cursive? Please Give Text Sir")
            return
        string = ''.join(args).lower()
        for normiecharacter in string:
            if normiecharacter in normiefont:
                cursivecharacter = cursivefont[normiefont.index(normiecharacter)]
                string = string.replace(normiecharacter, cursivecharacter)
        await text.edit(string)