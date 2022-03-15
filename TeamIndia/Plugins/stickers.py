import os

import math

import cloudscraper

import urllib.request as urllib

from PIL import Image

from html import escape

from bs4 import BeautifulSoup as bs



from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from telegram import TelegramError, Update

from telegram.ext import CallbackContext

from telegram.utils.helpers import mention_html



from AliciaRobot import dispatcher

from AliciaRobot.modules.disable import DisableAbleCommandHandler



combot_stickers_url = "https://combot.org/telegram/stickers?q="





def stickerid(update: Update, context: CallbackContext):

    msg = update.effective_message

    if msg.reply_to_message and msg.reply_to_message.sticker:

        update.effective_message.reply_text(

            "Hello "

            + f"{mention_html(msg.from_user.id, msg.from_user.first_name)}"

            + ", The sticker id you are replying is :\n <code>"

            + escape(msg.reply_to_message.sticker.file_id)

            + "</code>",

            parse_mode=ParseMode.HTML,

        )

    else:

        update.effective_message.reply_text(

            "Hello "

            + f"{mention_html(msg.from_user.id, msg.from_user.first_name)}"

            + ", Please reply to sticker message to get id sticker",

            parse_mode=ParseMode.HTML,

        )





def kang(update: Update, context: CallbackContext):

    msg = update.effective_message

    user = update.effective_user

    args = context.args

    packnum = 0

    packname = "f" + str(user.id) + "_by_" + context.bot.username

    packname_found = 0

    max_stickers = 120

    while packname_found == 0:

        try:

            stickerset = context.bot.get_sticker_set(packname)

            if len(stickerset.stickers) >= max_stickers:

                packnum += 1

                packname = (

                    "f"

                    + str(packnum)

                    + "_"

                    + str(user.id)

                    + "_by_"

                    + context.bot.username

                )

            else:

                packname_found = 1

        except TelegramError as e:

            if e.message == "Stickerset_invalid":

                packname_found = 1

    kangsticker = "kangsticker.png"

    is_animated = False

    file_id = ""



    if msg.reply_to_message:

        if msg.reply_to_message.sticker:

            if msg.reply_to_message.sticker.is_animated:

                is_animated = True

            file_id = msg.reply_to_message.sticker.file_id



        elif msg.reply_to_message.photo:

            file_id = msg.reply_to_message.photo[-1].file_id

        elif msg.reply_to_message.document:

            file_id = msg.reply_to_message.document.file_id

        else:

            msg.reply_text("Yea, I can't kang that.")



        kang_file = context.bot.get_file(file_id)

        if not is_animated:

            kang_file.download("kangsticker.png")

        else:

            kang_file.download("kangsticker.tgs")



        if args:

            sticker_emoji = str(args[0])

        elif msg.reply_to_message.sticker and msg.reply_to_message.sticker.emoji:

            sticker_emoji = msg.reply_to_message.sticker.emoji

        else:

            sticker_emoji = "ð¤"



        if not is_animated:

            try:

                im = Image.open(kangsticker)

                maxsize = (512, 512)

                if (im.width and im.height) < 512:

                    size1 = im.width

                    size2 = im.height

                    if im.width > im.height:

                        scale = 512 / size1

                        size1new = 512

                        size2new = size2 * scale

                    else:

                        scale = 512 / size2

                        size1new = size1 * scale

                        size2new = 512

                    size1new = math.floor(size1new)

                    size2new = math.floor(size2new)

                    sizenew = (size1new, size2new)

                    im = im.resize(sizenew)

                else:

                    im.thumbnail(maxsize)

                if not msg.reply_to_message.sticker:

                    im.save(kangsticker, "PNG")

                context.bot.add_sticker_to_set(

                    user_id=user.id,

                    name=packname,

                    png_sticker=open("kangsticker.png", "rb"),

                    emojis=sticker_emoji,

                )

                msg.reply_text(

                    f"Sticker successfully added to [pack](t.me/addstickers/{packname})"

                    + f"\nEmoji is: {sticker_emoji}",

                    parse_mode=ParseMode.MARKDOWN,

                )



            except OSError as e:

                msg.reply_text("I can only kang images m8.")

                print(e)

                return



            except TelegramError as e:

                if e.message == "Stickerset_invalid":

                    makepack_internal(

                        update,

                        context,

                        msg,

                        user,

                        sticker_emoji,

                        packname,

                        packnum,

                        png_sticker=open("kangsticker.png", "rb"),

                    )

                elif e.message == "Sticker_png_dimensions":

                    im.save(kangsticker, "PNG")

                    context.bot.add_sticker_to_set(

                        user_id=user.id,

                        name=packname,

                        png_sticker=open("kangsticker.png", "rb"),

                        emojis=sticker_emoji,

                    )

                    msg.reply_text(

                        f"Sticker successfully added to [pack](t.me/addstickers/{packname})"

                        + f"\nEmoji is: {sticker_emoji}",

                        parse_mode=ParseMode.MARKDOWN,

                    )

                elif e.message == "Invalid sticker emojis":

                    msg.reply_text("Invalid emoji(s).")

                elif e.message == "Stickers_too_much":

                    msg.reply_text("Max packsize reached. Press F to pay respecc.")

                elif e.message == "Internal Server Error: sticker set not found (500)":

                    msg.reply_text(

                        "Sticker successfully added to [pack](t.me/addstickers/%s)"

                        % packname

                        + "\n"

                        "Emoji is:" + " " + sticker_emoji,

                        parse_mode=ParseMode.MARKDOWN,

                    )

                print(e)



        else:

            packname = "animation" + str(user.id) + "_by_" + context.bot.username

            packname_found = 0

            max_stickers = 50

            while packname_found == 0:

                try:

                    stickerset = context.bot.get_sticker_set(packname)

                    if len(stickerset.stickers) >= max_stickers:

                        packnum += 1

                        packname = (

                            "animation"

                            + str(packnum)

                            + "_"

                            + str(user.id)

                            + "_by_"

                            + context.bot.username

                        )

                    else:

                        packname_found = 1

                except TelegramError as e:

                    if e.message == "Stickerset_invalid":

                        packname_found = 1

            try:

                context.bot.add_sticker_to_set(

                    user_id=user.id,

                    name=packname,

                    tgs_sticker=open("kangsticker.tgs", "rb"),

                    emojis=sticker_emoji,

                )

                msg.reply_text(

                    f"Sticker successfully added to [pack](t.me/addstickers/{packname})"

                    + f"\nEmoji is: {sticker_emoji}",

                    parse_mode=ParseMode.MARKDOWN,

                )

            except TelegramError as e:

                if e.message == "Stickerset_invalid":

                    makepack_internal(

                        update,

                        context,

                        msg,

                        user,

                        sticker_emoji,

                        packname,

                        packnum,

                        tgs_sticker=open("kangsticker.tgs", "rb"),

                    )

                elif e.message == "Invalid sticker emojis":

                    msg.reply_text("Invalid emoji(s).")

                elif e.message == "Internal Server Error: sticker set not found (500)":

                    msg.reply_text(

                        "Sticker successfully added to [pack](t.me/addstickers/%s)"

                        % packname

                        + "\n"

                        "Emoji is:" + " " + sticker_emoji,

                        parse_mode=ParseMode.MARKDOWN,

                    )

                print(e)



    elif args:

        try:

            try:

                urlemoji = msg.text.split(" ")

                png_sticker = urlemoji[1]

                sticker_emoji = urlemoji[2]

            except IndexError:

                sticker_emoji = "ð¤"

            urllib.urlretrieve(png_sticker, kangsticker)

            im = Image.open(kangsticker)

            maxsize = (512, 512)

            if (im.width and im.height) < 512:

                size1 = im.width

                size2 = im.height

                if im.width > im.height:

                    scale = 512 / size1

                    size1new = 512

                    size2new = size2 * scale

                else:

                    scale = 512 / size2

                    size1new = size1 * scale

                    size2new = 512

                size1new = math.floor(size1new)

                size2new = math.floor(size2new)

                sizenew = (size1new, size2new)

                im = im.resize(sizenew)

            else:

                im.thumbnail(maxsize)

            im.save(kangsticker, "PNG")

            msg.reply_photo(photo=open("kangsticker.png", "rb"))

            context.bot.add_sticker_to_set(

                user_id=user.id,

                name=packname,

                png_sticker=open("kangsticker.png", "rb"),

                emojis=sticker_emoji,

            )

            msg.reply_text(

                f"Sticker successfully added to [pack](t.me/addstickers/{packname})"

                + f"\nEmoji is: {sticker_emoji}",

                parse_mode=ParseMode.MARKDOWN,

            )

        except OSError as e:

            msg.reply_text("I can only kang images m8.")

            print(e)

            return

        except TelegramError as e:

            if e.message == "Stickerset_invalid":

                makepack_internal(

                    update,

                    context,

                    msg,

                    user,

                    sticker_emoji,

                    packname,

                    packnum,

                    png_sticker=open("kangsticker.png", "rb"),

                )

            elif e.message == "Sticker_png_dimensions":

                im.save(kangsticker, "PNG")

                context.bot.add_sticker_to_set(

                    user_id=user.id,

                    name=packname,

                    png_sticker=open("kangsticker.png", "rb"),

                    emojis=sticker_emoji,

                )

                msg.reply_text(

                    "Sticker successfully added to [pack](t.me/addstickers/%s)"

                    % packname

                    + "\n"

                    + "Emoji is:"

                    + " "

                    + sticker_emoji,

                    parse_mode=ParseMode.MARKDOWN,

                )

            elif e.message == "Invalid sticker emojis":

                msg.reply_text("Invalid emoji(s).")

            elif e.message == "Stickers_too_much":

                msg.reply_text("Max packsize reached. Press F to pay respecc.")

            elif e.message == "Internal Server Error: sticker set not found (500)":

                msg.reply_text(

                    "Sticker successfully added to [pack](t.me/addstickers/%s)"

                    % packname

                    + "\n"

                    "Emoji is:" + " " + sticker_emoji,

                    parse_mode=ParseMode.MARKDOWN,

                )

            print(e)

    else:

        packs = "Please reply to a sticker, or image to kang it!\nOh, by the way. here are your packs:\n"

        if packnum > 0:

            firstpackname = "f" + str(user.id) + "_by_" + context.bot.username

            for i in range(0, packnum + 1):

                if i == 0:

                    packs += f"[pack](t.me/addstickers/{firstpackname})\n"

                else:

                    packs += f"[pack{i}](t.me/addstickers/{packname})\n"

        else:

            packs += f"[pack](t.me/addstickers/{packname})"

        msg.reply_text(packs, parse_mode=ParseMode.MARKDOWN)

    try:

        if os.path.isfile("kangsticker.png"):

            os.remove("kangsticker.png")

        elif os.path.isfile("kangsticker.tgs"):

            os.remove("kangsticker.tgs")

    except:

        pass





