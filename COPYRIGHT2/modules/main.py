from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters
from pyrogram.types import Message
import time
import psutil
import platform
import logging
from config import OWNER_ID, BOT_USERNAME
from config import *
from COPYRIGHT2 import COPYRIGHT2 as app

import pyrogram
from pyrogram.errors import FloodWait


# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------


start_txt = """<b> 🤖 ˹ Cᴏᴘʏʀɪɢʜᴛ ✘ Rᴇᴍᴏᴠᴇʀ ˼ 🛡️ </b>

👋 I'm your 𝗧ᴇ𝘅ᴛ 𝗧ᴇʀᴍɪɴᴀᴛᴏʀ , here to maintain a secure environment for our discussions.

🚫 𝗘𝗱𝗶𝘁𝗲𝗱 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗗𝗲𝗹𝗲𝘁𝗶𝗼𝗻: 𝗜'𝗹𝗹 𝗿𝗲𝗺𝗼𝘃𝗲 𝗲𝗱𝗶𝘁𝗲𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝘁𝗼 𝗺𝗮𝗶𝗻𝘁𝗮𝗶𝗻 𝘁𝗿𝗮𝗻𝘀𝗽𝗮𝗿𝗲𝗻𝗰𝘆.

📣 𝗡𝗼𝘁𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻𝘀: 𝗬𝗼𝘂'𝗹𝗹 𝗯𝗲 𝗶𝗻𝗳𝗼𝗿𝗺𝗲𝗱 𝗲𝗮𝗰𝘁𝗶𝗺𝗲 𝘁𝗶𝗺𝗲 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗶𝘀 𝗱𝗲𝗹𝗲𝘁𝗲𝗱.

🌟 𝗚𝗲𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱:
1. Add me to your group.
2. I'll start protecting instantly.

➡️ Click on 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 to add me and keep our group safe ⚡"""

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴀɴᴅʟᴇʀ •", callback_data="dil_back")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/d5d23e541737366550aef.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


gd_buttons = [              
        [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER_ID),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/GAURAV_BOTS"),    
        ]
        ]


# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("dil_back"))
async def dil_back(_, query: CallbackQuery):
    await query.message.edit_caption(start_txt,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"



@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)


    
# -------------------------------------------------------------------------------------



