from datetime import datetime
from datetime import timedelta
from datetime import timezone
import pytest

from bot.schedule import calc_time_remaining
from bot.schedule import set_announce_time


class TestSchedule(object):

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

        time_difference_hours = 9
        minutes = 60
        seconds = 60
        time_difference_seconds = time_difference_hours * minutes * seconds

        expected_contest_start_time = datetime(
            2020, 6, 13, 21, 0,
            tzinfo=timezone(timedelta(seconds=time_difference_seconds))
        )
        expected_announce_start_time = datetime(
            2020, 6, announce_start_day, announce_start_hour, 0,
            tzinfo=timezone(timedelta(seconds=time_difference_seconds))
        )

        assert contest_start_time == expected_contest_start_time
        assert announce_start_time == expected_announce_start_time

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
