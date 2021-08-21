#!/usr/bin/python3
"""python"""


from urllib import request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    """ ...  """

    data = {'email': argv[2]}
    arg1 = argv[1]
    value = urllib.parse.urlencode(data)
    value = value.encode('ascii')
    url = request.Request(arg1, value)

    with request.urlopen(url) as new:
        print(new.read().decode("utf-8"))
