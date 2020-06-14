from datetime import datetime
from datetime import timedelta
from datetime import timezone
import pytest

from bot.schedule import calc_time_remaining
from bot.schedule import remove_seconds_from_datetime
from bot.schedule import remove_timezone
from bot.schedule import set_announce_time


class TestSchedule(object):

    def test_remove_seconds_from_datetime(self):
        dummy_now = datetime(2020, 6, 14, 21, 0, 30)
        datetime_without_seconds = remove_seconds_from_datetime(dummy_now)

        assert datetime_without_seconds == '2020-06-14 21:00+09:00'

    @pytest.mark.parametrize((
        'contest_day', 'contest_hour', 'contest_minute',
        'now_day', 'now_hour', 'now_minute',
        'expected_remain_hours', 'expected_remain_minutes'
        ), [
        (14, 21, 0,
         14, 21, 0,
         0, 0),
        (14, 21, 0,
         14, 12, 0,
         9, 0),
        (14, 20, 0,
         14, 12, 0,
         8, 0),
        (14, 21, 0,
         13, 21, 30,
         23, 30),
        (14, 21, 30,
         14, 12, 0,
         9, 30),
        (14, 21, 15,
         14, 12, 3,
         9, 12),
    ])
    def test_calc_time_remaining(self,
                                 contest_day, contest_hour, contest_minute,
                                 now_day, now_hour, now_minute,
                                 expected_remain_hours, expected_remain_minutes
                                 ):
        remain_hours, remain_minutes = calc_time_remaining(
            contest_start_time=self._generate_datetime_jst(
                year=2020, month=6,
                day=contest_day, hour=contest_hour, minute=contest_minute
            ),
            now_jst=self._generate_datetime_jst(
                year=2020, month=6,
                day=now_day, hour=now_hour, minute=now_minute
            )
        )

        assert remain_hours == expected_remain_hours
        assert remain_minutes == expected_remain_minutes

    @pytest.mark.parametrize((
        'before_hours', 'announce_start_day', 'announce_start_hour'), [
        (12, 13, 9),
        (24, 12, 21)
    ])
    def test_set_announce_time(self, before_hours,
                               announce_start_day, announce_start_hour):
        contest_start_time, announce_start_time = set_announce_time(
            contest_start_time='2020-06-13 21:00:00+09:00',
            before_hours=before_hours
        )

        expected_contest_start_time = self._generate_datetime_jst(
            year=2020, month=6,
            day=13, hour=21, minute=0
        )
        expected_announce_start_time = self._generate_datetime_jst(
            year=2020, month=6,
            day=announce_start_day, hour=announce_start_hour, minute=0
        )

        assert contest_start_time == expected_contest_start_time
        assert announce_start_time == expected_announce_start_time

    def test_remove_timezone(self):
        time_with_timezone = self._generate_datetime_jst(
            year=2020, month=6, day=14, hour=21, minute=0
        )

        time_without_timezone = remove_timezone(time_with_timezone)
        expected = '2020-06-14 21:00:00'

        assert time_without_timezone == expected

    def _generate_datetime_jst(self, year, month, day, hour, minute):
        time_difference_hours = 9
        minutes = 60
        seconds = 60
        time_difference_seconds = time_difference_hours * minutes * seconds

        datetime_jst = datetime(
            year, month, day, hour, minute,
            tzinfo=timezone(timedelta(seconds=time_difference_seconds))
        )

        return datetime_jst
