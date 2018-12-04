import time

import tweepy

from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

access_keys = []
with open('keys.txt', 'r') as key_file:
    lines = key_file.readlines()
    for line in lines:
        line = line.split(',')
        access_keys.append({'key': line[0], 'secret': line[1], 'username': line[2][:-1]})

keywords = [
    '#btc',
    '#bitcoin',
    '#takibetakip',
    '#takipedentakipedilir',
    '#geritakip',
    '#takipedeneanındageritakip',
    '#garantitakip',
    '#takipleselim',
    '#folloforfolloback',
]

class Listener(tweepy.StreamListener):

    def on_status(self, status):
        status = status._json
        for key in access_keys:
            auth.set_access_token(key['key'], key['secret'])
            api = tweepy.API(auth)
            follow = api.create_friendship(screen_name=status['user']['screen_name'])


def start_stream():
    while True:
        try:
            listener = Listener()
            stream = tweepy.Stream(auth=api.auth, listener=listener)
            stream.filter(track=keywords)
        except:
            time.sleep(300)
            continue

start_stream()