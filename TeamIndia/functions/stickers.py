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

 
def alicia_sticker_callback(update, context):
    query = update.callback_query
    if query.data == "aliciasticker_":
        query.message.edit_text(
            text="""Here is the help for the *Stickers* module:

   *Stickers made easy with stickers module!*
  
  ❍ /stickers: Find stickers for given term on combot sticker catalogue 
  
  ❍ /steal or /kang: Reply to a sticker to add it to your pack.
  
  ❍ /remove: Reply to your anime exist sticker to your pack to delete it.
  
  ❍ /stickerid: Reply to a sticker to me to tell you its file ID.
  
  ❍ /getsticker: Reply to a sticker to me to upload its raw PNG file.
  
  ❍ /addfsticker or /afs <custom name>: Reply to a sticker to add it into your favorite pack list.
  
  ❍ /myfsticker or /mfs: Get list of your favorite packs.
  
  ❍ /removefsticker or /rfs <custom name>: Reply to a sticker to remove it into your favorite pack list.
  
  *Example:* `/addfstickers Alicia`
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(stickers)")
                 ]
                ]
            ),
        )

 
def alicia_sticker_memify_callback(update, context):
    query = update.callback_query
    if query.data == "aliciastickermemify_":
        query.message.edit_text(
            text=""" Here is the help for the *Memify* module:

 You can create stickers via this module - 
 ❍ /animate text : Randomly Generate Stickers with Given Text
 ❍ /mmf <upper text ; down text> : Write on stickers
 ❍ /mms <upper text ; lower text> : Advanced version of memify
 ❍ /carbon - Make Carbon Of Code.
 ❍ /slet <text> : Convert Text In Sticker
 ❍ /q - make sticker via qouting message 
 ❍ /kang - save stickers to pack""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(stickers)")
                 ]
                ]
            ),
        )

 
def alicia_sticker_transform_callback(update, context):
    query = update.callback_query
    if query.data == "aliciastickertransform_":
        query.message.edit_text(
            text=""" Here is the help for the *Transform* module:

  This Module Will Transform media and Make It as Sticker.
  ❍ /ghost reply to media 
  UsageEnchance your image to become a ghost!.
  ❍ /flip reply to media 
  UsageTo flip your image reply to media
  ❍ /mirror reply to media 
  UsageTo mirror your image reply to media 
  ❍ /bw reply to media 
  UsageTo Change your colorized image to b/w image!
  ❍ /poster reply to media 
  UsageTo posterize your image! reply to media 
  ❍ /rotate <value>. reply to media 
  UsageTo rotate your image The value is range 1-360 if not it'll give default value which is 90
  *NOTE* - if you want image not sticker then hit /getsticker command.
              """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(stickers)")
                 ]
                ]
            ),
        )


 
def alicia_sticker_dpic_callback(update, context):
    query = update.callback_query
    if query.data == "aliciastickerdpic_":
        query.message.edit_text(
            text=""" Here is the help for the *DocPic* module:

  ❍ /dpic <with reply any document image> 
  Usage: Convert any Document Image to Full Size Image.
               """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(stickers)")
                 ]
                ]
            ),
        )




# Handlers start from here 

sticker_callback_handler = CallbackQueryHandler(alicia_sticker_callback, pattern=r"aliciasticker_", run_async=True)
sticker_memify_callback_handler = CallbackQueryHandler(alicia_sticker_memify_callback, pattern=r"aliciastickermemify_", run_async=True)
sticker_transform_callback_handler = CallbackQueryHandler(alicia_sticker_transform_callback, pattern=r"aliciastickertransform_", run_async=True)
sticker_dpic_callback_handler = CallbackQueryHandler(alicia_sticker_dpic_callback, pattern=r"aliciastickerdpic_", run_async=True)







