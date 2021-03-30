# Recode by @mrismanaziz
# @sharinguserbot

from os import remove
from random import choice
from urllib import parse

import requests

from userbot import CMD_HELP
from userbot.events import register

BASE_URL = "https://headp.at/pats/{}"
PAT_IMAGE = "pat.jpg"


@register(outgoing=True, pattern=".pat ?(.*)")
async def lastfm(event):
    if event.fwd_from:
        return
    username = event.pattern_match.group(1)
    if not username and not event.reply_to_msg_id:
        await edit_or_reply(event, "`Reply to a message or provide username`")
        return

    resp = requests.get("http://headp.at/js/pats.json")
    pats = resp.json()
    pat = BASE_URL.format(parse.quote(choice(pats)))
    await event.delete()
    with open(PAT_IMAGE, "wb") as f:
        f.write(requests.get(pat).content)
    if username:
        await borg.send_file(event.chat_id, PAT_IMAGE, caption=username)
    else:
        await borg.send_file(event.chat_id, PAT_IMAGE, reply_to=event.reply_to_msg_id)
    remove(PAT_IMAGE)


CMD_HELP.update({
    "pat":
    "`.pat` <reply msg>\
        \nUsage: Gives the replied user a pat"
})
