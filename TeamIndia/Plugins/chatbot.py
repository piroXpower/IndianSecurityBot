
import json
import re
import os
import html
import requests
import AliciaRobot.modules.sql.chatbot_sql as sql

from time import sleep
from telegram import ParseMode
from AliciaRobot import dispatcher, updater, SUPPORT_CHAT
from AliciaRobot.modules.log_channel import gloggable
from telegram import (CallbackQuery, Chat, MessageEntity, InlineKeyboardButton,
                      InlineKeyboardMarkup, Message, ParseMode, Update, Bot, User)

from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler,
                          DispatcherHandlerStop, Filters, MessageHandler,
                          run_async)

from telegram.error import BadRequest, RetryAfter, Unauthorized

from AliciaRobot.modules.helper_funcs.filters import CustomFilters
from AliciaRobot.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply

from telegram.utils.helpers import mention_html, mention_markdown, escape_markdown

 
@user_admin_no_reply
@gloggable
def aliciarm(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"rm_chat\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_alicia = sql.rem_alicia(chat.id)
        if is_alicia:
            is_alicia = sql.rem_alicia(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"AI_DISABLED\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                "Chatbot disable by {}.".format(mention_html(user.id, user.first_name)),
                parse_mode=ParseMode.HTML,
            )

    return ""

@user_admin_no_reply
@gloggable
def aliciaadd(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"add_chat\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_alicia = sql.set_alicia(chat.id)
        if is_alicia:
            is_alicia = sql.set_alicia(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"AI_ENABLE\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                "Chatbot enable by {}.".format(mention_html(user.id, user.first_name)),
                parse_mode=ParseMode.HTML,
            )

    return ""

@user_admin
@gloggable
def alicia(update: Update, context: CallbackContext):
    user = update.effective_user
    message = update.effective_message
    msg = f"Choose an option"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Enable",
            callback_data="add_chat({})")],
       [
        InlineKeyboardButton(
            text="Disable",
            callback_data="rm_chat({})")]])
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )

def alicia_message(context: CallbackContext, message):
    reply_message = message.reply_to_message
    if message.text.lower() == "alicia":
        return True
    if reply_message:
        if reply_message.from_user.id == context.bot.get_me().id:
            return True
    else:
        return False
        

def chatbot(update: Update, context: CallbackContext):
    message = update.effective_message
    chat_id = update.effective_chat.id
    bot = context.bot
    is_alicia = sql.is_alicia(chat_id)
    if not is_alicia:
        return
	
    if message.text and not message.document:
        if not alicia_message(context, message):
            return
        Message = message.text
        bot.send_chat_action(chat_id, action="typing")
        aliciaurl = requests.get('https://kukiapi.xyz/api/apikey=ALICIAROBOT/alicia/h1m4n5hu0p/message='+Message)
        Alicia = json.loads(aliciaurl.text)
        alicia = Alicia['reply']
        sleep(0.3)
        message.reply_text(alicia, timeout=60)

def list_all_chats(update: Update, context: CallbackContext):
    chats = sql.get_all_alicia_chats()
    text = "<b>ALICIA-Enabled Chats</b>\n"
    for chat in chats:
        try:
            x = context.bot.get_chat(int(*chat))
            name = x.title or x.first_name
            text += f"• <code>{name}</code>\n"
        except (BadRequest, Unauthorized):
            sql.rem_alicia(*chat)
        except RetryAfter as e:
            sleep(e.retry_after)
    update.effective_message.reply_text(text, parse_mode="HTML")

__help__ = f"""We have highly artificial intelligence chatbot of telegram which provides you real and attractive experience of chatting.
*Admins only Commands*:
  ➢ `/Chatbot`*:* Shows chatbot control panel
  
 Reports bugs at {SUPPORT_CHAT}
"""

__mod_name__ = "Chatbot"
__button__ = ""
__buttons__ = ""

CHATBOTK_HANDLER = CommandHandler("ChatBot", alicia, run_async=True)
ADD_CHAT_HANDLER = CallbackQueryHandler(aliciaadd, pattern=r"add_chat", run_async=True)
RM_CHAT_HANDLER = CallbackQueryHandler(aliciarm, pattern=r"rm_chat", run_async=True)
CHATBOT_HANDLER = MessageHandler(
    Filters.text & (~Filters.regex(r"^#[^\s]+") & ~Filters.regex(r"^!")
                    & ~Filters.regex(r"^\/")), chatbot, run_async=True)
LIST_ALL_CHATS_HANDLER = CommandHandler(
    "allchats", list_all_chats, filters=CustomFilters.dev_filter, run_async=True)

dispatcher.add_handler(ADD_CHAT_HANDLER)
dispatcher.add_handler(CHATBOTK_HANDLER)
dispatcher.add_handler(RM_CHAT_HANDLER)
dispatcher.add_handler(LIST_ALL_CHATS_HANDLER)
dispatcher.add_handler(CHATBOT_HANDLER)

__handlers__ = [
    ADD_CHAT_HANDLER,
    CHATBOTK_HANDLER,
    RM_CHAT_HANDLER,
    LIST_ALL_CHATS_HANDLER,
    CHATBOT_HANDLER,
]
