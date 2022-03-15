import logging
import os
import sys
import time
import spamwatch

import telegram.ext as tg
from redis import StrictRedis
from pyrogram import Client, errors
from telethon import TelegramClient
from telethon.sessions import StringSession
from Python_ARQ import ARQ
from aiohttp import ClientSession


INFOPIC = True                                                                                                                                                                                                                                                       
SPAMWATCH_SUPPORT_CHAT = ""                                                                                                                                                                                                                                          
TIME_API_KEY = ""                                                                                                                                                                                                                                                    
HEROKU_API_KEY = ""                                                                                                                                                                                                                                                  
HEROKU_APP_NAME = ""                                                                                                                                                                                                                                                 
WALL_API = ""                                                                                                                                                                                                                                                        
CASH_API_KEY = ""                                                                                                                                                                                                                                                    
DONATION_LINK = "paypal.me/piroXpower"                                                                                                                                                                                                                                 
WEBHOOK = False                                                                                                                                                                                                                                                      
DEL_CMDS = False                                                        
StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)


# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", "")

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", -1001204088829)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")

    try:
        DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in os.environ.get("DEMONS", "").split())
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in os.environ.get("WOLVES", "").split())
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in os.environ.get("TIGERS", "").split())
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    INFOPIC = bool(os.environ.get("INFOPIC", False))
    EVENT_LOGS = os.environ.get("EVENT_LOGS", -1001459323267)
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "https://TeamIndia.herokuapp.com/")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get("API_ID", 2857558)
    API_HASH = os.environ.get("API_HASH", "1038be815e038592fa2b483c13dd6c4b")
    BOT_ID = os.environ.get("BOT_ID", "1613196478")
    BOT_NAME = os.environ.get("BOT_NAME", "TGManagerBot")
    BOT_USERNAME = int(os.environ.get("BOT_USERNAME", ""))
    DB_URI = os.environ.get("DATABASE_URL", "")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "")
    DONATION_LINK = os.environ.get("DONATION_LINK")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", None)
    VIRUS_API_KEY = os.environ.get("VIRUS_API_KEY", None)
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "rss").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    CASH_API_KEY = os.environ.get("CASH_API_KEY", "-xyz")
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
    AI_API_KEY = os.environ.get("AI_API_KEY", None)
    WALL_API = os.environ.get("WALL_API", None)
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "")
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    REDIS_URL = os.environ.get("REDIS_URL", "")
    ARQ_API_URL = os.environ.get("ARQ_API_URL", "https://thearq.tech")
    ARQ_API_KEY = os.environ.get("ARQ_API_KEY", "NAQKZO-UMQSBG-IUTXPK-WZRJDB-ARQ")

 
    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)

    if STRING_SESSION:
        ubot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
    else:
        sys.exit(1)

    try:
        ubot.start()
    except BaseException:
        print("Network Error/INVALID TOKEN !")
        sys.exit(1)
        


    try:
        BL_CHATS = set(int(x) for x in os.environ.get("BL_CHATS", "").split())
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")


