from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("28011815"))
API_HASH = getenv("9c2670fc7ace6211d8c237a309a96bfb")

BOT_TOKEN = getenv("8079418891:AAHAi3OMfcJVHBzkwB1U14U6wlb5kL8dGyc", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "190"))

OWNER_ID = int(getenv("7770816455"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/a9a2d183286bf143a4a6e-48b9814b2dcf67d2f5.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/5b94a782999c13a8c1ba5-4aa720053cecaa5050.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7770816455").split()))


FAILED = "https://graph.org/file/9bed950a923860af1da64-92218b6b21eb47b1dc.jpg"
