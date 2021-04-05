# Copyright (C) 2020 TeamUltroid
# Recode by @mrismanaziz
# @sharinguserbot

import os
import cv2
from userbot.events import register
from userbot import CMD_HELP, bot

@register(outgoing=True, pattern="^.circle(?: |$)(.*)", disable_errors=True)
async def _(e):
    a = await e.get_reply_message()
    if a is None:
        return await eor(e, "Reply to a gif or audio")
    if a.document and a.document.mime_type == "audio/mpeg":
        z = await eor(e, "`Processing...`")
        toime = time.time()
        try:
            bbbb = await a.download_media(thumb=-1)
            im = cv2.imread(bbbb)
            dsize = (320, 320)
            output = cv2.resize(im, dsize, interpolation=cv2.INTER_AREA)
            cv2.imwrite("img.png", output)
            thumb = "img.png"
        except TypeError:
            thumb = ".resources/man_blank.png"
        c = await a.download_media(
            "resources/downloads/",
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, z, toime, "`Downloading...`")
            ),
        )
        await z.edit("`Sedang Mendownload...\nSaatnya Mengconvert...`")
        cmd = [
            "ffmpeg",
            "-i",
            c,
            "-acodec",
            "libmp3lame",
            "-ac",
            "2",
            "-ab",
            "144k",
            "-ar",
            "44100",
            "comp.mp3",
        ]
        proess = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proess.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
        mcd = [
            "ffmpeg",
            "-y",
            "-i",
            thumb,
            "-i",
            "comp.mp3",
            "-c:a",
            "copy",
            "circle.mp4",
        ]
        process = await asyncio.create_subprocess_exec(
            *mcd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
        taime = time.time()
        await e.client.send_file(
            e.chat_id,
            "circle.mp4",
            thumb=thumb,
            video_note=True,
            reply_to=a,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, z, taime, "`Sedang Mengupload...`")
            ),
        )
        await z.delete()
        os.system("rm resources/downloads/*")
        os.system("rm circle.mp4 comp.mp3 img.png")
        os.remove(bbbb)
    elif a.document and a.document.mime_type == "video/mp4":
        z = await eor(e, "`Membuat Video Note..`")
        c = await a.download_media("resources/downloads/")
        await e.client.send_file(e.chat_id, c, video_note=True, reply_to=a)
        await z.delete()
        os.remove(c)
    else:
        return await eor(e, "`Reply to a gif or audio file only`")

CMD_HELP.update(
    {
        "circle": "`.circle <reply video>`\
    \nUsage: Untuk mengubah video ukuran persegi menjadi Bulan seperti video message."
    }
)
