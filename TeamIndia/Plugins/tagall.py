# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.


from AliciaRobot import telethn as bot
from AliciaRobot.events import register


@register(pattern="^/all$")
async def all(event):
    if event.fwd_from:
        return
    await event.delete()
    mentions = "Members Mentioned⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣؜"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 1000):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await bot.send_message(chat, mentions, reply_to=event.message.reply_to_msg_id)




__mod_name__ = "Mention"
__help__ = """
➥ /all - it will mention group members without spam group
➥ /tagon - it will tag online members in group
➥ /tagoff - it will tag offline members in group
➥ /tagall - it will tag all members of group
➥ /tagadmins - it will tag members only
➥ /tagowner - it will tag group owner
"""

__button__ = ""
__buttons__ = ""