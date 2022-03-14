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
 
 
def alicia_user_callback(update, context):
    query = update.callback_query
    if query.data == "aliciauser_":
        query.message.edit_text(
            text="""Here is the help for the *Horoscope* module:

  ❍ /hs <sign> 
  Usage: it will show horoscope of daily of your sign.
  List of all signs - aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius and pisces.
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(user)")
                 ]
                ]
            ),
        )

 
def alicia_user_afk_callback(update, context):
    query = update.callback_query
    if query.data == "aliciauserafk_":
        query.message.edit_text(
            text=""" *Away from group*
  ❍ /afk <reason>: mark yourself as AFK(away from keyboard).
  ❍ brb <reason>: same as the afk command - but not a command.
  When marked as AFK, any mentions will be replied to with a message to say you're not available!""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(user)")
                 ]
                ]
            ),
        )

 
def alicia_user_about_callback(update, context):
    query = update.callback_query
    if query.data == "aliciauserabout_":
        query.message.edit_text(
            text=""" *Self addded information:*
  ❍ /setme <text>: will set your info
  ❍ /me: will get your or another user's info.
  Examples: 💡
  ➩ /setme I am a wolf.
  ➩ /me @username(defaults to yours if no user specified)

   *Information others add on you:*
  ❍ /bio: will get your or another user's bio. This cannot be set by yourself.
  ❍ /setbio <text>: while replying, will save another user's bio 
  Examples: 💡
  ➩ /bio @username(defaults to yours if not specified).
  ➩ /setbio This user is a wolf (reply to the user)
              """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(user)")
                 ]
                ]
            ),
        )


 
def alicia_user_info_callback(update, context):
    query = update.callback_query
    if query.data == "aliciauserinfo_":
        query.message.edit_text(
            text=""" *Overall Information about you:*
  ❍ /info: get information about a user.
   *GET ID:*
  ❍ /id: get the current group id. If used by replying to a message, gets that user's id.
  ❍ /gifid: reply to a gif to me to tell you its file ID.
               """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(user)")
                 ]
                ]
            ),
        )

 
def alicia_user_history_callback(update, context):
    query = update.callback_query
    if query.data == "aliciauserhistory_":
        query.message.edit_text(
            text="""  *GET NAME HISTORY OF USER*
   ❍ sangmata : /sg - View user name history.
   NOTE: THIS COMMAND WILL WORK IF YOU USED IN REPLY OF USER MESSAGE.
              """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(user)")
                 ]
                ]
            ),
        )



 
def alicia_user_extra_callback(update, context):
    query = update.callback_query
    if query.data == "aliciauserextra_":
        query.message.edit_text(
            text=""" Alicia have some extra tool for users, they can use also them*:*
    *Poto* - You can download anyuser profile pic via this tool
  ❍ /poto - reply to user for download all profile picsF
  ❍ /poto 1 - download specific number of pic, it will download first pic of user

    *Fake iDentity* - get easily fake identiy of user
  ❍ /fakegen - generate fake id 
  ❍ /picgen - generate fake pic
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(user)")
                 ]
                ]
            ),
        )


# Handlers start from here 

user_callback_handler = CallbackQueryHandler(alicia_user_callback, pattern=r"aliciauser_", run_async=True)
user_afk_callback_handler = CallbackQueryHandler(alicia_user_afk_callback, pattern=r"aliciauserafk_", run_async=True)
user_about_callback_handler = CallbackQueryHandler(alicia_user_about_callback, pattern=r"aliciauserabout_", run_async=True)
user_info_callback_handler = CallbackQueryHandler(alicia_user_info_callback, pattern=r"aliciauserinfo_", run_async=True)
user_histroy_callback_handler = CallbackQueryHandler(alicia_user_history_callback, pattern=r"aliciauserhistory_", run_async=True)
user_extra_callback_handler = CallbackQueryHandler(alicia_user_extra_callback, pattern=r"aliciauserextra_", run_async=True)






