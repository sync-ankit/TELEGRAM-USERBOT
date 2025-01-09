from telethon import events
import ankit.client
import time
client = ankit.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.alive'))
async def alive(event):
		client = event.client
		me = await client.get_me()
		username = me.username
		img = await client.download_profile_photo(username)
		time.sleep(0.5)
		await event.respond(f"""Developer : ANKIT KUMAR🏓[@XNKIT69]
Github : @xnkit69
Instagram : @xnkit69
Telegram : @xnkitkumar
Website : xnkitk.netlify.app""", file=img)
		await event.message.delete()