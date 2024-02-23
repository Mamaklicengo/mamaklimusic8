from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 21119132))
API_HASH = getenv("API_HASH", "c0a90d0ba66e6bdea356894a55f4856e")

BOT_TOKEN = getenv("BOT_TOKEN", "6704245576:AAGqYQrMMuH2yt2sHJ9Zhk7q2wtNrDA_Eow")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", 6532412571))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/9db6ae360e0a7b833abff.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/3d0d7d23d3a7fb86b442e.jpg")

SESSION = getenv("SESSION", "BADNvmIAbYX1eqXpWeOIl7Ec2zyOnd5eywkS02yebz0e4VMCE59mckRi8xuIEPxJP4hK2NuZjSLKX4TT54IgA4Y6Tw84Eoek__OGLbsHDtKLmpJ93Y2ZrqU0vXmrQn-Iu1PJlrzzT_p1C-GIjM7wG7nVbJWL5Mm8MUWOzsdEr-EIfKNv8Ru8jhRyHS1rezh-qVnOsVuEskedgaoXw8MK8lxViSRPl4hkzn5kDZzui0Q6uv8s8_mWTjG0F9gu8OaxSocbIUNvPOw4xBc5urjDiiFtsSt8LzhTi3DIlKGwjXBgDaufM2WvQbxmso6sxEodveJqfszbjo5Rts0f_kMWieoxmnYbyAAAAAFgBjptAA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/BRANDED_WORLD")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/BRANDRD_BOT")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6532412571").split()))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "BRANDED KIGN")  

FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
