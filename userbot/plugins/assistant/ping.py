import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

LEGEND_IMG = os.environ.get(
    "BOT_PING_PIC", "https://te.legra.ph/file/fef2d78da4110fbf98a2e.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

LegendPro = f"**꧁•⊹٭RoBoot Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 RoBoot 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("⚜ DragonRoẞoo† ⚜", "https://t.me/LegendBot_Pros")]]
    await tgbot.send_file(event.chat_id, LEGEND_IMG, caption=LegendPro, buttons=GOOD)
