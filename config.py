from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("23251665"))
API_HASH = getenv("40a41efd69f47b26790ea393477ffc01")

BOT_TOKEN = getenv("6973314741:AAFj6KH6oeOPFF6C8msyXpWzLp3qMvjmK28", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6760626015"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/de5ca0272c622c2bcb226.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/RobinxMusicChat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RobinxMusicNews")

SUDO_USERS = list(map(int, getenv("6619405270").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
