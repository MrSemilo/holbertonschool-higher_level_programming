#!/usr/bin/python3
"""python"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    """ ...  """

    git = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print(git.json().get('id'))
