from telethon import events 
from telethon.tl.functions.account import UpdateProfileRequest
import ankit.client
import time

client = ankit.client.client
@events.register(events.NewMessage(pattern=r".rename (.*)", outgoing=True))
async def rename(event):
    ok = await event.edit("Nickname changing...")
    names = event.pattern_match.group(1).strip() 
    first_name = names
    last_name = ""
    if "/" in names:
        first_name, last_name = names.split("/", 1)
        await event.edit('Nick changed succusfully')
    try:
        await event.client(UpdateProfileRequest(first_name=first_name, last_name=last_name,)) 
        await event.edit('Nick changed succusfully')
    except Exception as ex:
        await event.edit(ok, "\n`{}`".format(str(ex)))
    time.sleep(0.5)
    await event.delete()