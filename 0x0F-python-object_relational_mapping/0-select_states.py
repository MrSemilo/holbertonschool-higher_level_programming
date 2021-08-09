#!/usr/bin/python3
"""test1"""
if __name__ == '__main__':
    """main"""

    import MySQLdb
    from sys import argv

    n = MySQLdb.connect(host='localhost', port=3306,
                        user=argv[1], passwd=argv[2], db=argv[3])

    cur = n.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    _rows = cur.fetchall()
    for row in _rows:
        print(row)
