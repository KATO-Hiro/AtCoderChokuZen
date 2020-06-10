import requests


# See:
# https://requests.readthedocs.io/en/master/
def fetch():
    ATCODER_BASE_URL = 'https://atcoder.jp/'
    HOME_PAGE = ATCODER_BASE_URL + 'home'
    response = requests.get(HOME_PAGE)
    print(response.text)


def main():
    fetch()


if __name__ == '__main__':
    main()
