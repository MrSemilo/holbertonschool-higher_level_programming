#!/usr/bin/python3
"""tsts 2"""

if __name__ == '__main__':
    """main"""

    import MySQLdb
    from sys import argv

    n = MySQLdb.connect(host="localhost", port=3306,
                        user=argv[1], passwd=argv[2], db=argv[3])

    u = n.cursor()
    u.execute("""SELECT * FROM states WHERE name LIKE BINARY
              'N%' ORDER BY states.id ASC""")
    _rows = u.fetchall()
    for row in _rows:
        print(row)
