# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# Recode by @mrismanaziz
# @sharinguserbot

from telethon.tl import functions
from telethon.tl.types import (ChatBannedRights, UserStatusEmpty,
                               UserStatusLastMonth, UserStatusLastWeek,
                               UserStatusOffline, UserStatusOnline,
                               UserStatusRecently)

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=".rmusers ?(.*)")
async def _(event):
    xx = await eor(event, "`Searching Participant Lists...`")
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not (chat.admin_rights or chat.creator):
            return await eod(xx, "`Master Bukan admin Disini !`", time=5)
    p = 0
    b = 0
    c = 0
    d = 0
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    async for i in event.client.iter_participants(event.chat_id):
        p += 1
        rights = ChatBannedRights(
            until_date=None,
            view_messages=True,
        )
        if isinstance(i.status, UserStatusEmpty):
            y += 1
            if "empty" in input_str:
                try:
                    await event.client(
                        functions.channels.EditBannedRequest(event.chat_id, i, rights)
                    )
                    c += 1
                    y -= 1
                except BaseException:
                    pass
        if isinstance(i.status, UserStatusLastMonth):
            m += 1
            if "month" in input_str:
                try:
                    await event.client(
                        functions.channels.EditBannedRequest(event.chat_id, i, rights)
                    )
                    c += 1
                    m -= 1
                except BaseException:
                    pass
        if isinstance(i.status, UserStatusLastWeek):
            w += 1
            if "week" in input_str:
                try:
                    await event.client(
                        functions.channels.EditBannedRequest(event.chat_id, i, rights)
                    )
                    c += 1
                    w -= 1
                except BaseException:
                    pass
        if isinstance(i.status, UserStatusOffline):
            o += 1
            if "offline" in input_str:
                try:
                    await event.client(
                        functions.channels.EditBannedRequest(event.chat_id, i, rights)
                    )
                    c += 1
                    o -= 1
                except BaseException:
                    pass
        if isinstance(i.status, UserStatusOnline):
            q += 1
            if "online" in input_str:
                try:
                    await event.client(
                        functions.channels.EditBannedRequest(event.chat_id, i, rights)
                    )
                    c += 1
                    q -= 1
                except BaseException:
                    pass
        if isinstance(i.status, UserStatusRecently):
            r += 1
            if "recently" in input_str:
                try:
                    await event.client(
                        functions.channels.EditBannedRequest(event.chat_id, i, rights)
                    )
                    c += 1
                    r -= 1
                except BaseException:
                    pass
        if i.bot:
            b += 1
            if "bot" in input_str:
                try:
                    await event.client(
                        functions.channels.EditBannedRequest(event.chat_id, i, rights)
                    )
                    c += 1
                    b -= 1
                except BaseException:
                    pass
        elif i.deleted:
            d += 1
            if "deleted" in input_str:
                try:
                    await event.client(
                        functions.channels.EditBannedRequest(event.chat_id, i, rights)
                    )
                    c += 1
                    d -= 1
                except BaseException:
                    pass
        elif i.status is None:
            n += 1
            if "none" in input_str:
                try:
                    await event.client(
                        functions.channels.EditBannedRequest(event.chat_id, i, rights)
                    )
                    c += 1
                    n -= 1
                except BaseException:
                    pass
    required_string = ""
    if input_str:
        required_string += f"**>> Kicked** `{c} / {p}` **users**\n\n"
        required_string += f"  **••Deleted Accounts••** `{d}`\n"
        required_string += f"  **••UserStatusEmpty••** `{y}`\n"
        required_string += f"  **••UserStatusLastMonth••** `{m}`\n"
        required_string += f"  **••UserStatusLastWeek••** `{w}`\n"
        required_string += f"  **••UserStatusOffline••** `{o}`\n"
        required_string += f"  **••UserStatusOnline••** `{q}`\n"
        required_string += f"  **••UserStatusRecently••** `{r}`\n"
        required_string += f"  **••Bots••** `{b}`\n"
        required_string += f"  **••None••** `{n}`\n"
    else:
        required_string += f"**>> Total** `{p}` **users**\n\n"
        required_string += f"  `.rmusers deleted`  **••**  `{d}`\n"
        required_string += f"  `.rmusers empty`  **••**  `{y}`\n"
        required_string += f"  `.rmusers month`  **••**  `{m}`\n"
        required_string += f"  `.rmusers week`  **••**  `{w}`\n"
        required_string += f"  `.rmusers offline`  **••**  `{o}`\n"
        required_string += f"  `.rmusers online`  **••**  `{q}`\n"
        required_string += f"  `.rmusers recently`  **••**  `{r}`\n"
        required_string += f"  `.rmusers bot`  **••**  `{b}`\n"
        required_string += f"  `.rmusers none`  **••**  `{n}`\n\n"
        required_string += f"**••Empty**  `Name with deleted Account`\n"
        required_string += f"**••None**  `Last Seen A Long Time Ago`\n"
    await eod(xx, required_string)

CMD_HELP.update(
    {
        "bannedall": ".rmusers\
    \nUsage : Menghapus/Banned user dari grup dengan spesifik."
    })
