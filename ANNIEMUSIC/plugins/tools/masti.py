import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ANNIEMUSIC import app
from config import SUPPORT_CHAT

BUTTON = [[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"{SUPPORT_CHAT}")]]
GAMER = "https://telegra.ph/file/bdc5c8e6e9445a5d5068e.mp4"
HANDSOME = "https://telegra.ph/file/595799faee5acef0a00d2.mp4"
COOL = "https://telegra.ph/file/8e3a43b6f4929876e610e.mp4"
URUTTU = "https://telegra.ph/file/89088f3c128eec57720df.mp4"
KOLARU = "https://telegra.ph/file/798bcc26b68c2013e6e2a.mp4"
NO = "https://telegra.ph/file/26d3c7b5c3bbeb84f4382.mp4"
ACCEPTED = "https://telegra.ph/file/ba50a01bc7f4f7f20c6c1.mp4"
CUTIE = "https://graph.org/file/24375c6e54609c0e4621c.mp4"

####### masti
########  CUTE
@app.on_message(filters.command("cutie"))
async def cutie(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTIE = f"🍑 {mention} {mm}% 𐤠ȴ𐤠Ɠꓴꓴ 😍🥀"

    await app.send_document(
        chat_id=message.chat.id,
        document=CUTIE,
        caption=CUTIE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )
    
###### horny

@app.on_message(filters.command("handsome"))
async def handsome(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    HANDSOME = f"🔥 {mention} ɪꜱ {mm} % Gentleman da nee! 🔥"

    await app.send_document(
        chat_id=message.chat.id,
        document=HANDSOME,
        caption=HANDSOME,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )

###### HOT 

@app.on_message(filters.command("gamer"))
async def gamer(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    GAMER = f"Nee {mention} yeppo {mm}% da gamer aane!"

    await app.send_document(
        chat_id=message.chat.id,
        document=GAMER,
        caption=GAMER,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )

########## SEXY 

@app.on_message(filters.command("cool"))
async def cool(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    SEXO = f" 🤟 {mention} ɪꜱ {mm}% ❀ ƇΘΘȴ ❀!"
    await app.send_document (
        chat_id=message.chat.id,
        document=COOL,
        caption=COOL,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

#########gay
@app.on_message(filters.command("kolaru"))
async def kolaru(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    KOLARU = f" 🍷 {mention} ɪꜱ {mm}%  𝐊𝐨𝐥𝐚𝐫𝐮 !"
    await app.send_document (
        chat_id=message.chat.id,
        document=KOLARU,
        caption=KOLARU,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

########### LESBIAN
@app.on_message(filters.command("uruttu"))
async def uruttu(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    URUTTU = f" 🫣 {mention} ɪꜱ {mm}% υяяυтυ!"
    await app.send_document (
        chat_id=message.chat.id,
        document=URUTTU,
        caption=URUTTU,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

########### BOOBS

@app.on_message(filters.command("no"))
async def no(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    NO = f"  {mention}ꜱ  {mm} ! "
    await app.send_document (
        chat_id=message.chat.id,
        document=NO,
        caption=NO,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

######### COCK

@app.on_message(filters.command("accepted"))
async def accepted(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    ACCEPTED = f"  {mention} Meow Meow {mm} 𝙈𝙖𝙩𝙘𝙝 🐈"
    await app.send_document (
        chat_id=message.chat.id,
        document=ACCEPTED,
        caption=ACCEPTED,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)
