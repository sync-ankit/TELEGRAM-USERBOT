from telethon import events
import ankit.client
from ankit.magic import Magic
import time
magic = Magic()
client = ankit.client.client
@events.register(events.NewMessage(pattern='\.magic'))
async def magicrun(event):
		time.sleep(0.2)
		for d in magic.magic:
			time.sleep(0.2)
			await event.edit(d)