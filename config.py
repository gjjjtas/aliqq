## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgC-bkMjpYPcDlM0Mt5QmP-13mkvkVrhoiLiEEBFbONkDiMZmtSBPsUf701Zed9o1VagLZC3Aqqdx6gb208ezaJBAsVfgH6lTSUYH1YsRXBk4AYNCkY-2AWcDAezoHZIsdCo2tGNz4-_hXT8kyQN5rxJrg5dz14pA5HbUG3deZpNa8EUWe0lz7j2BGToft9wdA-ZJuE7uA5OX4_BQmaeY8ilX75k04vzTHzd8MnT67Y9hUkCinSSsmPfq618sC29NN0Yx-8lBp0UUHQgL2gfioPd9nJYVTa6tz3wFCuD2PJL02DO61WlaSkCtUB2g1xMfijDoqgNUUH2AcHJMofnI5qiAAAAAT3HOEYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5362302605:AAEsH55OYCXv-9Fl0KAueXPjo-cOqdzl_sU")
BOT_NAME = getenv("BOT_NAME", "𝐌𝗨𝐒𝐈𝐂 𝐋𝐑𝐀𝐐")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "𝐌𝗨𝐒𝐈𝐂 𝐋𝐑𝐀𝐐")
OWNER_USERNAME = getenv("OWNER_USERNAME", "KKTTO")
ALIVE_NAME = getenv("ALIVE_NAME", "𝐌𝗨𝐒𝐈𝐂 𝐋𝐑𝐀𝐐")
BOT_USERNAME = getenv("BOT_USERNAME", "meyzekbot")
OWNER_ID = getenv("OWNER_ID", "2044554138")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "PQTQP")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "nanhhs")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "nanhhs")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2044554138").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/589249a3327aaf595aa13.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/1a3b1c922a8a3d5c7a578.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
