# Kang with Credits for Dark_Cobra
# Recode by @mrismanaziz
# @sharinguserbot

from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from userbot.events import 
from userbot import bot, CMD_HELP


@register(outgoing=True, pattern="^.allban ?(.*)", disable_errors=True)
async def testing(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("𝗬𝗢𝗨 𝗗𝗜𝗗𝗡𝗧 𝗛𝗔𝗩𝗘 𝗦𝗨𝗙𝗙𝗜𝗖𝗜𝗘𝗡𝗧 𝗥𝗜𝗚𝗛𝗧𝗦")
        return
    await event.edit("Doing Nothing 🙃🙂")

    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
        except Exception as e:
            await event.edit(str(e))
        await sleep(.5)
    await event.edit("Nothing Happend here🙃🙂")

CMD_HELP.update(
    {
        "allban": "**Plugin : **`allban`\
    \n\n**Syntax : **`.allban`\
    \n**Function : **Banned semua member dengan 1 cmd"
    }
)
