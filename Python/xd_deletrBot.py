import json
import requests
import re
import time
from time import gmtime, strftime

TOKEN = "461288912:AAEa8DEl0-Din8sDp8fuVBUKiVtRsCG7Y9Q"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_message_id(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    message_id = updates["result"][last_update]["message"]["message_id"]
    return (chat_id, message_id)

def get_last_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    return text



def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&can_delete_messages=True&chat_id={}".format(text, chat_id)
    get_url(url)
    

def delete_message(message_id):
    url = URL + "deleteMessage?message_id={}&chat_id=-300889364".format(message_id)
    get_url(url)


def main():
    while True:
        x = get_updates()['result'][0]['message']['message_id']
        # chat, message = get_last_chat_id_and_message_id(get_updates())   
        # text = get_last_text(get_updates())
        try:
            for i in range(0, 10000):
                message_id = get_updates()['result'][i]['message']['message_id']
                chat_id = get_updates()['result'][i-(i-1)]['message']['chat']['id']
                print(message_id, chat_id)
                delete_message(message_id)
        except:
            print('im sleeping it is {}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))
            time.sleep(10800)
        time.sleep(10800)

main()
