#!/usr/bin/python3
"""takes in an argument and displays all values in the states"""

if __name__ == '__main__':
    """main"""

    import MySQLdb
    from sys import argv

    n = MySQLdb.connect(host="localhost", port=3306,
                        user=argv[1], passwd=argv[2], db=argv[3])

    u = conn.cursor()
    u.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC".format(argv[4]))
    _rows = cur.fetchall()
    for row in _rows:
        print(row)
