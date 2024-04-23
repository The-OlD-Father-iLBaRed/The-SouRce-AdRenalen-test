import asyncio
import os
import shutil
import socket
from datetime import datetime
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import filters
import config
from iLBaReD import app
from iLBaReD.misc import HAPP, SUDOERS, XCB
from iLBaReD.utils.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from iLBaReD.utils.decorators.language import language
from iLBaReD.utils.pastebin import OmarBin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()


@app.on_message(filters.command(["السجل","السجلات""سجل"],"")) 
@app.on_message(filters.command(["getlog", "logs", "getlogs"]) & SUDOERS)
@language
async def log_(client, message, _):
    try:
        await message.reply_document(document="log.txt")
    except:
        await message.reply_text(_["server_1"])
