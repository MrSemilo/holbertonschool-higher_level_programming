#!/usr/bin/python3
"""python"""


import urllib
from urllib import request
from sys import argv


if __name__ == "__main__":
    """ ...  """

    url = request.Request(argv[1])

    try:
        with request.urlopen(url) as new:
            print(new.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