else:
    from TeamIndia.config import Development as Config

    TOKEN = ""

    try:
        OWNER_ID = #YOUR OWNER_ID
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = #YOUR LOGHER                                                                                                                                                                                                                                     
    OWNER_USERNAME = "piroxpower"                                                                                                                                                                                                                                 
    LOAD = ""                                                                                                                                                                                                                                                        
    EVENT_LOGS = -1001774935713                                                                                                                                                                                                                                      
    URL = "https://TeamIndia.herokuapp.com/"                                                                                                                                                                                                                       
    PORT = 5000                                                                                                                                                                                                                                                      
    API_ID = 2857558                                                                                                                                                                                                                                                 
    API_HASH = "1038be815e038592fa2b483c13dd6c4b"                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                     
    DB_URI = ""                                                                                                                                                               
    MONGO_DB_URI = ""                                                                                                                                                             
    TEMP_DOWNLOAD_DIRECTORY = "./"                                                                                                                                                                                                                                   
    BOT_ID = 1240287427                                                                                                                                                                                                                                              
    NO_LOAD = "rss"                                                                                                                                                                                                                                                  
    STRICT_GBAN = True                                                                                                                                                                                                                                               
    ALLOW_EXCL = True                                                                                                                                                                                                                                                
    TOKEN = ""                                                                                                                                                                                                         
    SUPPORT_CHAT = "IndianSupportGroup"                                                                                                                                                                                                                                 
    ARQ_API_KEY = "DOAGPB-DQBYDD-PVINUY-DSUAHO-ARQ"                                                                                                                                                                                                                  
    ARQ_API_URL = "https://thearq.tech"                                                                                                                                                                                                                              
    CERT_PATH = ""                                                                                                                                                                                                                                                   
    WORKERS = 8                                                                                                                                                                                                                                                      
    SPAMWATCH_API = "sJsaTYZnYqTR7z~pq8OAdVj2UIktizitY5k6ivnErXkArICQv_ZbNmG6HMDlE7Lg"                                                                                                                                                                               
    REDIS_URL = ""                                                                                                               
    STRING_SESSION = "1AZWarzoBuyHII-icttyUtvtubNyeDRvmf3TaqsGDxFWm9V9VqlrnAWDIEKY5emvS9Gqi0ilnP1ZFPJA2KZh3_V53NZdZGDLY8qHnQPcMgJl31ZqMusI9_B-KdxyrggS7ERpR9EJnZp4Y89PCxk2_QOJ39U-u6tlRoQBF3dh8SVXU-3U4CSZPDSF3MSTI2azSwL-CxEdVGu0DHlQk5hsZMunSNqo1zSl-pODwGAmofevPWe6HhARt3V4qfn-1BeOzWdLNJzZtWYA89uLFasEVAfdVHc2h9bGr55h1hBkS5hcPJt_Vv_2f_lAjXaWBdGTY4xcFkk0fsKI8IJSmHToFalF2SkRKUcA="
    try:                                                                                                                                                                                                                                                             
        DRAGONS = set(int(x) for x in [])                                                                                                                                                                                                                            
        DEV_USERS = set(int(x) for x in [])                                                                                                                                                                                                                          
    except ValueError:                                                                                                                                                                                                                                               
        raise Exception("Your sudo or dev users list does not contain valid integers.")                                                                                                                                                                              
                                                                                                                                                                                                                                                                     
    try:                                                                                                                                                                                                                                                             
        DEMONS = set(int(x) for x in [])                                                                                                                                                                                                                             
    except ValueError:                                                                                                                                                                                                                                               
        raise Exception("Your support users list does not contain valid integers.")                                                                                                                                                                                  
                                                                                                                                                                                                                                                                     
    try:                                                                                                                                                                                                                                                             
        WOLVES = set(int(x) for x in [])                                                                                                                                                                                                                             
    except ValueError:                                                                                                                                                                                                                                               
        raise Exception("Your whitelisted users list does not contain valid integers.")                                                                                                                                                                              
                                                                                                                                                                                                                                                                     
    try:                                                                                                                                                                                                                                                             
        TIGERS = set(int(x) for x in [])                                                                                                                                                                                                                             
    except ValueError:                                                                                                                                                                                                                                               
        raise Exception("Your tiger users list does not contain valid integers.")

DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add()
DEV_USERS.add(5125042013)
DEV_USERS.add(5125042013)
DEV_USERS.add(5125042013)
DEV_USERS.add(5125042013)
DRAGONS.add(5125042013)
DRAGONS.add(5125042013)

if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("SpamWatch API key missing! recheck your config.")
else:
    try:
        sw = spamwatch.Client(SPAMWATCH_API)
    except:
        sw = None
        LOGGER.warning("Can't connect to SpamWatch!")


aiohttpsession = ClientSession()


updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("india", API_ID, API_HASH)
pbot = Client("indiaPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
dispatcher = updater.dispatcher


DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)



# Load at end to ensure all prev variables have been set
from TeamIndia.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
