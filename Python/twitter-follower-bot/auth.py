import tweepy

from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

print(auth.get_authorization_url())
pin = input("PIN: ")
tokens = auth.get_access_token(pin)
username = input("Username: ")

with open("keys.txt", "a") as key_file:
    key_file.write(tokens[0] + "," + tokens[1] + "," + username)
