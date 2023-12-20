class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 16452568
    API_HASH = "f936697c5c9e5bffd433babef7a4e4c9"

    CASH_API_KEY = "J1BBEIOV38CZ"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    EVENT_LOGS = (-1001795374467)  # Event logs channel to note down important bot level events

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph//file/a679b3ae99ff100437671.jpg"
    
    DONATE_LINK = "https://link.dana.id/qr/3akqs26o"

    SUPPORT_CHAT = "SiArab_Support"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6515197149:AAEUZdUatsvt_t1ElCqWB2qDl5wEg6Ca9DM"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "ZMOE8Q6BE25J7BEU"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1948147616  # User id of your telegram account (Must be integer)
    
    MUST_JOIN = "SiArab_Support"
    
    #TAMBAHAN
    DATABASE_URL = "mongodb+srv://doadmin:9r260Iqy437zS1lA@db-mongodb-sgp1-52558-1312a8db.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-sgp1-52558"
    MONGO_DB_URI = "mongodb+srv://doadmin:9r260Iqy437zS1lA@db-mongodb-sgp1-52558-1312a8db.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-sgp1-52558"
    ARQ_API_KEY = "WMFOGU-ONOVQJ-QOZVEQ-UHVFBD-ARQ"
    ARQ_API_URL = "http://arq.hamker.dev"
    
    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [1948147616]  # User id of sudo users
    DEV_USERS = [1948147616]  # User id of dev users
    DEMONS = [1948147616]  # User id of support users
    TIGERS = [1948147616]  # User id of tiger users
    WOLVES = [1948147616]  # User id of whitelist users

    ALLOW_CHATS = True
    OWNER_USERNAME = "Dhilnihnge"
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./download/"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
