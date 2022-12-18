# Imports
from telethon import TelegramClient
from service import ConfigService as conf

# Pre-loader for the config
conf.init()

# Use your own values from my.telegram.org
api_id = conf.get_int('API', 'api_id')
api_hash = conf.get_string('API', 'api_hash')
bot_token = conf.get_string('API', 'bot_token')

# Manual call line to sign in as a bot.
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
bot.flood_sleep_threshold = 15

# Plugin loader
try:
    # Standalone script __init__.py with folder plugins/
    import plugins

    plugins.init(bot)
except ImportError:
    try:
        from . import plugins

        plugins.init(bot)
    except ImportError:
        plugins = None
try:
    bot.run_until_disconnected()
finally:
    bot.disconnect()
