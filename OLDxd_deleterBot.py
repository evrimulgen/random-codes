import json
import requests
import re
import time

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
    

def delete_message(message_id, chat_id):
    url = URL + "deleteMessage?message_id={}&chat_id={}".format(message_id, chat_id)
    get_url(url)


def main():
    last_textchat = (None, None)
    while True:
        chat, message = get_last_chat_id_and_message_id(get_updates())   
        text = get_last_text(get_updates())
        if re.search("\\ud83d|\\ude06", text):
            delete_message("\\ud83d\\ude06", chat)
            last_textchat = (text, chat)
        elif re.search("xd|Xd|XD|xD|", text):
            delete_message(message, chat)
            last_textchat = (text, chat)
        time.sleep(0.5)


if __name__ == '__main__':
    main()