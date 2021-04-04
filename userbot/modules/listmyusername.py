# Recode by @mrismanaziz
# @sharinguserbot

from userbot.events import register
from userbot import CMD_HELP
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest


@register(outgoing=True, pattern=".listmyusername ?(.*)")
async def mine(event):
    """ For .reserved command, get a list of your reserved usernames. """
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)


CMD_HELP.update(
    {
        "LIST MY USERNAMES": "**Plugin : **`listmyusernames`\
    \n\n**Syntax : **`.listmyusername`\
    \n**Function : **this plugin give you your all channel and groups usernamen"
    }
)
