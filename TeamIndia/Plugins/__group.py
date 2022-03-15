from AliciaRobot.functions.group import *



__mod_name__ = "Group"

__help__ = """We promise to keep you latest up-date with the latest technology on telegram. 
we updradge alicia everyday to simplifie use of telegram and give a better exprince to users.

Click on below buttons and check amazing group for group.

"""
__button__ = [ InlineKeyboardButton(text="Backup", callback_data="aliciagroup_"),
            InlineKeyboardButton(text="Blacklist", callback_data="aliciagroupbl_"),
            InlineKeyboardButton(text="F-Sub", callback_data="aliciagroupfsub_"),

] 
__buttons__ = [InlineKeyboardButton(text="Control", callback_data="aliciagroupcontrol_"), 
              InlineKeyboardButton(text="Disable", callback_data="aliciagroupdisable_"),
              InlineKeyboardButton(text="Nightmode", callback_data="aliciagroupnmode_"),
]



dispatcher.add_handler(group_callback_handler)
dispatcher.add_handler(group_bl_callback_handler)
dispatcher.add_handler(group_fsub_callback_handler)
dispatcher.add_handler(group_control_callback_handler)
dispatcher.add_handler(group_disable_callback_handler)
dispatcher.add_handler(group_nmode_callback_handler)