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

SESSION = getenv("BQGrbScAofmC2OF8BOU35cFYUmuvIWK8DsGOwRzFd4AskV32AD-6KP_akyasyNpfbkSK8QoxMQCEJ1B_usHoJ5rd97tqVtYrR8pvZWhezi0PXow8YeKbCUUsOaB41peBp3TreZy0huUlAIF_Q7MxU9kHr2mf9lXuMO2Lrjf-dsV1QCoRWU52hH_wTGcj2WO3WRqubNf3CxTpxfQYBU1-I2iNHa1NqE0aBNVWEGURuuMFJXDhLMx7j6y0BnLuEl0pIavayvA6aZFMKnR1u-WF-lOp45QyBAaNYkejF3tseqzuDkizYyFRnFMU2tEkXSDUnyf5wFAt-WZo2JKQEk1h-k2fNShESAAAAAHPLT_HAA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Prince_Music_group")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/prince_Music_channel")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7770816455").split()))


FAILED = "https://graph.org/file/9bed950a923860af1da64-92218b6b21eb47b1dc.jpg"
