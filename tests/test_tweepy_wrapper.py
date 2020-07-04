from unittest.mock import Mock
from unittest.mock import patch

import pytest

from bot import tweepy_wrapper
from bot.tweepy_wrapper import create_twitter_api


class TestTweepyWrapper(object):

    def test_successfully_create_twitter_api(self):
        api = create_twitter_api()

        assert api

    @patch.object(tweepy_wrapper,
                  'create_twitter_api',
                  Mock(side_effect=Exception)
                  )
    def test_failed_to_create_twitter_api(self):

        with pytest.raises(Exception):
            tweepy_wrapper.create_twitter_api()
