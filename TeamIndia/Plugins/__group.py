from TeamIndia.functions.group import *



__mod_name__ = "Group"

__help__ = "Click on below buttons and check amazing group for group."

__button__ = [ InlineKeyboardButton(text="Backup", callback_data="indiagroup_"),
            InlineKeyboardButton(text="Blacklist", callback_data="indiagroupbl_"),
            InlineKeyboardButton(text="F-Sub", callback_data="indiagroupfsub_"),

] 
__buttons__ = [InlineKeyboardButton(text="Control", callback_data="indiagroupcontrol_"), 
              InlineKeyboardButton(text="Disable", callback_data="indiagroupdisable_"),
              InlineKeyboardButton(text="Nightmode", callback_data="indiagroupnmode_"),
]



dispatcher.add_handler(group_callback_handler)
dispatcher.add_handler(group_bl_callback_handler)
dispatcher.add_handler(group_fsub_callback_handler)
dispatcher.add_handler(group_control_callback_handler)
dispatcher.add_handler(group_disable_callback_handler)
dispatcher.add_handler(group_nmode_callback_handler)
