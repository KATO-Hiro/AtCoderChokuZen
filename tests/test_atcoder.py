import pytest
import requests

from bot import atcoder
from bot.atcoder import fetch_upcoming_contest
from bot.atcoder import _fetch_home_page
from bot.atcoder import _fix_contest_date_format
from bot.atcoder import _get_upcoming_contest_info
from bot.atcoder import _parse_upcoming_contests
from bot.contest import Contest


@pytest.fixture()
def response():
    return _fetch_home_page()


class TestAtCoder(object):

    @pytest.mark.vcr('fixtures/vcr_cassettes/atcoder_upcoming_contest.yaml')
    def test_response(self, response):
        assert response.status_code == requests.codes.ok
        assert response.text

    @pytest.mark.vcr('fixtures/vcr_cassettes/atcoder_upcoming_contest.yaml')
    def test__parse_upcoming_contests(self, response):
        upcoming_contests = _parse_upcoming_contests(response)

        assert upcoming_contests

    @pytest.mark.vcr('fixtures/vcr_cassettes/atcoder_upcoming_contest.yaml')
    def test__get_upcoming_contest_info(self, response, monkeypatch):
        upcoming_contests = _parse_upcoming_contests(response)
        contest_info = _get_upcoming_contest_info(upcoming_contests)

        assert contest_info.name == 'AtCoder Beginner Contest 172'
        assert contest_info.start_date == '2020-06-27 21:00:00+09:00'
        assert contest_info.url == 'https://atcoder.jp/contests/abc172'

    @pytest.mark.vcr('fixtures/vcr_cassettes/atcoder_upcoming_contest.yaml')
    def test_fetch_contest_info_for_abc172(self, monkeypatch):
        monkeypatch.setattr(atcoder,
                            'fetch_upcoming_contest',
                            self._dummy_contest_info_for_abc172)
        status_code, contest_info = fetch_upcoming_contest()

        assert status_code == requests.codes.ok
        assert contest_info.name == 'AtCoder Beginner Contest 172'
        assert contest_info.start_date == '2020-06-27 21:00:00+09:00'
        assert contest_info.url == 'https://atcoder.jp/contests/abc172'

    def _dummy_contest_info_for_abc172(self):
        name = 'AtCoder Beginner Contest 172'
        start_date = '2020-06-27 21:00:00+09:00'
        url = 'https://atcoder.jp/contests/abc172'

        contest = Contest(name=name, start_date=start_date, url=url)

        return requests.codes.ok, contest

    # See:
    # https://www.magata.net/memo/index.php?pytest%C6%FE%CC%E7#kc1cba3c
    @pytest.mark.vcr('fixtures/vcr_cassettes/atcoder_upcoming_contest.yaml')
    def test_failed_to_fetch_contest_info_for_abc172(self, monkeypatch):
        monkeypatch.setattr(atcoder,
                            'fetch_upcoming_contest',
                            self._dummy_failed_to_fetch_upcoming_contest)

        status_code, contest_info = atcoder.fetch_upcoming_contest()

        assert status_code == 404
        assert contest_info is None

    def _dummy_failed_to_fetch_upcoming_contest(self):
        status_code = 404

        return status_code, None

    def test__fix_contest_date_format(self):
        date = '2020-06-27 21:00:00+0900'
        actual = _fix_contest_date_format(date)
        expected = '2020-06-27 21:00:00+09:00'

        assert actual == expected
