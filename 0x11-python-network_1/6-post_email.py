#!/usr/bin/python3
"""python"""

import requests
from sys import argv

if __name__ == "__main__":
    """ python  """

    url = requests.post(argv[1], data={'email': argv[2]})
    print(url.text)
