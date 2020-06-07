from datetime import datetime
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


def announce_contest():
    note = '【注】開発中のBotです。α版の公開までお待ちください。\n\n'

    hash_tags = '#AtCoder #AtCoderChokuZenBot\n\n'

    jst = set_jst()
    current_time_jst = '現在の時刻(JST): ' + str(datetime.now(jst)) + '\n\n'
    contset_name = '【AtCoder hogehoge Contest fuga】開催まで、\n'

    hour = 'bar'
    minute = 'fuga'
    remain_time = '約 ' + hour + ' 時間 ' + minute + ' 分です。\n'

    words = note + hash_tags + current_time_jst + contset_name + remain_time
    tweet(words)


if __name__ == '__main__':
    jst = set_jst()

    scheduler = BlockingScheduler(timezone=jst)
    # TODO: Enable to change start and end date accoring to the constest.
    scheduler.add_job(announce_contest,
                      'interval',
                      minutes=1,
                      start_date='2020-06-07 15:33:00',
                      end_date='2020-06-07 15:38:00'
                      )

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
