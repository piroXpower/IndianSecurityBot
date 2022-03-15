from TeamIndia.functions.stickers import *



__mod_name__ = "Stickers"

__help__ = "Click on below buttons and get information about stickers commands."

__button__ = [ InlineKeyboardButton(text="Sticker", callback_data="indiasticker_"),
            InlineKeyboardButton(text="Transform", callback_data="indiastickertransform_"),
            InlineKeyboardButton(text="DocPic", callback_data="indiastickerdpic_"),
            

] 
__buttons__ = [InlineKeyboardButton(text="Make Stickers", callback_data="indiastickermemify_"), 
             
 
]



dispatcher.add_handler(sticker_callback_handler)
dispatcher.add_handler(sticker_memify_callback_handler)
dispatcher.add_handler(sticker_transform_callback_handler)
dispatcher.add_handler(sticker_dpic_callback_handler)
