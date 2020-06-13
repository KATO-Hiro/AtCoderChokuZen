import os

from dotenv import find_dotenv
from dotenv import load_dotenv

# See:
# https://github.com/theskumar/python-dotenv
load_dotenv(find_dotenv())

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')
