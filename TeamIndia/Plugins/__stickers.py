from AliciaRobot.functions.stickers import *



__mod_name__ = "Stickers"

__help__ = """We promise to keep you latest up-date with the latest technology on telegram. 
we updradge alicia everyday to simplifie use of telegram and give a better exprince to users.

Click on below buttons and get information about stickers commands.

"""
__button__ = [ InlineKeyboardButton(text="Sticker", callback_data="aliciasticker_"),
            InlineKeyboardButton(text="Transform", callback_data="aliciastickertransform_"),
            InlineKeyboardButton(text="DocPic", callback_data="aliciastickerdpic_"),
            

] 
__buttons__ = [InlineKeyboardButton(text="Make Stickers", callback_data="aliciastickermemify_"), 
             
 
]



dispatcher.add_handler(sticker_callback_handler)
dispatcher.add_handler(sticker_memify_callback_handler)
dispatcher.add_handler(sticker_transform_callback_handler)
dispatcher.add_handler(sticker_dpic_callback_handler)