def makepack_internal(

    update,

    context,

    msg,

    user,

    emoji,

    packname,

    packnum,

    png_sticker=None,

    tgs_sticker=None,

):

    name = user.first_name

    name = name[:50]

    keyboard = InlineKeyboardMarkup(

        [[InlineKeyboardButton(text="View Pack", url=f"{packname}")]]

    )

    try:

        extra_version = ""

        if packnum > 0:

            extra_version = " " + str(packnum)

        if png_sticker:

            success = context.bot.create_new_sticker_set(

                user.id,

                packname,

                f"{name}s kang pack" + extra_version,

                png_sticker=png_sticker,

                emojis=emoji,

            )

        if tgs_sticker:

            success = context.bot.create_new_sticker_set(

                user.id,

                packname,

                f"{name}s animated kang pack" + extra_version,

                tgs_sticker=tgs_sticker,

                emojis=emoji,

            )



    except TelegramError as e:

        print(e)

        if e.message == "Sticker set name is already occupied":

            msg.reply_text(

                "<b>Your Sticker Pack is already created!</b>"

                "\n\nYou can now reply to images, stickers and animated sticker with /steal to add them to your pack"

                "\n\n<b>Send /stickers to find any sticker pack.</b>",

                reply_markup=keyboard,

                parse_mode=ParseMode.HTML,

            )

        elif e.message == "Peer_id_invalid" or "bot was blocked by the user":

            msg.reply_text(

                f"{context.bot.first_name} was blocked by you.",

                reply_markup=InlineKeyboardMarkup(

                    [

                        [

                            InlineKeyboardButton(

                                text="Unblock", url=f"t.me/{context.bot.username}"

                            )

                        ]

                    ]

                ),

            )

        elif e.message == "Internal Server Error: created sticker set not found (500)":

            msg.reply_text(

                "<b>Your Sticker Pack has been created!</b>"

                "\n\nYou can now reply to images, stickers and animated sticker with /steal to add them to your pack"

                "\n\n<b>Send /stickers to find sticker pack.</b>",

                reply_markup=keyboard,

                parse_mode=ParseMode.HTML,

            )

        return



    if success:

        msg.reply_text(

            "<b>Your Sticker Pack has been created!</b>"

            "\n\nYou can now reply to images, stickers and animated sticker with /steal to add them to your pack"

            "\n\n<b>Send /stickers to find sticker pack.</b>",

            reply_markup=keyboard,

            parse_mode=ParseMode.HTML,

        )

    else:

        msg.reply_text("Failed to create sticker pack. Possibly due to blek mejik.")





