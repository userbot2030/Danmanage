class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 16452568
    API_HASH = "f936697c5c9e5bffd433babef7a4e4c9"

    CASH_API_KEY = "J1BBEIOV38CZ"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://xgjapvne:JAVP4wiquJr5a-99moi-XV4EYxBZ4F3X@hansken.db.elephantsql.com/xgjapvne"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001935424604)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Muhammad:new37@cluster0.i5k0icq.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/9f93ca1114a1e01b63239.jpg"
    
    DONATE_LINK = "https://t.me/stories_zulll/34"

    SUPPORT_CHAT = "MSPR0JECT"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6135290396:AAF7UgILn63OaK17nErr2Z_DGK9Tqvn4d98"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "ZMOE8Q6BE25J7BEU"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1337085565  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    OWNER_USERNAME = "Kiritonibos"
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
