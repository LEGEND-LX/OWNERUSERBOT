from telethon import events

from userbot import *

from . import *

PM_IMG = "https://te.legra.ph/file/fef2d78da4110fbf98a2e.jpg"
pm_caption = f"⚜『DragonRoẞoo†』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{legend_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `8.15.17` \n"
pm_caption += f"┣『DragonRoẞoo†』~ `{LEGENDversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/Pro_LegendBots)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/DARK-LEGEND-PRO/PRO-DRAGONSETUP/blob/master/LICENSE)\n"
pm_caption += f"┣Vps-Loader ~ By [『DragonRoẞoo†』 ](https://t.me/DragonPro_UserBot)\n"
pm_caption += f"┣Pro-Assistant ~ By [『Lêɠêɳ̃dPro』 ](https://t.me/DARK_LEGEND_PRO)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『DRAGONROẞOO†』](https://t.me/DragonPro_UserBot) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