def getsticker(update: Update, context: CallbackContext):

    msg = update.effective_message

    chat_id = update.effective_chat.id

    if msg.reply_to_message and msg.reply_to_message.sticker:

        context.bot.sendChatAction(chat_id, "typing")

        update.effective_message.reply_text(

            "Hello"

            + f"{mention_html(msg.from_user.id, msg.from_user.first_name)}"

            + ", Please check the file you requested below."

            "\nPlease use this feature wisely!",

            parse_mode=ParseMode.HTML,

        )

        context.bot.sendChatAction(chat_id, "upload_document")

        file_id = msg.reply_to_message.sticker.file_id

        newFile = context.bot.get_file(file_id)

        newFile.download("sticker.png")

        context.bot.sendDocument(chat_id, document=open("sticker.png", "rb"))

        context.bot.sendChatAction(chat_id, "upload_photo")

        context.bot.send_photo(chat_id, photo=open("sticker.png", "rb"))



    else:

        context.bot.sendChatAction(chat_id, "typing")

        update.effective_message.reply_text(

            "Hello"

            + f"{mention_html(msg.from_user.id, msg.from_user.first_name)}"

            + ", Please reply to sticker message to get sticker image",

            parse_mode=ParseMode.HTML,

        )





def cb_sticker(update: Update, context: CallbackContext):

    msg = update.effective_message

    split = msg.text.split(" ", 1)

    if len(split) == 1:

        msg.reply_text("Provide some name to search for pack.")

        return



    scraper = cloudscraper.create_scraper()

    text = scraper.get(combot_stickers_url + split[1]).text

    soup = bs(text, "lxml")

    results = soup.find_all("a", {"class": "sticker-pack__btn"})

    titles = soup.find_all("div", "sticker-pack__title")

    if not results:

        msg.reply_text("No results found :(.")

        return

    reply = f"Stickers for *{split[1]}* :"

    for result, title in zip(results, titles):

        link = result["href"]

        reply += f"\nâ¥ [{title.get_text()}]({link})"

    msg.reply_text(reply, parse_mode=ParseMode.MARKDOWN)





