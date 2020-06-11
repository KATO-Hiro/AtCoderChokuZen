import os

from apscheduler.schedulers.blocking import BlockingScheduler

from announce import announce_contest
from atcoder import fetch_upcoming_contest
from schedule import remove_timezone
from schedule import set_jst
from schedule import set_announce_time


def main():
    contest = fetch_upcoming_contest()

    # TODO: Fetch contest date from AtCoder Official page.
    # contest_start_time_str = '2020-06-10 20:00:00+09:00'
    contest_start_time_str = contest.start_date
    contest_start_time, announce_start_time = set_announce_time(
        contest_start_time=contest_start_time_str,
        before_hours=12
    )
    print('Contest name: ', contest.name)
    print('Announce start: ', announce_start_time)
    print('Contest start: ', contest_start_time)
    print('Contest url: ', contest.url)

    jst = set_jst()
    scheduler = BlockingScheduler(timezone=jst)
    scheduler.add_job(announce_contest,
                      'interval',
                      minutes=30,
                      start_date=remove_timezone(announce_start_time),
                      end_date=remove_timezone(contest_start_time),
                      args=[contest]
                      )

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    main()
