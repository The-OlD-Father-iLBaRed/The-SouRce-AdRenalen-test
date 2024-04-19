from iLBaReD.core.bot import Omar
from iLBaReD.core.dir import dirr
from iLBaReD.core.git import git
from iLBaReD.core.userbot import Userbot
from iLBaReD.misc import dbb, heroku, sudo
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = Omar()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

async def joinch(message):
    if not message.from_user: return
    try:
            await message._client.get_chat_member("WA_AdRenalen", message.from_user.id)
    except UserNotParticipant:
                await message.reply(
                    f"🚦 يجب ان تشترك في القناة\n\nقنـاة الـبـوت : « https://t.me/WA_AdRenalen »",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("اضـغط هنا للأشتـراك القنـاة ", url=f"https://t.me/WA_AdRenalen"),
                            ],
                         ] 
                      ) 
                   )
                return True
    except:
        pass
        
