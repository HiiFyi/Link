import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '24935727'))
API_HASH = environ.get('API_HASH', '3fd33336629324ecd664e9b6894f0909')
BOT_TOKEN = environ.get('BOT_TOKEN', "7623238714:AAFAmUR4TLUq695-6ACfwzbOrgvB69zLG4s")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002374955566'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7348205141').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Linkbot:Linkbot@cluster08766774578.h0jit.mongodb.net/?retryWrites=true&w=majority&appName=Cluster08766774578")
DATABASE_NAME = environ.get('DATABASE_NAME', "Linkbot")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', True)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'onylinks.com')
SHORTLINK_API = environ.get('SHORTLINK_API', 'e0b993ab824859c3375b05a636c32f5b61d528d2')
