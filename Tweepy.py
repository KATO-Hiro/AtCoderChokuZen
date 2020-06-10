from tweepy import API
from tweepy import OAuthHandler
import logging

import settings

logger = logging.getLogger()


# See:
# http://docs.tweepy.org/en/latest/getting_started.html
# http://docs.tweepy.org/en/latest/api.html?highlight=API#API
# https://realpython.com/twitter-bot-python-tweepy/
# https://qiita.com/iroiro_bot/items/3406caf025e89b8f7a25
def create_twitter_api():
    CONSUMER_KEY = settings.CONSUMER_KEY
    CONSUMER_SECRET = settings.CONSUMER_SECRET
    ACCESS_TOKEN = settings.ACCESS_TOKEN
    ACCESS_SECRET = settings.ACCESS_SECRET

    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = API(auth,
              wait_on_rate_limit=True,
              wait_on_rate_limit_notify=True
              )

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)

        raise e

    logger.info("API was created")

    return api
