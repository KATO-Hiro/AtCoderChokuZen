from datetime import datetime
from datetime import timedelta
import os

from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import timezone
from Tweepy import use_twitter_api


def set_jst():
    # See:
    # https://github.com/stub42/pytz/blob/master/src/README.rst
    # https://note.nkmk.me/python-datetime-pytz-timezone/
    jst = timezone('Asia/Tokyo')

    return jst


def tweet(words):
    api = use_twitter_api()
    api.update_status(words)


def tick():
    # See:
    # https://github.com/agronholm/apscheduler/blob/master/examples/schedulers/blocking.py
    jst = set_jst()
    words = 'Test! The time is: %s' % datetime.now(jst)

    tweet(words)


def calc_time_remaining(contest_start_time, now_jst):
    diff = datetime.fromisoformat(str(contest_start_time)) - now_jst
    remain_hours = diff.seconds // 3600
    remain_minutes = (diff.seconds % 3600) // 60

    return remain_hours, remain_minutes


def get_note() -> str:
    note = '【注】開発中のBotです。α版の公開までお待ちください。\n\n'

    return note


def get_hash_tags() -> str:
    hash_tags = '#AtCoder #AtCoderChokuZenBot\n\n'

    return hash_tags


# TODO: Enable to change contest name.
def get_contest_name() -> str:
    contest_name = '【AtCoder hogehoge Contest fuga】開催まで、\n'

    return contest_name


def get_now_jst():
    # See:
    # https://docs.python.org/ja/3/library/datetime.html
    jst = set_jst()
    now_jst = datetime.fromisoformat(str(datetime.now(jst)))

    return now_jst


def get_current_time_jst(now_jst):
    current_time_jst = '現在の時刻(JST): ' + str(now_jst) + '\n\n'

    return current_time_jst


def get_remain_time(contest_start_time, now_jst) -> str:
    remain_hours, remain_minutes = calc_time_remaining(
                                   contest_start_time=contest_start_time,
                                   now_jst=now_jst
                                   )
    remain_time = '約 ' + str(remain_hours) + ' 時間 ' + str(remain_minutes) + ' 分です。\n\n'

    return remain_time


def add_contest_url(url: str) -> str:
    url = url + '\n'

    return url


def announce_contest(contest_start_time, contest_url):
    note = get_note()
    hash_tags = get_hash_tags()

    now_jst = get_now_jst()
    current_time_jst = get_current_time_jst(now_jst)
    contest_name = get_contest_name()
    remain_time = get_remain_time(
        contest_start_time=contest_start_time,
        now_jst=now_jst
    )

    contest_url = add_contest_url(contest_url)

    words = note + hash_tags + current_time_jst + contest_name + remain_time + contest_url
    tweet(words)


def set_announce_time(contest_start_time: str, before_hours: int):
    delta = timedelta(hours=before_hours)
    contest_start_time = datetime.fromisoformat(contest_start_time)
    announce_start_time = contest_start_time - delta

    return contest_start_time, announce_start_time


# HACK: Not good solution.
#        It is necessary to remove '+X:XX',
#        but builtin function may be existed.
def remove_timezone(time) -> str:
    return str(time).split('+')[0]


if __name__ == '__main__':
    # TODO: Fetch contest date from AtCoder Official page.
    contest_start_time_str = '2020-06-10 13:00:00+09:00'
    contest_start_time, announce_start_time = set_announce_time(
        contest_start_time=contest_start_time_str,
        before_hours=6
    )
    # TODO: Fetch contest url from AtCoder Official page.
    contest_url = 'https://atcoder.jp/contests/agc045'
    print('Announce start: ', announce_start_time)
    print('Contest start: ', contest_start_time)
    print('Contest url: ', contest_url)

    jst = set_jst()
    scheduler = BlockingScheduler(timezone=jst)
    # TODO: Enable to change start and end date accoring to the constest.
    scheduler.add_job(announce_contest,
                      'interval',
                      minutes=1,
                      start_date=remove_timezone(announce_start_time),
                      end_date=remove_timezone(contest_start_time),
                      args=[contest_start_time, contest_url]
                      )

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
