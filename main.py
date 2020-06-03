from Tweepy import use_twitter_api


def tweet(words):
    api = use_twitter_api()
    api.update_status(words)


if __name__ == '__main__':
    tweet('Hello, world!')
