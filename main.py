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


def announce_contest(contest_start_time):
    note = '【注】開発中のBotです。α版の公開までお待ちください。\n\n'

    hash_tags = '#AtCoder #AtCoderChokuZenBot\n\n'

    jst = set_jst()
    # FIXME: Typo.
    contest_name = '【AtCoder hogehoge Contest fuga】開催まで、\n'

    # See:
    # https://docs.python.org/ja/3/library/datetime.html
    now_jst = datetime.fromisoformat(str(datetime.now(jst)))
    current_time_jst = '現在の時刻(JST): ' + str(now_jst) + '\n\n'

    # TODO: Extract method.
    diff = datetime.fromisoformat(str(contest_start_time)) - now_jst
    remain_hours = diff.seconds // 3600
    remain_minutes = (diff.seconds % 3600) // 60
    remain_time = '約 ' + str(remain_hours) + ' 時間 ' + str(remain_minutes) + ' 分です。\n'

    words = note + hash_tags + current_time_jst + contest_name + remain_time
    tweet(words)


if __name__ == '__main__':
    jst = set_jst()

    hours = 6
    delta = timedelta(hours=hours)
    contest_start_time = datetime.fromisoformat('2020-06-07 23:45:00+09:00')
    announce_start_time = contest_start_time - delta
    print(announce_start_time)
    print(contest_start_time)

    scheduler = BlockingScheduler(timezone=jst)
    # TODO: Enable to change start and end date accoring to the constest.
    # FIXME: str(hoge).split('+')[0] is not good solution.
    #        It is necessary to remove '+9:00',
    #        but builtin function may be existed.
    scheduler.add_job(announce_contest,
                      'interval',
                      minutes=1,
                      start_date=str(announce_start_time).split('+')[0],
                      end_date=str(contest_start_time).split('+')[0],
                      args=[contest_start_time]
                      )

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
