#!/usr/bin/python3
"""python"""

import requests
from sys import argv

if __name__ == "__main__":
    """ ...  """
    link = 'http://0.0.0.0:5000/search_user'
    try:
        url = requests.post(link, data={'q': argv[1]})
    except IndexError:
        url = requests.post(link, data={'q': ""})
    try:
        json_ = url.json()
        if not json_:
            print('No result')
        else:
            print('[{}] {}'.format(json_.get('id'), json_.get('name')))
    except ValueError:
        print('Not a valid JSON')
