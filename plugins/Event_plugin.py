import asyncio
import re

from telethon import events
import json

BlockList = ['_init', '_chat_peer', 'InputPeerUser']


async def init(bot):
    @bot.on(events.NewMessage(incoming=True, pattern=rf"^(/start)"))
    async def start(event):
        await bot.send_message(entity=event.chat_id, message='I will display you all information about an event.\n'
                                                        '\n'
                                                        'How do I work?\n'
                                                        '- Add me to any chat / channel and send a message\n'
                                                        '- I convert it into the whole event log for you to see there\n')


    @bot.on(events.NewMessage(incoming=True, pattern=rf"^(/privacy)"))
    async def start(event):
        await bot.send_message(entity=event.chat_id, message='The bot does not save any information!\n'
                                       'There\'s no database behind it and the bot code is open for everyone.\n'
                                       'Logging is not implemented for privacy reasons\n'
                                       '\n'
                                       'The code: https://github.com/ShadowsCodes/TelethonEventHelper')

    @bot.on(events.NewMessage(incoming=True, pattern=rf"^(/version)"))
    async def start(event):
        await bot.send_message(entity=event.chat_id,
                               message='The bot works on:\n'
                                       '- Python 3.11.1\n'
                                       '- Telethon 1.26.0\n'
                                       '\n'
                                       'Contact: @Shadowscodesfeedback_bot')

    @bot.on(events.NewMessage(incoming=True))
    async def eventSwap(event):
        if event.raw_text != '/start' and event.raw_text != '/privacy' and event.raw_text != '/version':
            if event:
                tab = 4
                event_array_chat = str(event.chat).replace(',', '\n')
                event_array_message = str(event.message).replace(',', '\n')
                event_array_input_chat = str(event.input_chat).replace(',', '\n')
                response = []
                response.append('<code>')
                response.append('event.chat')
                response.append('\n')
                for line in event_array_chat.splitlines():
                    counter = 0
                    if '(' in line:
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        newvalue = line.split('(')
                        response.append(newvalue[0] + '(')
                        response.append('\n')
                        counter = 0
                        tab = tab + 4
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        response.append(newvalue[1])
                        response.append('\n')
                    if ')' in line:
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        newvalue = line.split(')')
                        response.append(newvalue[0] + ')')
                        response.append('\n')
                        counter = 0
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        response.append(newvalue[1])
                        response.append('\n')
                        tab = tab - 4
                    if '(' not in line and ')' not in line:
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        line = line.replace('=', ' = ')
                        response.append(line.replace(' ', ''))
                        response.append('\n')
                response.append('</code>')
                await bot.send_message(entity=event.chat_id, message=''.join(response), parse_mode='HTML')

                response = []
                response.append('\n')
                response.append('<code>')
                response.append('event.message')
                response.append('\n')
                for line in event_array_message.splitlines():
                    counter = 0
                    if '(' in line:
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        newvalue = line.split('(')
                        response.append(newvalue[0] + '(')
                        response.append('\n')
                        counter = 0
                        tab = tab + 4
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        response.append(newvalue[1])
                        response.append('\n')
                    if ')' in line:
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        newvalue = line.split(')')
                        response.append(newvalue[0] + ')')
                        response.append('\n')
                        counter = 0
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        response.append(newvalue[1])
                        response.append('\n')
                        tab = tab - 4
                    if '(' not in line and ')' not in line:
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        response.append(line)
                        response.append('\n')
                response.append('</code>')
                await bot.send_message(entity=event.chat_id, message=''.join(response), parse_mode='HTML')

                response = []
                response.append('\n')
                response.append('<code>')
                response.append('event.input_chat')
                response.append('\n')
                for line in event_array_input_chat.splitlines():
                    counter = 0
                    if '(' in line:
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        newvalue = line.split('(')
                        response.append(newvalue[0] + '(')
                        response.append('\n')
                        counter = 0
                        tab = tab + 4
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        response.append(newvalue[1])
                        response.append('\n')
                    if ')' in line:
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        newvalue = line.split(')')
                        response.append(newvalue[0] + ')')
                        response.append('\n')
                        counter = 0
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        response.append(newvalue[1])
                        response.append('\n')
                        tab = tab - 4
                    if '(' not in line and ')' not in line:
                        while tab > counter:
                            response.append(' ')
                            counter += 1
                        response.append(line)
                        response.append('\n')
                response.append('</code>')
                await bot.send_message(entity=event.chat_id, message=''.join(response), parse_mode='HTML')

                response = []
                response.append('<code>')
                response.append('Small Information:')
                response.append('\n')
                response.append('event.is_channel=')
                response.append(str(event.is_channel))
                response.append('\n')
                response.append('event.is_group=')
                response.append(str(event.is_group))
                response.append('\n')
                response.append('event.is_private=')
                response.append(str(event.is_private))
                response.append('\n')
                response.append('event.chat_id=')
                response.append(str(event.chat_id))
                response.append('\n')
                response.append('</code>')
                await bot.send_message(entity=event.chat_id, message=''.join(response), parse_mode='HTML')