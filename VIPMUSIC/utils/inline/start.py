from pyrogram.types import InlineKeyboardButton

import config
from config import SUPPORT_GROUP
from VIPMUSIC import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀𝙳𝙳 𝙼𝙴 𝙸𝙽 𝙽𝙴𝚆 𝙶𝚁𝙾𝚄𝙿𝚂",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text=" 𝐇𝙴𝙻𝙿 ", callback_data="settings_back_helper"),
            InlineKeyboardButton(text=" 𝐒ҽƚƚιɳɠ𝐒", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="", url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀𝙳𝙳 𝙼𝙴 𝙸𝙽 𝙽𝙴𝚆 𝙶𝚁𝙾𝚄𝙿𝚂",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="𝐒ҽƚƚιɳɠ𝐒", callback_data="settings_back_helper"
            )
        ],
        [
                InlineKeyboardButton(
                text="❰𝐏𝐑𝐎𝐌𝐎𝐓𝐈𝐎𝐍 𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄❱",
                url=f"https:/https://t.me/TG_NAME_STYLE/4602",
            )
        ],
    ]
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✿︎ ᴀᴅᴅ ᴍᴇ ✿︎", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
        ],
    ]
    return buttons
    
