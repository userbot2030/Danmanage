from RitoRobot.config import CHANNEL
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def join_channel(bot: Client, msg: Message):
    if not CHANNEL:  
        return
    try:
        try:
            await bot.get_chat_member(CHANNEL, msg.from_user.id)
        except UserNotParticipant:
            if CHANNEL.isalpha():
                link = "https://t.me/" + CHANNEL
            else:
                chat_info = await bot.get_chat(CHANNEL)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"Kamu harus join channel dibawah ini sebelum menggunakan saya. Setelah join coba lagi klik /start",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("JOIN CHANNEL", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Kamu bukan admin!")
