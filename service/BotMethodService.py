import logging
import traceback

bot = None

logger = logging.getLogger(__name__)


def init(newbot):
    global bot
    bot = newbot


async def send_message(entity,
                       message,
                       buttons=None,
                       reply_to=None,
                       parse_mode='html'):
    try:
        if reply_to:
            if buttons:
                return await bot.send_message(entity=int(entity), message=str(message), parse_mode=parse_mode, buttons=buttons, reply_to=int(reply_to))
            else:
                return await bot.send_message(entity=int(entity), message=str(message), parse_mode=parse_mode, reply_to=int(reply_to))
        else:
            if buttons:
                return await bot.send_message(entity=int(entity), message=str(message), parse_mode=parse_mode, buttons=buttons)
            else:
                return await bot.send_message(entity=int(entity), message=str(message), parse_mode=parse_mode)
    except Exception as e:
        logger.exception('Entity with id: "' + str(entity) + '", can\'t recieve the message.\n\n' + ''.join(traceback.format_stack()) + '\n\n')


async def edit_message(entity,
                       message,
                       text,
                       buttons=None,
                       parse_mode='html'):
    try:
        if buttons:
            return await bot.edit_message(entity=int(entity), message=message,
                                          text=text,
                                          buttons=buttons, parse_mode=parse_mode)
        else:
            return await bot.edit_message(entity=int(entity), message=message,
                                          text=text, parse_mode=parse_mode)
    except Exception as e:
        logger.exception('Cant Edit message with id: ' + str(message) + ' in the Entity with id: "' + str(entity) + '" ' + str(e))


async def pin_message(entity, message, notify=False):
    try:
        await bot.pin_message(entity=int(entity), message=message, notify=notify)
    except Exception as e:
        logger.exception('Cant pin message with the id: ' + str(message) + ' in the entity with id: "' + str(entity) + '"' + str(e))


async def send_file(entity, file, force_document=False):
    try:
        if force_document:
            return await bot.send_message(entity=int(entity), file=file, force_document=force_document)
        else:
            return await bot.send_message(entity=int(entity), file=file)
    except Exception as e:
        logger.exception('Entity with id: "' + str(entity) + '", can\'t recieve the message.' + str(e))


async def send_file_with_caption(entity, file, caption=''):
    try:
        await bot.send_file(entity=int(entity), file=file, caption=caption)
    except Exception as e:
        logger.exception('Entity with id: "' + str(entity) + '", can\'t recieve the message.' + str(e))


async def kick_participant(entity, user):
    try:
        await bot.kick_participant(entity=int(entity), user=user)
    except Exception as e:
        logger.exception('Cant kick user with id: "' + str(user) + '" from the chat with the id: ' + str(user) + str(e))


async def ban_participant(entity, user):
    try:
        await bot.edit_permissions(entity=int(entity), user=user, view_messages=False)
    except Exception as e:
        logger.exception('Cant ban user with id: "' + str(user) + '" from the chat with the id: ' + str(user) + str(e))


async def unban_participant(entity, user):
    try:
        await bot.edit_permissions(entity=entity, user=user)
    except Exception as e:
        logger.exception('Cant unban user with id: "' + str(user) + '" from the chat with the id: ' + str(user) + str(e))