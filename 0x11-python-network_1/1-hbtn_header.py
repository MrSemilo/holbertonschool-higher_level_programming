  #!/usr/bin/python3
"""
python
"""


from urllib import request
from sys import argv


if __name__ == "__main__":
    """ ...  """

    url = request.Request(argv[1])

    with request.urlopen(url) as test:
        print(test.headers['X-Request-Id'])