def getsticker(update: Update, context: CallbackContext):

    bot = context.bot

    msg = update.effective_message

    chat_id = update.effective_chat.id

    if msg.reply_to_message and msg.reply_to_message.sticker:

        file_id = msg.reply_to_message.sticker.file_id

        new_file = bot.get_file(file_id)

        new_file.download("sticker.png")

        bot.send_document(chat_id, document=open("sticker.png", "rb"))

        os.remove("sticker.png")

    else:

        update.effective_message.reply_text(

            "Please reply to a sticker for me to upload its PNG."

        )





def delsticker(update: Update, context: CallbackContext):

    msg = update.effective_message

    if msg.reply_to_message and msg.reply_to_message.sticker:

        file_id = msg.reply_to_message.sticker.file_id

        context.bot.delete_sticker_from_set(file_id)

        msg.reply_text("Deleted!")

    else:

        update.effective_message.reply_text(

            "Please reply to sticker message to del sticker"

        )





def add_fvrtsticker(update: Update, context: CallbackContext):

    bot = context.bot

    message = update.effective_message

    chat = update.effective_chat

    user = update.effective_user

    args = context.args

    query = " ".join(args)

    if message.reply_to_message and message.reply_to_message.sticker:

        get_s_name = message.reply_to_message.sticker.set_name

        if not query:

            get_s_name_title = get_s_name

        else:

            get_s_name_title = query

        if get_s_name is None:

            message.reply_text("Sticker is invalid!")

        sticker_url = f"https://t.me/addstickers/{get_s_name}"

        sticker_m = "<a href='{}'>{}</a>".format(sticker_url, get_s_name_title)

        check_pack = REDIS.hexists(f"fvrt_stickers2_{user.id}", get_s_name_title)

        if check_pack is False:

            REDIS.hset(f"fvrt_stickers2_{user.id}", get_s_name_title, sticker_m)

            message.reply_text(

                f"<code>{sticker_m}</code> has been succesfully added into your favorite sticker packs list!",

                parse_mode=ParseMode.HTML,

            )

        else:

            message.reply_text(

                f"<code>{sticker_m}</code> is already exist in your favorite sticker packs list!",

                parse_mode=ParseMode.HTML,

            )



    else:

        message.reply_text("Reply to any sticker!")





