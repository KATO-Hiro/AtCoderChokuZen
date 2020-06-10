from tweepy_wrapper import tweet
from schedule import calc_time_remaining
from schedule import get_now_jst


def announce_contest(contest):
    note = _get_note()
    hash_tags = _get_hash_tags()

    now_jst = get_now_jst()
    current_time_jst = _get_current_time_jst(now_jst)
    contest_name = _get_contest_name(contest.name)
    remain_time = _get_remain_time(
        contest_start_time=contest.start_date,
        now_jst=now_jst
    )

    contest_url = _add_contest_url(contest.url)

    words = note + hash_tags + current_time_jst + \
        contest_name + remain_time + contest_url
    tweet(words)


def _get_note() -> str:
    note = '【注】開発中のBotです。α版の公開までお待ちください。\n\n'

    return note


def _get_hash_tags() -> str:
    hash_tags = '#AtCoder #AtCoderChokuZenBot\n\n'

    return hash_tags


def _get_current_time_jst(now_jst):
    current_time_jst = '現在の時刻(JST): ' + str(now_jst) + '\n\n'

    return current_time_jst


def _get_remain_time(contest_start_time, now_jst) -> str:
    remain_hours, remain_minutes = calc_time_remaining(
        contest_start_time=contest_start_time,
        now_jst=now_jst
    )
    remain_time = '約 ' + str(remain_hours) + ' 時間 ' + \
        str(remain_minutes) + ' 分です。\n\n'

    return remain_time


def _get_contest_name(contest_name) -> str:
    contest_name = '【' + contest_name + '】開催まで、\n'

    return contest_name


def _add_contest_url(url: str) -> str:
    url = url + '\n'

    return url
