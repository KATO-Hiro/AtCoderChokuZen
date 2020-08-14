import os
import requests

from apscheduler.schedulers.blocking import BlockingScheduler

from announce import announce_contest
from atcoder import fetch_upcoming_contest
from schedule import set_jst
from schedule import set_announce_time


def main():
    status_code, contest = fetch_upcoming_contest()

    if status_code != requests.codes.ok:
        exit()

    # contest_start_time_str = '2020-07-01 15:00:00+09:00'
    contest_start_time_str = contest.start_date
    contest_start_time, _ = set_announce_time(
        contest_start_time=contest_start_time_str,
        before_hours=24
    )

    print('Contest name: ', contest.name)
    print('Contest start: ', contest_start_time)
    print('Contest url: ', contest.url)

    jst = set_jst()
    scheduler = BlockingScheduler(timezone=jst)

    remain_hours_minutes = [('before 24 hours 00 minutes: ', 24, 0),
                            ('before 12 hours 00 minutes: ', 12, 0),
                            ('before 06 hours 00 minutes: ', 6, 0),
                            ('before 03 hours 00 minutes: ', 3, 0),
                            ('before 01 hours 00 minutes: ', 1, 0),
                            ('before 00 hours 30 minutes: ', 0, 30),
                            ('before 00 hours 15 minutes: ', 0, 15)
                            ]

    for description, hours, minutes in remain_hours_minutes:
        _, before_contest_date = set_announce_time(
            contest_start_time=contest_start_time_str,
            before_hours=hours,
            before_minutes=minutes
        )

        print(description, before_contest_date)

        scheduler.add_job(announce_contest,
                          'date',
                          run_date=before_contest_date,
                          args=[contest]
                          )

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    main()
