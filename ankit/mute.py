from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
import datetime
import ankit.client
client = ankit.client.client

@events.register(events.NewMessage(pattern=r'.mute', outgoing=True))
async def mute(event: events.NewMessage.Event):
    chat = await event.get_chat()
    reply_to_message = await event.get_reply_message()

    if not reply_to_message:
        await event.delete()
        return

    time_flags_dict = {
        "m": [60, "minute"],
        "h": [3600, "hour"],
        "d": [86400, "day"]
        }

    try:
        time_type = event.message.text[-1]
        count = int(event.message.text.split()[1][:-1])
        count_seconds = count * time_flags_dict[time_type][0]
        rights = ChatBannedRights(
            until_date=datetime.datetime.utcnow() + datetime.timedelta(seconds=count_seconds),
            send_messages=True
        )
        await client(EditBannedRequest(chat.id, reply_to_message.sender_id, rights))
        await event.edit(f'Muted on {count} {time_flags_dict[time_type][1]}')
    except Exception as e:
        print(e)