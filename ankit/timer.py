from telethon import events
from time import sleep
import asyncio
from telethon import events
import ankit.client
client = ankit.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".timer"))
async def timer(event):
        msg=event.message.raw_text.split()
        t=int(msg[1])
        mins=0
        while t>0:
                secs=t
                if(secs>=60):
                        mins=secs//60
                        secs-=mins*60
                else: mins=0
                timer=f"{mins}:{secs}"
                await event.edit(timer)
                await asyncio.sleep(1)
                t-=1
        await event.edit("time out i!!!")
        await asyncio.sleep(3)
        await event.delete()


@events.register(events.NewMessage(outgoing=True, pattern=".numbers"))
async def numbers(event):
        msg=event.message.raw_text.split()
        t=int(msg[1])
        await event.delete()
        while t>0:
                sleep(1)
                await client.send_message(event.message.to_id,str(t))
                t-=1

@events.register(events.NewMessage(outgoing=True, pattern=".setclock"))
async def setclock(event):
    from telethon.tl.functions.account import UpdateProfileRequest
    await event.edit('Clock setting . . .')
    sleep(0.5)
    msg=event.message.raw_text.split()
    t=int(msg[1])
    t*=60
    while t>0:
            from datetime import datetime
            today = datetime.today()
            time= today.strftime("| %H:%M |")
            await client(UpdateProfileRequest(last_name=str(time)))
            await event.edit('Clock setted succesfully')
            sleep(0.5)
            await event.delete()
            await asyncio.sleep(60)
            t-=1
    await client(UpdateProfileRequest(last_name="Vaqt nisbiy tushuncha !!"))
 



from telethon import events
from time import sleep

@events.register(events.NewMessage(outgoing=True, pattern=r'\.findaccount'))
async def runsda(event):
    await event.edit("Searching...")
    sleep(1)
    await event.delete()
    messagelocation = event.to_id
    deletedid = []
    try:
        chatname = event.chat.title
        async for users in event.client.iter_participants(messagelocation):
            if users.deleted:
                deletedid.append(users.id)
        countdeletedid = len(deletedid)
        if countdeletedid == 1:
            await event.client.send_message(messagelocation, f"{countdeletedid} Deleted accounts not found\nGuruh nomi: {chatname}")
        elif countdeletedid == 0:
            await event.client.send_message(messagelocation, f"Deleted accounts not found\nGuruh nomi: {chatname}")
        else:
            await event.client.send_message(messagelocation, f"{countdeletedid} Deleted accounts not found\nGuruh nomi: {chatname}")
    except:
        await event.client.send_message(messagelocation, "Something Went Wrong")

@events.register(events.NewMessage(outgoing=True, pattern=r'\.removeaccount'))
async def runrda(event):
    await event.edit("waiting...")
    sleep(1)
    await event.delete()
    messagelocation = event.to_id
    deletedid = []
    try:
        chatname = event.chat.title
        async for users in event.client.iter_participants(messagelocation):
            if users.deleted:
                deletedid.append(users.id)
                await event.client.kick_participant(messagelocation, users.id)
        countdeletedid = len(deletedid)
        if countdeletedid == 1:
            await event.client.send_message(messagelocation, f"{countdeletedid} Deleted accounts removed from this group\n Group name:  {chatname}")
        elif countdeletedid == 0:
            await event.client.send_message(messagelocation, f"Deleted accounts not found\nGuruh nomi: {chatname}")
        else:
         await event.client.send_message(messagelocation, f"{countdeletedid} Deleted accounts kicked {chatname}")
    except:
        await event.client.send_message(messagelocation, "Some error")
 

from os import remove

@events.register(events.NewMessage(outgoing=True, pattern=r'\.psave'))
async def rundrc(event):
    await event.delete()
    try:
        getrestrictedcontent = await event.get_reply_message()
        downloadrestrictedcontent = await getrestrictedcontent.download_media()
        await event.client.send_file("me", downloadrestrictedcontent)
        remove(downloadrestrictedcontent)
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.msave'))
async def runrts(event):
    await event.delete()
    try:
        foundrestrictedcontent = await event.get_reply_message()
        restricteddata = foundrestrictedcontent.message
        await event.client.send_message("me", restricteddata)
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.rgm'))
async def runrgm(event):
    await event.edit("recovery...")
    sleep(1)
    await event.delete()
    try:
        targetgroup = event.to_id
        recoveredplace = "me"
        grouplog = await event.client.get_admin_log(targetgroup, edit=False, delete=True)
        for restore in grouplog:
            await event.client.send_message(recoveredplace, restore.original.action.message, silent=True)
    except:
        pass
        
@events.register(events.NewMessage(outgoing=True, pattern=".setbioclock"))
async def setbioclock(event):
        from telethon.tl.functions.account import UpdateProfileRequest
        await event.edit('Clock setting . . .')
        sleep(0.5)
        msg=event.message.raw_text.split()
        t=int(msg[1])
        t*=60
        while t>0:
                from datetime import datetime
                today = datetime.today()
                time= today.strftime("%H:%M | %A | %d | %B | %Y")
                await client(UpdateProfileRequest(about=str(time)))
                await event.edit('Clock setted succesfully')
                sleep(0.5)
                await event.delete()
                await asyncio.sleep(60)
                t-=1 
        await client(UpdateProfileRequest("Vaqt nisbiy tushuncha !!"))
 
