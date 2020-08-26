import requests
from bs4 import BeautifulSoup

ATCODER_BASE_URL = 'https://atcoder.jp'


def fetch_upcoming_contest():
    ''' See:
        https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request
    '''
    response = _fetch_home_page()
    status_code = response.status_code

    if status_code == requests.codes.ok:
        upcoming_contests = _parse_upcoming_contests(response)

    if upcoming_contests:
        contest_info = _get_upcoming_contest_info(upcoming_contests)

        return status_code, contest_info

    # HACK: The below solution is not good?
    return status_code, None


def _fetch_home_page():
    ''' See:
        https://requests.readthedocs.io/en/master/
    '''

    HOME_PAGE = ATCODER_BASE_URL + '/home?lang=ja'
    response = requests.get(HOME_PAGE)

    return response


def _parse_upcoming_contests(response):
    ''' See:
        https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    '''

    soup = BeautifulSoup(response.text, 'html.parser')
    upcoming_contests = soup.find(id='contest-table-upcoming')

    return upcoming_contests


def _get_upcoming_contest_info(upcoming_contests):
    ''' HACK: The codes depend on AtCoder Home page.
        contest_info contains below information:

        ignore       : http://www.timeanddate.com/worldclock/fixedtime.html?
                       iso=202xxxxxTxxxx&px=xxx
        contest date : 202x-xx-xx xx:xx:xx+0900
        contest url  : /contests/abbreviated_contest_name
        contest name : hogehoge
    '''
    from contest import Contest

    contest_info = upcoming_contests.find_all('a', limit=2)
    name, start_date, url = '', '', ''

    for index, link in enumerate(contest_info):
        if index == 0:
            start_date = _fix_contest_date_format(link.text)
        elif index == 1:
            name = link.text
            url = ATCODER_BASE_URL + link['href']

    contest = Contest(name=name, start_date=start_date, url=url)

    return contest


# HACK: Not good solution.
#       It is necessary to add '+X:XX',
#       but builtin function may be existed.
def _fix_contest_date_format(date: str) -> str:
    ''' Expected: 202x-xx-xx xx:xx:xx+09:00
        Actual  : 202x-xx-xx xx:xx:xx+0900
    '''
    left = date[:-2]
    right = date[-2:]

    fixed_date_format = left + ':' + right

    return fixed_date_format
