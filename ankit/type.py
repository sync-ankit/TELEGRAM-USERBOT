from telethon import events
import time

import ankit.client
client = ankit.client.client


@events.register(events.NewMessage(outgoing=True, pattern='\.type'))
async def type(event):
    if ".type" == event.raw_text[:5]:
        orig_text = event.raw_text.split(".type ", maxsplit=1)[1]
        text = orig_text
        pb = ""
        typing_symbol = "▒"
    while(pb != orig_text):
        try:
            await event.edit(pb + typing_symbol)
            time.sleep(0.05)
            pb += text[0]
            text = text[1:]
            await event.edit(pb)
            time.sleep(0.05)
        except Exception as e:
            print(e)