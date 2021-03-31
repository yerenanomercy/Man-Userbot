# Recode by @mrismanaziz
# @sharinguserbot
# t.me/sharinguserbot

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import CMD_HELP, bot, TEMP_DOWNLOAD_DIRECTORY

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
            await event.edit("```Nonaktifkan pengaturan privasi forward```")
        else:
                downloaded_file_name = await event.client.download_media(
                response.media, TEMP_DOWNLOAD_DIRECTORY
            )
            await event.client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply,
            )
            """ - cleanup chat after completed - """
            if msg_reply is not None:
                await event.client.delete_messages(
                    conv.chat_id, [msg.id, msg_reply.id, r.id, response.id]
                )
            else:
                await event.client.delete_messages(conv.chat_id, [msg.id, response.id])
    await event.delete()
    return os.remove(downloaded_file_name)

CMD_HELP.update(
    {
        "circle": "`.circle <reply video>`\
    \nUsage: Untuk mengubah video ukuran persegi menjadi Bulan seperti video message."
    })
