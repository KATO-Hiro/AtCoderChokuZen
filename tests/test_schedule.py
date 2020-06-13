from datetime import datetime
from datetime import timedelta
from datetime import timezone
import pytest

from bot.schedule import set_announce_time


class TestSchedule(object):

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
