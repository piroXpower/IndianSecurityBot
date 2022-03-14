from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from AliciaRobot.__main__ import *


# Buttons Function for admin module

 
def alicia_tools_callback(update, context):
    query = update.callback_query
    if query.data == "aliciatools_":
        query.message.edit_text(
            text=""" Here is the help for the *Tools* module:

 *Date-time-Weather*
  ❍ /time <country code>*:* Gives information about a timezone.
  ❍ /weather <city>*:* Get weather info in a particular place.
  ❍ /wttr <city>*:* Advanced weather module, usage same as /weather
  ❍ /wttr moon*:* Get the current status of moon
 
 *Converts*
  ❍ /encrypt*:* Encrypts The Given Text
  ❍ /decrypt*:* Decrypts Previously Ecrypted Text
  ❍ /zip*:* reply to a telegram file to compress it in .zip format
  ❍ /unzip*:* reply to a telegram file to decompress it from the .zip format
  
  *live cricket score*
  ❍ /cs*:* Latest live scores from cricinfo
 
  *Clean Deleted Accounts*
  ❍ /zombies clean : it will remove all zombies account from group
      """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(tools)")
                 ]
                ]
            ),
        )

 
def alicia_tools_barcode_callback(update, context):
    query = update.callback_query
    if query.data == "aliciatoolsbarcode_":
        query.message.edit_text(
            text=""" Here is the help for the *Barcode* module:

  ❍ /makeqr <content>
  Usage: Make a QR Code from the given content.
  Example: /makeqr www.google.com
  Note: use /decode <reply to barcode/qrcode> to get decoded content.
  
  ❍ /barcode <content>
  Usage: Make a BarCode from the given content.
  Example: /barcode www.google.com"
  Note: use /decode <reply to barcode/qrcode> to get decoded content.""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(tools)")
                 ]
                ]
            ),
        )

 
def alicia_tools_cc_callback(update, context):
    query = update.callback_query
    if query.data == "aliciatoolscc_":
        query.message.edit_text(
            text="""Here is the help for the *CC-Check* module:

  ❍ /au <cc>: Stripe Auth given CC
  ❍ /pp <cc>: Paypal 1$ Guest Charge
  ❍ /ss <cc>: Speedy Stripe Auth
  ❍ /ch <cc>: Check If CC is Live
  ❍ /bin <bin>: Gather's Info About the bin
  ❍ /gen <bin>: Generates CC with given bin
  ❍ /key <sk>: Checks if Stripe key is Live
  More Gates Soon...
  Note: Format of cc is ccnum|mm|yy|cvv
              """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(tools)")
                 ]
                ]
            ),
        )


 
def alicia_tools_telegraph_callback(update, context):
    query = update.callback_query
    if query.data == "aliciatoolstelegraph_":
        query.message.edit_text(
            text=""" Here is the help for the *Telegraph* module:

 ❍ /tgm : Get Telegraph Link Of Replied Media
 ❍ /tgt: Get Telegraph Link of Replied Text
               """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(tools)")
                 ]
                ]
            ),
        )

 
def alicia_tools_tts_callback(update, context):
    query = update.callback_query
    if query.data == "aliciatoolstts_":
        query.message.edit_text(
            text="""Here is the help for the *TTS/STT* module:

  I can convert text to voice and voice to text..
   ❍ /tts <lang code>: Reply to any message to get text to speech output
   ❍ /stt: Type in reply to a voice message(support english only) to extract text from it.
  Language Codes
  af,am,ar,az,be,bg,bn,bs,ca,ceb,co,cs,cy,da,de,el,en,eo,es,
  et,eu,fa,fi,fr,fy,ga,gd,gl,gu,ha,haw,hi,hmn,hr,ht,hu,hy,
  id,ig,is,it,iw,ja,jw,ka,kk,km,kn,ko,ku,ky,la,lb,lo,lt,lv,mg,mi,mk,
  ml,mn,mr,ms,mt,my,ne,nl,no,ny,pa,pl,ps,pt,ro,ru,sd,si,sk,sl,
  sm,sn,so,sq,sr,st,su,sv,sw,ta,te,tg,th,tl,tr,uk,ur,uz,
  vi,xh,yi,yo,zh,zh_CN,zh_TW,zu
              """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(tools)")
                 ]
                ]
            ),
        )



 
def alicia_tools_search_callback(update, context):
    query = update.callback_query
    if query.data == "aliciatoolsearch_":
        query.message.edit_text(
            text=""" Here is the help for the *Search* module:

  ❍ /google <text>: Perform a google search
  ❍ /img <text>: Search Google for images and returns them
   For greater no. of results specify lim, For eg: /img hello lim=10
  ❍ /app <appname>: Searches for an app in Play Store and returns its details.
  ❍ /reverse: Does a reverse image search of the media which it was replied to.
  ❍ /gps <location>: Get gps location.
  ❍ /twt username : Scrap latest tweet from someone
  ❍ /github <username>: Get information about a GitHub user.
  ❍ /country <country name>: Gathering info about given country
  ❍ /imdb <Movie name>: Get full info about a movie with imdb.com
  ❍ Alicia <query>: Alicia answers the query
   💡Ex: Alicia where is India?
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(tools)")
                 ]
                ]
            ),
        )


# Handlers start from here 

tools_callback_handler = CallbackQueryHandler(alicia_tools_callback, pattern=r"aliciatools_", run_async=True)
tools_barcode_callback_handler = CallbackQueryHandler(alicia_tools_barcode_callback, pattern=r"aliciatoolsbarcode_", run_async=True)
tools_cc_callback_handler = CallbackQueryHandler(alicia_tools_cc_callback, pattern=r"aliciatoolscc_", run_async=True)
tools_telegraph_callback_handler = CallbackQueryHandler(alicia_tools_telegraph_callback, pattern=r"aliciatoolstelegraph_", run_async=True)
tools_tts_callback_handler = CallbackQueryHandler(alicia_tools_tts_callback, pattern=r"aliciatoolstts_", run_async=True)
tools_search_callback_handler = CallbackQueryHandler(alicia_tools_search_callback, pattern=r"aliciatoolsearch_", run_async=True)






