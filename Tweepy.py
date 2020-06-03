from tweepy import API
from tweepy import OAuthHandler

import settings


# See:
# http://docs.tweepy.org/en/latest/getting_started.html
# https://qiita.com/iroiro_bot/items/3406caf025e89b8f7a25
def use_twitter_api():
    CONSUMER_KEY = settings.CONSUMER_KEY
    CONSUMER_SECRET = settings.CONSUMER_SECRET
    ACCESS_TOKEN = settings.ACCESS_TOKEN
    ACCESS_SECRET = settings.ACCESS_SECRET

    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = API(auth)

    return api
