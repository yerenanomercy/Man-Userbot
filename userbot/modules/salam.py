from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamualaikum Dulu Biar Sopan**")


@register(outgoing=True, pattern="^.pe(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamualaikum Warahmatullahi Wabarakatuh**")


@register(outgoing=True, pattern="^.P(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Haii Salken Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("**Assalamualaikum...**")


@register(outgoing=True, pattern="^.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Wa'alaikumsalam**")


CMD_HELP.update(
    {
        "salam": "`.p`\
    \nMenampilkan: Assalamualaikum Dulu Biar Sopan.\
    \n\n`.P`\
    \nMenampilkan: salam Kenal dan salam.\
    \n\n`.pe`\
    \nMenampilkan: Untuk Memberi salam\
    \n\n`.l`\
    \nMenampilkan: Untuk Menjawab Salam.\
    \n\n`.ass`\
    \nMenampilkan: Salam Bahas arab\
    \n\n`.sayang`\
    \nMenampilkan: Kata I Love You.\
    \n\n`.semangat`\
    \nMenampilkan: Memberikan Semangat.\
    \n\n`.ywc`\
    \nMenampilkan: sama sama.\
    \n\n`.k`\
    \nMenampilkan: LU SEMUA NGENTOT 🔥\
    \n\n`.j`\
    \nMenampilkan: NIMBRUNG GOBLOKK!!!🔥"
    }
)
