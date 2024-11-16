from pyrogram import Client, filters
import asyncio
from Mangandi import ImageUploader, VideoUploader
import logging
from pyrogram import enums

FORMAT = "[IMAGE URL]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
                                                    logging.StreamHandler()], format=FORMAT)




Imageu = Client(
    name = "imageurl",
    api_id = 19042248,
    api_hash = "a1d443cb79941a89c493f22abf4f84cb",
    bot_token = "7749319524:AAFy5ulFuIpbBoiHfO7ggHO2Ck86z1t8Rrk"
)

@Imageu.on_message(filters.command("start"))
async def start_cmd(client, msg):
    await msg.reply("<pre>Send me any image, video mp4 only, animation, sticker.</pre>\nI give a url of pic")

@Imageu.on_message(filters.incoming & filters.photo)
async def test(client,message):
    
    msg = await message.reply("ɢᴇᴛᴛɪɴɢ ʟɪɴᴋ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs ...")
    
    
    k = await message.download()
    up = ImageUploader(k)
    link = up.upload()
    await msg.edit(link)

@Imageu.on_message(filters.incoming & filters.sticker)
async def sticker(client, message):
    msg = await message.reply("ɢᴇᴛᴛɪɴɢ ʟɪɴᴋ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs ...")
    
    k = await message.download()
    up = ImageUploader(k)
    link = up.upload()
    await msg.edit(link)

@Imageu.on_message(filters.incoming & filters.video)
async def video(client, message):
    msg = await message.reply("ɢᴇᴛᴛɪɴɢ ʟɪɴᴋ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs ...")
    k = await message.download()
    up = VideoUploader(k)
    link = up.upload()
    await msg.edit(link)



@Siva.on_message(filters.incoming & filters.animation)
async def animation(client, message):
    msg = await message.reply("ɢᴇᴛᴛɪɴɢ ʟɪɴᴋ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs ...")
    
    k = await message.download()
    up = VideoUploader(k)
    link = up.upload()
    await msg.edit(link)

@Imageu.on_message(filters.incoming & filters.text & filters.private)
async def ntext(client, message):
    await message.reply("<pre>Send me a sticker, video(mp4), photo, gif</pre>")










Imageu.run()



    
