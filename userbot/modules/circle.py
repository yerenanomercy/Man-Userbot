# Recode by @mrismanaziz
# @sharinguserbot
# t.me/sharinguserbot

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import CMD_HELP

@register(outgoing=True, pattern=".circle ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "Reply to any user message")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "Balas ke pesan media")
        return
    chat = "@TelescopyBot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "Reply to actual users message.")
        return
    await event.edit("Trying to convert...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```unblock @TelescopyBot dan coba lagi```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```Bisakah Master menonaktifkan pengaturan privasi forward pesan untuk selamanya?```"
            )
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message.media,)
            await event.client.send_read_acknowledge(conv.chat_id)

CMD_HELP.update(
    {
        "circle": "`.circle <reply video>`\
    \nUsage: Untuk mengubah video ukuran persegi menjadi Bulan seperti video message."
    })
