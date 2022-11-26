
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID, OWNER_NAME

DEADLY_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/b066ef5a06391f0151170.jpg"


Deadly_Button = [
        [
        Button.url("𝗚𝗿𝗼𝘂𝗽", "https://t.me/BrandSanki"),
        Button.url("𝗣𝗼𝘄𝗲𝗿𝗲𝗱", "https://t.me/iTs_Hexor")
        ],
        [
        Button.url("𝗦𝘂𝗽𝗽𝗼𝗿𝘁", "https://t.me/esport_Bots")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[𝗛𝗲𝘅𝗼𝗿'𝘅𝗗](tg://user?id={1964732367})"
        DEADLY_ON = f"""
𝗛𝗮𝘆 {mention}, 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗖𝗿𝗲𝗮𝘁𝗲𝗱 𝗕𝘆 𝗠𝘆 𝗠𝗮𝘀𝘁𝗲𝗿 {creator} ! 𝗔𝗻𝗱 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 {myOwner} . 𝗖𝗹𝗶𝗰𝗸 𝗕𝗲𝗹𝗼𝘄 𝗔𝗻𝗱 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗔𝗻𝗱 𝗙𝗶𝗴𝗵𝘁𝗶𝗻𝗴 𝗚𝗿𝗼𝘂𝗽𝘀 🦁 !!
    """
        await e.client.send_file(e.chat_id, DEADLY_IMG, caption=DEADLY_ON, buttons=Deadly_Button)
