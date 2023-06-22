class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 16452568
    API_HASH = "f936697c5c9e5bffd433babef7a4e4c9"

    CASH_API_KEY = "J1BBEIOV38CZ"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    EVENT_LOGS = (-1001935424604)  # Event logs channel to note down important bot level events

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/9f93ca1114a1e01b63239.jpg"
    
    DONATE_LINK = "https://t.me/stories_zulll/34"

    SUPPORT_CHAT = "envSample"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = ""  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "ZMOE8Q6BE25J7BEU"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1337085565  # User id of your telegram account (Must be integer)

    #TAMBAHAN
    DATABASE_URL = "postgres://bqlkbhhl:YG-iSQ5u5g-6l2MJ-NRgEi-yPJnq3S-H@rajje.db.elephantsql.com/bqlkbhhl"
    MONGO_DB_URI = "mongodb+srv://avel:tmp0@aveltmp.nqyqy6h.mongodb.net/aveltmp?retryWrites=true&w=majority"
    ARQ_API_KEY = "UHZKNH-IRFVEV-ANNQWQ-XMZKFE-ARQ"
    ARQ_API_URL = "http://arq.hamker.dev"
    
    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [1337085565]  # User id of sudo users
    DEV_USERS = [1337085565]  # User id of dev users
    DEMONS = [1337085565]  # User id of support users
    TIGERS = [1337085565]  # User id of tiger users
    WOLVES = [1337085565]  # User id of whitelist users

    ALLOW_CHATS = True
    OWNER_USERNAME = "MSDZULQRNN"
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
