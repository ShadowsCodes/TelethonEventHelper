# Imports
import logging
from logging.handlers import TimedRotatingFileHandler
from telethon import TelegramClient
from service import ConfigService as conf, BotMethodService as botmethods
from models.basemodel import Session

# Gets the root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
fh = TimedRotatingFileHandler('logs/console.log', when="midnight", interval=1, backupCount=5)
formatter = logging.Formatter('%(levelname)s [%(asctime)s] [%(filename)s:%(lineno)d] %(message)s', '%H:%M:%S')
fh.setFormatter(formatter)
logger.addHandler(fh)

# Pre loader for the config
conf.init()

# Use your own values from my.telegram.org
api_id = conf.get_int('API', 'api_id')
api_hash = conf.get_string('API', 'api_hash')
bot_token = conf.get_string('API', 'bot_token')

# Manual call line to sign in as a bot.
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
bot.flood_sleep_threshold = 15

# Initiating the bot methods
botmethods.init(bot)

# Creating session for the dao applications and services
session = Session()
# example for dao: playerdao.init(session)


# Loads the game handlers
# if __name__ == '__main__':


# Plugin loader
try:
    # Standalone script __init__.py with folder plugins/
    import plugins

    plugins.init(bot, session)
except ImportError:
    try:
        from . import plugins

        plugins.init(bot, session)
    except ImportError:
        plugins = None
try:
    bot.run_until_disconnected()
finally:
    bot.disconnect()
