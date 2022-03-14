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

 
def alicia_group_callback(update, context):
    query = update.callback_query
    if query.data == "aliciagroup_":
        query.message.edit_text(
            text="""Here is the help for the *Backup* module:

 Only for *Group Owner*:

 ❍ /import: Reply to the backup file for the Alicia group to import as much as possible, making transfers very easy!  Note that files / photos cannot be imported due to telegram restrictions.
 ❍ /export: Export group data, which will be exported are: rules, notes (documents, images, music, video, audio, voice, text, text buttons)  """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(group)")
                 ]
                ]
            ),
        )

 
def alicia_group_bl_callback(update, context):
    query = update.callback_query
    if query.data == "aliciagroupbl_":
        query.message.edit_text(
            text=""" Here is the help for the *BlackList* module:

 Blacklists are used to stop certain triggers from being said in a group. Any time the trigger is mentioned, the message will immediately be deleted. A good combo is sometimes to pair this up with warn filters!
 
 NOTE: Blacklists do not affect group admins.
 
  ❍ /blacklist: View the current blacklisted words.
 
 Admin only:
  ❍ /addblacklist <triggers>: Add a trigger to the blacklist. Each line is considered one trigger, so using different lines will allow you to add multiple triggers.
  ❍ /unblacklist <triggers>: Remove triggers from the blacklist. Same newline logic applies here, so you can remove multiple triggers at once.
  ❍ /blacklistmode <off/del/warn/ban/kick/mute/tban/tmute>: Action to perform when someone sends blacklisted words.
 
 Blacklist sticker is used to stop certain stickers. Whenever a sticker is sent, the message will be deleted immediately.
 NOTE: Blacklist stickers do not affect the group admin
  ❍ /blsticker: See current blacklisted sticker
 Only admin:
  ❍ /addblsticker <sticker link>: Add the sticker trigger to the black list. Can be added via reply sticker
  ❍ /unblsticker <sticker link>: Remove triggers from blacklist. The same newline logic applies here, so you can delete multiple triggers at once
  ❍ /rmblsticker <sticker link>: Same as above
  ❍ /blstickermode <ban/tban/mute/tmute>: sets up a default action on what to do if users use blacklisted stickers
 Note:
  ❍ <sticker link> can be https://t.me/addstickers/<sticker> or just <sticker> or reply to the sticker message""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(group)")
                 ]
                ]
            ),
        )

 
def alicia_group_fsub_callback(update, context):
    query = update.callback_query
    if query.data == "aliciagroupfsub_":
        query.message.edit_text(
            text=""" Here is the help for the *Force Subscribe* module:

  Force Subscribe:
  ❍ Alicia can mute members who are not subscribed your channel until they subscribe
  ❍ When enabled I will mute unsubscribed members and show them a unmute button. When they pressed the button I will unmute them
  Setup
  Only creator
  ❍ Add me in your group as admin
  ❍ Add me in your channel as admin 
   
  Commmands
  ❍ /fsub {channel username} - To turn on and setup the channel.
    💡Do this first...
  ❍ /fsub - To get the current settings.
  ❍ /fsub disable - To turn of ForceSubscribe..
    💡If you disable fsub, you need to set again for working.. /fsub {channel username} 
  ❍ /fsub clear - To unmute all members who muted by me.
              """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(group)")
                 ]
                ]
            ),
        )


 
def alicia_group_control_callback(update, context):
    query = update.callback_query
    if query.data == "aliciagroupcontrol_":
        query.message.edit_text(
            text=""" Here is the help for the *Control* module:

 Blue text cleaner removed any made up commands that people send in your chat.
  ❍ /cleanblue <on/off/yes/no>: clean commands after sending
  ❍ /ignoreblue <word>: prevent auto cleaning of the command
  ❍ /unignoreblue <word>: remove prevent auto cleaning of the command
  ❍ /listblue: list currently whitelisted commands
 
 Antiflood allows you to take action on users that send more than x messages in a row. Exceeding the set flood will result in restricting that user.
  This will mute users if they send more than 10 messages in a row, bots are ignored.
  ❍ /flood: Get the current flood control setting
 • Admins only:
  ❍ /setflood <int/'no'/'off'>: enables or disables flood control
  Example: /setflood 10
  ❍ /setfloodmode <ban/kick/mute/tban/tmute> <value>: Action to perform when user have exceeded flood limit. ban/kick/mute/tmute/tban
 • Note:
  • Value must be filled for tban and tmute!!
  It can be:
  5m = 5 minutes
  6h = 6 hours
  3d = 3 days
  1w = 1 week
               """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(group)")
                 ]
                ]
            ),
        )

 
def alicia_group_disable_callback(update, context):
    query = update.callback_query
    if query.data == "aliciagroupdisable_":
        query.message.edit_text(
            text=""" Here is the help for the *Disable* module:

  ❍ /cmds: check the current status of disabled commands  
   Admins only:
  ❍ /enable <cmd name>: enable that command
  ❍ /disable <cmd name>: disable that command
  ❍ /enablemodule <module name>: enable all commands in that module
  ❍ /disablemodule <module name>: disable all commands in that module
  ❍ /listcmds: list all possible toggleable commands.
              """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(group)")
                 ]
                ]
            ),
        )



 
def alicia_group_nmode_callback(update, context):
    query = update.callback_query
    if query.data == "aliciagroupnmode_":
        query.message.edit_text(
            text=""" Here is the help for the NightMode module:

  ❍ /addnt: Adds Group to NightMode Chats
  ❍ /rmnt: Removes Group From NightMode Chats
 Note: Night Mode chats get Automatically closed at 12pm(IST)
 and Automatically openned at 6am(IST) To Prevent Night Spams.
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(group)")
                 ]
                ]
            ),
        )


# Handlers start from here 

group_callback_handler = CallbackQueryHandler(alicia_group_callback, pattern=r"aliciagroup_", run_async=True)
group_bl_callback_handler = CallbackQueryHandler(alicia_group_bl_callback, pattern=r"aliciagroupbl_", run_async=True)
group_fsub_callback_handler = CallbackQueryHandler(alicia_group_fsub_callback, pattern=r"aliciagroupfsub_")
group_control_callback_handler = CallbackQueryHandler(alicia_group_control_callback, pattern=r"aliciagroupcontrol_", run_async=True)
group_disable_callback_handler = CallbackQueryHandler(alicia_group_disable_callback, pattern=r"aliciagroupdisable_", run_async=True)
group_nmode_callback_handler = CallbackQueryHandler(alicia_group_nmode_callback, pattern=r"aliciagroupnmode_", run_async=True)






