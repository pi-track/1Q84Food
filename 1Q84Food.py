#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary
from FoodKeys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twt = api.search(q="@1Q84Food")
print(twt)

#list of specific strings we want to check for in Tweets
t = ['A bellhop could bring a pot of coffee.',
    'She preferred coffee as hot and strong as a devil at midnight',
    'Tengo’s coffee arrived.']

for s in twt:
    for i in t:
        sn = s.user.screen_name
        m = "@{0} {1}".format(sn, i)
        s = api.update_status(m, s.id)