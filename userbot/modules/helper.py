""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.ihelp$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/mrismanaziz)"
        "\n[Repo](https://github.com/mrismanaziz/Man-Userbot)"
        "\n[Instagram](Instagram.com/mrismanaziz_)")


@register(outgoing=True, pattern="^.listvar$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/mrismanaziz/Man-Userbot/Man-Userbot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "`.ihelp`\
\nUsage: Bantuan Untuk Lord-Userbot.\
\n`.listvar`\
\nUsage: Melihat Daftar Vars."
})
