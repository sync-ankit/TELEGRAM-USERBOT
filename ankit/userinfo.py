from telethon import events
import ankit.client
from telethon.tl.functions.users import GetFullUserRequest
from os import remove

client = ankit.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.userinfo'))
async def userinfo(event):
    await event.delete()
    try:
        getinformation = await event.get_reply_message()
        targetid = getinformation.sender_id
        targetdetails = await client(GetFullUserRequest(targetid))
        messagelocation = event.to_id
        client.parse_mode = "html"
        userimage = await client.download_profile_photo(f"@{targetdetails.users[0].username}")
        await client.send_file(messagelocation, userimage, caption=f"👤 Firstname: {targetdetails.users[0].first_name}\n👤 Lastname: {targetdetails.users[0].last_name}\n🔗 Username: @{targetdetails.users[0].username}\n🆔 User ID: {targetdetails.users[0].id}\n☎️ Phone number: +{targetdetails.users[0].phone}\n📎 User Link: <a href='tg://user?id={targetid}'>Profile</a>\n📝 Bio: {targetdetails.full_user.about}\n🌐 Data Center ID: {targetdetails.users[0].photo.dc_id}\n🤖 Bot: {targetdetails.users[0].bot}\n👥 Common groups: {targetdetails.full_user.common_chats_count}\n🚫 Blocked: {targetdetails.full_user.blocked}")
        remove(userimage)
    except:
        pass