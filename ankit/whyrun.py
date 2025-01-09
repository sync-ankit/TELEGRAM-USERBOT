from telethon import events
import ankit.client
import random
client = ankit.client.client

whylist = ["""Nega Otabek borku Onabek yoq 😂❓ Nega""","""Nega uyg'otadigon soat boru uxlatadigon soat yoq ❓ Nega""","""Nega Ostiruvchi dori bor -u pasaytiruvchi dori yoq Nega 😂""","""Nega Akademiya boru Ukademiya yoq 😜 Nega""","""Nega Temir ismi boru Mis ismi yoq 🤔 Nega""","""Nega Calkulayotir boru Calyiglayotor yoq 💇‍♂️ Nega""","""Nega Kundosh bor Nega Tundosh yoq Nega 😂😂""", """Nega Oshqozonda Qozon yoq Nega 🍭""", """Nega Boychechak boy emas 🌻 Nega""", """Nega Tuyaqush va tuya aka uka emas Nega 🐫""", """Nega qorqiz boruu yomgir qiz yoq nega 🌧️""","""Nega Mandarin boru Sandarin yoq Nega 🤪""","""Nega Nega """, """❓""", """Nega"""]

@events.register(events.NewMessage(pattern=".why"))
async def why(event):
  anim = random.choice(whylist)
  return await event.edit(anim)