# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from pyrogram import Client as ren
from pyrogram import *
from pyrogram.types import *

@ren.on_message(filters.command("start") & filters.private)
async def start_bot(c: Client, m: Message):
    start_welcome = f"Hallo Cok ! {m.from_user.mention}\n\nTanya Apapun Bebas Asal Gak Bahas Agama, Ras, Suku Atau Tak Bal Ndasmu 😠.\n\nPaham Ra Cok??\n\nContoh : `/tanya membuat anak`"
    start_button = InlineKeyboardMarkup([[InlineKeyboardButton("Join Grub Ku Cok", url=f"https://t.me/internetgratishoax?startgroup=True")]])
    await m.reply_text(start_welcome, reply_markup=start_button)
