from telethon import events
import ankit.client
from ankit.lovely import Lovely
import time
lovely = Lovely()
client = ankit.client.client


@events.register(events.NewMessage)
async def lovelyrun(event):
    if '.lovely' in event.raw_text:
        time.sleep(0.3)
        for d in lovely.lovely:
            time.sleep(0.3)
            await event.edit(d)
