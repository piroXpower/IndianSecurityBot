from asyncio.exceptions import TimeoutError

from telethon.errors.rpcerrorlist import YouBlockedUserError
from AliciaRobot import ubot
from AliciaRobot.events import register


@register(pattern="^/sg ?(.*)")
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.reply("```Reply to get Name and Username History...```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.reply("```Getting info, Wait plox ...```")
        return
    await steal.reply("```Retrieving This Person's Name Change History Information```")
    try:
        async with ubot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
             
            except YouBlockedUserError:
                await steal.reply("```For your kind information, you blocked @Sangmatainfo_bot, Unblock it```")
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await steal.reply(f"`{r.message}`")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await steal.reply("```This Person Has Never Changed His Name```")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await steal.reply(f"```{response.message}```")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await steal.reply("`I'm under stress`")


__mod_name__ = "Sangmata"

# __help__ = """
#  ❍ sangmata *:* /sg - View user name history.
# """
__button__ = ""
__buttons__ = ""

