from collections import namedtuple

# See:
# https://docs.python.org/3.7/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields
Contest = namedtuple('Contest', ['name', 'start_date', 'url'])
