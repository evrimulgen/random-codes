
import json
import requests
import re
import time
import sys
import telepot
from telepot.loop import MessageLoop


# TOKEN = "461288912:AAEa8DEl0-Din8sDp8fuVBUKiVtRsCG7Y9Q"
# URL = "https://api.telegram.org/bot{}/".format(TOKEN)

# def get_url(url):
#     response = requests.get(url)
#     content = response.content.decode("utf8")
#     return content


# def get_json_from_url(url):
#     content = get_url(url)
#     js = json.loads(content)
#     return js


# def get_updates():
#     url = URL + "getUpdates"
#     js = get_json_from_url(url)
#     return js

# def get_last_chat_id_and_message_id(updates):
#     num_updates = len(updates["result"])
#     last_update = num_updates - 1
#     chat_id = updates["result"][last_update]["message"]["chat"]["id"]
#     message_id = updates["result"][last_update]["message"]["message_id"]
#     return (chat_id, message_id)

# def get_last_text(updates):
#     num_updates = len(updates["result"])
#     last_update = num_updates - 1
#     text = updates["result"][last_update]["message"]["text"]
#     return text

# # chat ('text', 'group', -254315048)
# # deleteMessage(self, msg_identifier)
# #msg_identifier = (chat_id, message_id)

# def message_identifier(msg):
#     if 'chat' in msg and 'message_id' in msg:
#         return msg['chat']['id'], msg['message_id']
#     elif 'inline_message_id' in msg:
#         return msg['inline_message_id'],
#     else:
#         raise ValueError()

# def deleteMessage(self, msg_identifier):
#     p = _strip(locals(), more=['msg_identifier'])
#     p.update(_dismantle_message_identifier(msg_identifier))
#     return self._api_request('deleteMessage', _rectify(p))

TOKEN = "461288912:AAEa8DEl0-Din8sDp8fuVBUKiVtRsCG7Y9Q"  # get token from command-line

# Keep the program running.

# _BotBase(builtins.object)
def message_identifier(msg):
    if 'chat' in msg and 'message_id' in msg:
        return msg['chat']['id'], msg['message_id']
    elif 'inline_message_id' in msg:
        return msg['inline_message_id'],
    else:
        raise ValueError()

def deleteMessage(self, msg_identifier):
    p = _strip(locals(), more=['msg_identifier'])
    p.update(_dismantle_message_identifier(msg_identifier))
    return self._api_request('deleteMessage', _rectify(p))

TOKEN = "461288912:AAEa8DEl0-Din8sDp8fuVBUKiVtRsCG7Y9Q"  # get token from command-line

bot = telepot.Bot(TOKEN)

MessageLoop(bot, Bot.deleteMessage).run_as_thread()
print('Listening ...')

while 1:
	time.sleep(10)
