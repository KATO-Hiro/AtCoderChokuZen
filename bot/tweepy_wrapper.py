from tweepy import Client
import logging

import settings

logger = logging.getLogger()


# See:
# http://docs.tweepy.org/en/latest/getting_started.html
# https://docs.tweepy.org/en/latest/client.html#tweepy.Client
# https://realpython.com/twitter-bot-python-tweepy/
# https://qiita.com/iroiro_bot/items/3406caf025e89b8f7a25
def create_twitter_api():
    BEARER_TOKEN = settings.BEARER_TOKEN
    CONSUMER_KEY = settings.CONSUMER_KEY
    CONSUMER_SECRET = settings.CONSUMER_SECRET
    ACCESS_TOKEN = settings.ACCESS_TOKEN
    ACCESS_SECRET = settings.ACCESS_SECRET

    client = Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=CONSUMER_KEY, 
        consumer_secret= CONSUMER_SECRET, 
        access_token= ACCESS_TOKEN, 
        access_token_secret= ACCESS_SECRET,
        wait_on_rate_limit=True,
    )

    return client


def tweet(words):
    # See:
    # https://github.com/agronholm/apscheduler/blob/master/examples/schedulers/blocking.py
    api = create_twitter_api()
    response = api.create_tweet(text=words)
    print(f"https://twitter.com/user/status/{response.data['id']}")
