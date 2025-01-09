from telethon import events
import ankit.client
from datetime import datetime

client = ankit.client.client


@events.register(events.NewMessage(pattern='\.ping'))
async def ping(event):
    start = datetime.now()
    msg = await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"Pong!!\n{ms} ms")
