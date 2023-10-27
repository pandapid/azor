#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, USOW, USCH
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Owner:</b> {USOW}\n\n<b>○ Language :</b> <code>Python3</code>\n\n<b>○ Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n\n<b>○ Channel :</b> {USCH}\n\n<b>○ Support :</b> @impidbot",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
