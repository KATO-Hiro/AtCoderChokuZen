from bot.tweepy_wrapper import create_twitter_api


class TestTweepyWrapper(object):

    def test_successfully_create_twitter_api(self):
        api = create_twitter_api()

        assert api
