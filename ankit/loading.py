from telethon import events
import time
import asyncio
import random
import ankit.client
client = ankit.client.client
@events.register(events.NewMessage(pattern='.loading$', outgoing=True))
async def loading(event: events.NewMessage.Event):
    try:
        percentage = 0
        while percentage < 100:
            temp = 100 - percentage
            temp = temp if temp > 5 else 5
            percentage += temp / random.randint(5, 10)
            percentage = round(percentage, 2)

            progress = int(percentage // 5)
            await event.edit(f'|{"█" * progress}{"-" * (20 - progress)}| {percentage}%')
            await asyncio.sleep(.5)

        time.sleep(5)
        await event.delete()

    except Exception as e:
        print(e)