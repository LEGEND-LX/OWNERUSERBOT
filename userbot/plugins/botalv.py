from telethon import version

from userbot import *
from userbot.cmdhelp import CmdHelp
from userbot.utils import *

# -------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

legend = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={legend})"


PM_IMG = "https://te.legra.ph/file/fef2d78da4110fbf98a2e.jpg"
pm_caption = "**DARGONROαΊOOβοΈ πΈπ πΎπππππ**\n\n"

pm_caption += f"**βπ₯βtΝαΊΜΈDragonRoαΊooβοΈtπ₯β**\n"
pm_caption += f"**β£.ΫΫπ²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π πΌπ’ πΌπππππ    : {mention}**\n"
pm_caption += f"**β£.ΫΫπ²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π ππππππππ : `{version.__version__}`**\n"
pm_caption += f"**β£.ΫΫπ²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­πDragonRoαΊooβοΈ : {LEGENDversion}**\n"
pm_caption += f"**β£.ΫΫπ²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π ππππ     : `{sudou}`**\n"
pm_caption += f"**β£.ΫΫπ²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π²­π πΎπ πππ     : [ππΙ ΓͺΙ³ΜD](https://t.me/DARK_LEGEND_PRO)**\n"
pm_caption += f"**β[β¦οΈπΆππππβ¦οΈ](https://t.me/DragonPro_Userbot)β**\n"

pm_caption += "β[ππΙ ΓͺΙ³ΜD ~ Pro](github.com/DARK-LEGEND-PRO)β"


@bot.on(admin_cmd(outgoing=True, pattern="bot$"))
@bot.on(sudo_cmd(pattern="bot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alv").add_command(
    "alive", None, "Check weather the bot is alive or not"
).add_command(
    "bot",
    None,
    "Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg",
).add_warning(
    "Harmless Module"
).add_info(
    "Are u alive?"
).add_type(
    "Official"
).add()
