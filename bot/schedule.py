from datetime import datetime
from datetime import timedelta
from pytz import timezone


def set_jst():
    # See:
    # https://github.com/stub42/pytz/blob/master/src/README.rst
    # https://note.nkmk.me/python-datetime-pytz-timezone/
    jst = timezone('Asia/Tokyo')

    return jst


def get_now_jst():
    # See:
    # https://docs.python.org/ja/3/library/datetime.html
    jst = set_jst()
    now_without_seconds = remove_seconds_from_datetime(datetime.now(jst))
    now_jst = datetime.fromisoformat(str(now_without_seconds))

    return now_jst


# HACK: Hard coding(+09:00) is not good solution.
# See:
# https://www.codespeedy.com/remove-seconds-from-the-datetime-in-python/
def remove_seconds_from_datetime(datetime_now):
    results = datetime_now.strftime("%Y-%m-%d %H:%M+09:00")

    return results


def calc_time_remaining(contest_start_time, now_jst):
    diff = datetime.fromisoformat(str(contest_start_time)) - now_jst
    remain_hours = diff.seconds // 3600
    remain_minutes = (diff.seconds % 3600) // 60

    return remain_hours, remain_minutes


# See:
# https://realpython.com/lessons/type-hinting/
def set_announce_time(contest_start_time: str,
                      before_hours: int,
                      before_minutes: int = 0
                      ):
    delta = timedelta(hours=before_hours,
                      minutes=before_minutes
                      )
    contest_start_time = datetime.fromisoformat(contest_start_time)
    announce_start_time = contest_start_time - delta

    return contest_start_time, announce_start_time


# HACK: Not good solution.
#        It is necessary to remove '+X:XX',
#        but builtin function may be existed.
def remove_timezone(time) -> str:
    return str(time).split('+')[0]


def main():
    print(get_now_jst())


if __name__ == '__main__':
    main()