FORBIDDEN_KEYWORDS = ["porn", "mitochondria" , "chemistry" , "velocity" , "modular" , "akash" , "physics" , "pwd" , "water" , "test series" , "minor" , "major" , "jee" , "neet" , "upse" , "bio" , "xxx", "sex", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt" "Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓙ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ','Ⓟ', 'Ⓠ', 'Ⓡ', 'Ⓢ', 'Ⓣ','Ⓤ','Ⓥ', 'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⓪','🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞','🅟', '🅠', '🅡', '🅢', '🅣','🅤','🅥', '🅦', '🅧', '🅨', '🅩', '❶', '❷', '❸', '❹', '❺', '❻', '❼', '❽', '❾', '⓿','𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎','𝐏', '𝐐', '𝐑', '𝐒', '𝐓','𝐔','𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗', '𝟎','𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕴', '𝕵', '𝕶', '𝕷', '𝕸', '𝕹', '𝕺','𝕻', '𝕼', '𝕽', '𝕾', '𝕿','𝖀','𝖁', '𝖂', '𝖃', '𝖄', '𝖅', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗', '𝟎','𝑨', '𝑩', '𝑪', '𝑫', '𝑬', '𝑭', '𝑮', '𝑯', '𝑰', '𝑱', '𝑲', '𝑳', '𝑴', '𝑵', '𝑶','𝑷', '𝑸', '𝑹', '𝑺', '𝑻','𝑼','𝑽', '𝑾', '𝑿', '𝒀', '𝒁', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗', '𝟎','𝓐', '𝓑', '𝓒', '𝓓', '𝓔', '𝓕', '𝓖', '𝓗', '𝓘', '𝓙', '𝓚', '𝓛', '𝓜', '𝓝', '𝓞','𝓟', '𝓠', '𝓡', '𝓢', '𝓣','𝓤','𝓥', '𝓦', '𝓧', '𝓨', '𝓩', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗', '𝟎','𝒜', '𝐵', '𝒞', '𝒟', '𝐸', '𝐹', '𝒢', '𝐻', '𝐼', '𝒥', '𝒦', '𝐿', '𝑀', '𝒩', '𝒪','𝒫', '𝒬', '𝑅', '𝒮', '𝒯','𝒰','𝒱', '𝒲', '𝒳', '𝒴', '𝒵','𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀', '𝕁', '𝕂', '𝕃', '𝕄', 'ℕ', '𝕆','ℙ', 'ℚ', 'ℝ', '𝕊', '𝕋','𝕌','𝕍', '𝕎', '𝕏', '𝕐', 'ℤ', '𝟙', '𝟚', '𝟛', '𝟜', '𝟝', '𝟞', '𝟟', '𝟠', '𝟡', '𝟘','𝙰', '𝙱', '𝙲', '𝙳', '𝙴', '𝙵', '𝙶', '𝙷', '𝙸', '𝙹', '𝙺', '𝙻', '𝙼', '𝙽', '𝙾','𝙿', '𝚀', '𝚁', '𝚂', '𝚃','𝚄','𝚅', '𝚆', '𝚇', '𝚈', '𝚉', '𝟷', '𝟸', '𝟹', '𝟺', '𝟻', '𝟼', '𝟽', '𝟾', '𝟿', '𝟶','𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢','𝗣', '𝗤', '𝗥', '𝗦', '𝗧','𝗨','𝗩', '𝗪', '𝗫', '𝗬', '𝗭', '𝟭', '𝟮', '𝟯', '𝟰', '𝟱', '𝟲', '𝟳', '𝟴', '𝟵', '𝟬','𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', '𝙄', '𝙅', '𝙆', '𝙇', '𝙈', '𝙉', '𝙊','𝙋', '𝙌', '𝙍', '𝙎', '𝙏','𝙐','𝙑', '𝙒', '𝙓', '𝙔', '𝙕', '𝟭', '𝟮', '𝟯', '𝟰', '𝟱', '𝟲', '𝟳', '𝟴', '𝟵', '𝟬','𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖','𝘗', '𝘘', '𝘙', '𝘚', '𝘛','𝘜','𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '𝟣', '𝟤', '𝟥', '𝟦', '𝟧', '𝟨', '𝟩', '𝟪', '𝟫', '𝟢','🄰', '🄱', '🄲', '🄳', '🄴', '🄵', '🄶', '🄷', '🄸', '🄹', '🄺', '🄻', '🄼', '🄽', '🄾','🄿', '🅀', '🅁', '🅂', '🅃','🅄','🅅', '🅆', '🅇', '🅈', '🅉','🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅼', '🅽', '🅾','🅿', '🆀', '🆁', '🆂', '🆃','🆄','🆅', '🆆', '🆇', '🆈', '🆉','🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴','🇵', '🇶', '🇷', '🇸', '🇹','🇺','🇻', '🇼', '🇽', '🇾', '🇿','𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒','𝔓', '𝔔', 'ℜ', '𝔖', '𝔗','𝔘','𝔙', '𝔚', '𝔛', '𝔜', 'ℨ','ₐ', 'ᵦ', '꜀', 'd', 'ₑ', 'f', '₉', 'ₕ', 'ᵢ', 'ⱼ', 'ₖ', 'ₗ', 'ₘ', 'ₙ', 'ₒ','ₚ', 'q', 'ᵣ', 'ₛ', 'ₜ','ᵤ','ᵥ', 'w', 'ₓ', 'ᵧ', '₂', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', '₀','ል', 'ጌ', 'ር', 'ዕ', 'ቿ', 'ቻ', 'ኗ', 'ዘ', 'ጎ', 'ጋ', 'ጕ', 'ረ', 'ጠ', 'ክ', 'ዐ','የ', 'ዒ', 'ዪ', 'ነ', 'ፕ','ሁ','ሀ', 'ሠ', 'ሸ', 'ሃ', 'ጊ', '˦', 'Ϩ', 'Յ', 'Ϥ', 'Ƽ', 'δ', '𐒇', 'ϐ', 'ƍ', 'θ','ﾑ', '乃', 'c', 'd', '乇', 'ｷ', 'g', 'ん', 'ﾉ', 'ﾌ', 'ズ', 'ﾚ', 'ﾶ', '刀', 'o','ｱ', 'q', '尺', '丂', 'ｲ','u','√', 'w', 'ﾒ', 'ﾘ', '乙', '⥑', 'ջ', 'ჳ', 'ʮ', 'ҕ', 'ϭ', '⁊', 'ზ', '𝚐', '○', '⓵', '⓶', '⓷', '⓸', '⓹', '⓺', '⓻', '⓼', '⓽','𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭', 'Ä̈', 'ß', 'Ç̧', 'Ð', 'È', '£', 'G', 'Ì', 'ñ', 'Ö', 'þ', 'Q', '§', '†', 'Ú', '×', 'Ɏ', 'α', 'Ⴆ', 'ƈ', 'ԃ', 'ҽ', 'ϝ', 'ɠ', 'ԋ', 'ι', 'ʝ', 'ƙ', 'ʅ', 'ɱ', 'ɳ', 'σ', 'ρ', 'ϙ', 'ɾ', 'ʂ', 'ƚ', 'υ', 'ʋ', 'ɯ', 'x', 'ყ', 'ȥ', '🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅼', '🅽', '🅾', '🅿', '🆀', '🆁', '🆂', '🆃', '🆄', '🆅', '🆆', '🆇', '🆈', '🆉', 'Ꭿ', 'Ᏸ', 'Ꮸ', 'Ꭰ', 'Ꭼ', 'Ꮀ', 'Ꮆ', 'Ꮋ', 'Ꭸ', 'Ꮰ', 'Ꮶ', 'Ꮭ', 'Ꮇ', 'Ꮑ', 'Ꮎ', 'Ꮲ', 'Ꮕ', 'Ꮢ', 'Ꮥ', 'Ꮏ', 'Ꮼ', 'Ꮙ', 'Ꮿ', 'Ꮂ', 'Ꮍ', 'Ꮓ', '🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤', '🅥', '🅦', '🅧', '🅨', '🅩', '𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒', '𝔓', '𝔔', 'ℜ', '𝔖', '𝔗', '𝔘', '𝔙', '𝔚', '𝔛', '𝔜', 'ℨ', '𝔤', '𝔥', '𝔦', '𝔧', '𝔨', '𝔩', '𝔪', '𝔫', '𝔬', '𝔭', '𝔮', '𝔯', '𝔰', '𝔱', '𝔲', '𝔳', '𝔴', '𝔵', '𝔶', '𝔷','ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ', 'ⓕ', 'ⓖ', 'ⓗ', 'ⓘ', 'ⓙ', 'ⓚ', 'ⓛ', 'ⓜ', 'ⓝ', 'ⓞ', 'ⓟ', 'ⓠ', 'ⓡ', 'ⓢ', 'ⓣ', 'ⓤ', 'ⓥ', 'ⓦ', 'ⓧ', 'ⓨ', 'ⓩ', 'Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓙ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ', 'Ⓟ', 'Ⓠ', 'Ⓡ', 'Ⓢ', 'Ⓣ', 'Ⓤ', 'Ⓥ', 'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', 'ł', 'J', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', 'Q', 'Ɽ', '₴', '₮', 'Ʉ', 'V', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', '𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', '𝘘', '𝘙', '𝘚', '𝘛', '𝘜', '𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '𝘢', '𝘣', '𝘤', '𝘥', '𝘦', '𝘧', '𝘨', '𝘩', '𝘪', '𝘫', '𝘬', '𝘭', '𝘮', '𝘯', '𝘰', '𝘱', '𝘲', '𝘳', '𝘴', '𝘵', '𝘶', '𝘷', '𝘸', '𝘹', '𝘺', '𝘻' ]

@app.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
      #  user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
       # user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
        
        
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()
    #  user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} just edited a message and i delete it 🤡🤡")



# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
def delete_long_messages(_, m):
    return len(m.text.split()) > 400

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"Hey {user_mention}, please keep your messages short!")
    

# -----------------------------------------------------------------------------------


    
@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
async def keep_reaction_message(client, message: Message):
    pass 
# -------------------------------

async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        warning_message = f"@{message.from_user.username} ᴍᴀᴀ ᴍᴀᴛ ᴄʜᴜᴅᴀ ᴘᴅғ ʙʜᴇᴊ ᴋᴇ,\n ʙʜᴏsᴀᴅɪᴋᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀɢʏᴇɢᴀ \n\n ᴅᴇʟᴇᴛᴇ ᴋᴀʀ ᴅɪʏᴀ ᴍᴀᴅᴀʀᴄʜᴏᴅ.\n\n ᴀʙ @iam_daxx ʙʜᴀɪ ᴋᴇ ᴅᴍ ᴍᴇ ᴀᴘɴɪ ᴍᴜᴍᴍʏ ᴋᴏ ʙʜᴇᴊ ᴅᴇ 🍌🍌🍌."
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)

# ----------------------------------------