def list_fvrtsticker(update: Update, context: CallbackContext):

    message = update.effective_message

    chat = update.effective_chat

    user = update.effective_user

    fvrt_stickers_list = REDIS.hvals(f"fvrt_stickers2_{user.id}")

    fvrt_stickers_list.sort()

    fvrt_stickers_list = "\nâ¢ ".join(fvrt_stickers_list)

    if fvrt_stickers_list:

        message.reply_text(

            "{}'s favorite sticker packs:\nâ¢ {}".format(

                user.first_name, fvrt_stickers_list

            ),

            parse_mode=ParseMode.HTML,

        )

    else:

        message.reply_text("You haven't added any sticker yet.")





def remove_fvrtsticker(update: Update, context: CallbackContext):

    message = update.effective_message

    chat = update.effective_chat

    user = update.effective_user

    args = context.args

    del_stick = " ".join(args)

    if not del_stick:

        message.reply_text(

            "Please give a your favorite sticker pack name to remove from your list."

        )

        return

    del_check = REDIS.hexists(f"fvrt_stickers2_{user.id}", del_stick)

    if not del_check is False:

        REDIS.hdel(f"fvrt_stickers2_{user.id}", del_stick)

        message.reply_text(

            f"<code>{del_stick}</code> has been succesfully deleted from your list.",

            parse_mode=ParseMode.HTML,

        )

    else:

        message.reply_text(

            f"<code>{del_stick}</code> doesn't exist in your favorite sticker pack list.",

            parse_mode=ParseMode.HTML,

        )





# __help__ = """

# *Stickers made easy with stickers module!*

# â¥ /stickers: Find stickers for given term on combot sticker catalogue 

# â¥ /steal or /kang: Reply to a sticker to add it to your pack.

# â¥ /remove: Reply to your anime exist sticker to your pack to delete it.

# â¥ /stickerid: Reply to a sticker to me to tell you its file ID.

# â¥ /getsticker: Reply to a sticker to me to upload its raw PNG file.

# â¥ /mmf : Memeify any sticker and image.

# â¥ /addfsticker or /afs <custom name>: Reply to a sticker to add it into your favorite pack list.

# â¥ /myfsticker or /mfs: Get list of your favorite packs.

# â¥ /removefsticker or /rfs <custom name>: Reply to a sticker to remove it into your favorite pack list.

# *Example:* `/addfstickers Alicia`

# """



__mod_name__ = "Sticker"

KANG_HANDLER = DisableAbleCommandHandler(["steal", "kang"], kang, pass_args=True, run_async=True)

DEL_HANDLER = DisableAbleCommandHandler("remove", "delsticker", run_async=True)

STICKERID_HANDLER = DisableAbleCommandHandler("stickerid", stickerid, run_async=True)

ADD_FSTICKER_HANDLER = DisableAbleCommandHandler(

    ["addfsticker", "afs"], add_fvrtsticker, pass_args=True, run_async=True

)

REMOVE_FSTICKER_HANDLER = DisableAbleCommandHandler(

    ["removefsticker", "rfs"], remove_fvrtsticker, pass_args=True, run_async=True

)

MY_FSTICKERS_HANDLER = DisableAbleCommandHandler(

    ["myfsticker", "mfs"], list_fvrtsticker, run_async=True

)

GETSTICKER_HANDLER = DisableAbleCommandHandler("getsticker", getsticker, run_async=True)

FIND_STICKERS_HANDLER = DisableAbleCommandHandler(

    "stickers", cb_sticker, run_async=True

)



dispatcher.add_handler(KANG_HANDLER)

dispatcher.add_handler(DEL_HANDLER)

dispatcher.add_handler(STICKERID_HANDLER)

dispatcher.add_handler(ADD_FSTICKER_HANDLER)

dispatcher.add_handler(REMOVE_FSTICKER_HANDLER)

dispatcher.add_handler(MY_FSTICKERS_HANDLER)

dispatcher.add_handler(GETSTICKER_HANDLER)

dispatcher.add_handler(FIND_STICKERS_HANDLER)
