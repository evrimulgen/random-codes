import time
import random

import tweepy
import requests

from keys import *


access_keys = []
with open('keys.txt', 'r') as key_file:
    lines = key_file.readlines()
    for line in lines:
        line = line.split(',')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(line[0], line[1])
        api = tweepy.API(auth)


def get_top_links(subreddit):
    blacklist = [
        "https://www.reddit.com",
        "https://reddit.com",
        "https://twitter.com",
        "https://i.redd.it",
    ]
    headers = {"User-Agent": "Enis-BotClient/0.1 by enisbt"}
    r = requests.get('https://www.reddit.com/r/' + subreddit + '/top.json?t=today', headers=headers)
    json_form = r.json()
    for x in range(20):
        link = json_form['data']['children'][x]['data']['url']
        title = json_form['data']['children'][x]['data']['title']
        blacklisted = False
        for site in blacklist:
            if link.startswith(site) or link in posted_links:
                blacklisted = True
        if blacklisted:
            continue
        text = title
        text = text + ' ' + link
        text = text + ' #BTC #Bitcoin #cryptocurrency #ETH #Ethereum #LTC #blockchain #altcoins'
        return text, link


subreddits = [
    "bitcoin",
    "CryptoCurrency",
    "altcoin",
    "blockchain",
    "ethereum",
]

iteration = 0
posted_links = []
while 1:
    if iteration == 3:
        posted_links = []
    random_sub = random.randint(0, len(subreddits) - 1)
    text, link = get_top_links(subreddits[random_sub])
    posted_links.append(link)
    try:
        api.update_status(text)
        iteration += 1
    except:
        continue
    time.sleep(21600)
