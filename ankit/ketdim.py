from telethon import events
import time
import ankit.client
client = ankit.client.client


ketdi = ["░░░░░░🚜░░░░░░🏠\n█████████████████",
 "░░░░░░🚜░░░░░🚶🏠\n█████████████████",
 "░░░░░░🚜░░░░🚶░🏠 \n█████████████████",
 "░░░░░░🚜░░🚶░░░🏠 \n█████████████████",
 "░░░░░░🚜🚶░░░░░🏠 \n█████████████████",
 "░░░░░░🚜░░░░🇰░🏠 \n█████████████████",
 "░░░░░🚜░░░░░░░░🏠 \n█████████████████",
 "░░░░🚜░░░🇰 🇪 ░🏠\n█████████████████",
 "░░░🚜░🇰 🇪 🇹░░🏠\n█████████████████",
 "░🚜░🇰 🇪 🇹 🇩 🏠\n█████████████████",
 "🚜░🇰 🇪 🇹 🇩 🇮🏠\n █████████████████",
 "🇰 🇪 🇹 🇩 🇮 🇲🏠\n█████████████████"]
@events.register(events.NewMessage)
async def ketdihandlers(event):
		if '.ketdim' in event.raw_text:
			time.sleep(0.3)
			for d in ketdi:
				time.sleep(0.3)
				await event.edit(d)