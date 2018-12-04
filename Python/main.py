from collections import defaultdict
import time
from random import randint
import urllib.request as urllib2
import math
import json

import telepot
import requests

from keys import TELEGRAM_TOKEN, DARKSKY_TOKEN

def handle(message):
  """Message/Command handler.

  Available commands:
    - /sa Command for checking bot's status
    - /gunaydin Good morning command
    - /havadurumu Weather forecast for Istanbul and Ankara
    - /hangisi Random word picker
    - /hmm Thinking emoji image
    - /roll Dice rolling command for RP purposes
    - /em Text emphasis command
    - /reddit Returns top posts in given subreddit
  """
  content_type, chat_type, chat_id = telepot.glance(message)
  if content_type == 'text':
    command = message['text'].split(' ')[0]
    if command == '/sa' or command == '/sa@EnisBot':
      bot.sendMessage(chat_id, 'as')
    elif command == '/gunaydin' or command == '/gunaydin@EnisBot':
      bot.sendMessage(chat_id, 'Gunaydin')
    elif command == '/havadurumu' or command == '/havadurumu@EnisBot':
      havadurumu(chat_id, message['text'])
    elif command == '/hangisi' or command == '/hangisi@EnisBot':
      hangisi(chat_id, message['text'])
    elif command == '/roll' or command == '/roll@EnisBot':
      bot.sendMessage(chat_id, str(randint(1, int(message['text'].split(' ')[1]))))
    elif command == '/dndroll' or command == '/dndroll@EnisBot':
      dndroll(chat_id, message["text"])
    elif command == '/em' or command == '/em@EnisBot':
      bot.sendMessage(chat_id, ' '.join(' '.join(message['text'].split(' ')[1:])))
    elif command == '/reddit' or command == '/reddit@EnisBot':
      reddit(chat_id, message['text'])


def havadurumu(chat_id, message):
    message = message.split(' ')

    def create_darksky_link(lat, long):
        return 'https://api.darksky.net/forecast/' + DARKSKY_TOKEN + '/' + lat + ',' + long + '?lang=tr&units=si&exclude=currently,minutely,alerts,flags'

    try:
        message_city = city_index[message[1].lower()]
    except KeyError:
        message_city = plate_index[message[1]]
    link = create_darksky_link(message_city['latitude'], message_city['longitude'])
    request = urllib2.urlopen(link)
    r_json = json.loads(request.read().decode('utf-8'))
    temperature_max = math.floor(float(r_json["daily"]["data"][0]["temperatureMax"]))
    temperature_min = math.floor(float(r_json["daily"]["data"][0]["temperatureMin"]))
    bot.sendMessage(chat_id, message_city['name'].title() + ' | En düşük ' + str(temperature_min) +
                    ' C, En yüksek. ' + str(temperature_max) + ' C. ' + r_json['hourly']['summary'])
    '''
    if message[1].lower() == 'ist' or message[1].lower() == 'istanbul':
      request = urllib2.urlopen(BASEFURLIST)
      r_json = json.loads(request.read().decode('utf-8'))
      temperature_max = math.floor(float(r_json["daily"]["data"][0]["temperatureMax"]))
      temperature_min = math.floor(float(r_json["daily"]["data"][0]["temperatureMin"]))
      bot.sendMessage(chat_id, 'Istanbul | En düşük ' + str(temperature_min) +
                       ' C, En yüksek. ' + str(temperature_max) + ' C. ' + r_json['hourly']['summary'])
    '''


def hangisi(chat_id, message):
  words = message.split(' ')
  if len(words) <= 1:
    pass
  else:
    bot.sendMessage(chat_id, words[randint(1, len(words) - 1)])


def reddit(chat_id, message):
  arguments = message.split(' ')
  subreddit = arguments[1]
  count = 3
  if len(arguments) > 2:
    count = int(arguments[2])
  headers = {"User-Agent": "Enis-BotClient/0.1 by enisbt"}
  response = requests.get('https://www.reddit.com/r/' + subreddit + '/top.json?t=today', headers=headers)
  for x in range(count):
    text = str(x + 1) + '-) ' + response.json()['data']['children'][x]['data']['title']
    text = text + ' - ' + response.json()['data']['children'][x]['data']['url']
    bot.sendMessage(chat_id, text)


def dndroll(chat_id, message):
  params = message.split(" ")
  dice = int(params[2])
  count = int(params[1])
  rolls = []
  for x in range(count):
    rolls.append(randint(1, dice))
  sum_list = sum(rolls)
  text = "Zarlar: "
  for roll in rolls:
    text = text + str(roll) + " "
  text = text + "\n" + "Toplam: " + str(sum_list)
  text = text + "\n" + "En küçük hariç toplam: " + str(sum_list - min(rolls))
  bot.sendMessage(chat_id, text)


bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handle)

response = requests.get('https://raw.githubusercontent.com/enisbt/turkey-cities/master/cities.json')
cities = response.json()
city_index = {}
plate_index = {}

for city in cities:
    city_index[city['name']] = city
    plate_index[city['plate']] = city

while 1:
    time.sleep(1)
