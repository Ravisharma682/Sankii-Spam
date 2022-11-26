from DEADLYSPAM import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from DEADLYSPAM import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/d5f864ce968a27e0b9454.jpg"

DEAD_Help = "Sanki Spam Bot\n"
 
DEAD_Help += f"Command\n"

DEAD_Help += f"Bot Cmds\n"

DEAD_Help += f" `!ping` - to check ping\n `!alive` - to check bot alive/version (only main userbot will reply)\n !`restart` - to restart all spam bots \n `!addecho` - to addecho \n `!rmecho` - To remove Echo \n `!addsudo` - To add sudo user using spam bot \n\n"
 
DEAD_Help += f" ↧ Leave Commands ↧\n\n"

DEAD_Help += f" `!leave` - to leave public/private channel/groups\n\n"
 
DEAD_Help += f" ↧ Spam Command ↧\n\n"

DEAD_Help += f" `!sanki` - to raid\n `!replyraid` - to active reply raid\n `!dreplyraid` - to de-active reply raid\n `!spam` - this cmd use for Normal spam\n `!bigspam` - this cmd use for big spam\n `!uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `!delayspam` - this cmd use for delay spam\n\n"

DEAD_Help += f" !sankispam - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧\n\n"

DEAD_Help += f"© @BrandSanki\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=DEAD_Help,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/BrandSanki")
        ] 
        ]
        )
