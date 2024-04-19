from iLBaReD.core.bot import Omar
from iLBaReD.core.dir import dirr
from iLBaReD.core.git import git
from iLBaReD.core.userbot import Userbot
from iLBaReD.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Omar()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
