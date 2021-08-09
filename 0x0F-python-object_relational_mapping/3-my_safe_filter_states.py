#!/usr/bin/python3

""" write a script that takes in arguments and displays
    all values in the states table of hbtn_0e_0_usa """
if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    n = MySQLdb.connect(host='localhost', port=3306,
                        user=argv[1], passwd=argv[2], db=argv[3])

    u = conn.cursor()
    u.execute("SELECT * FROM states WHERE name=%s\
              ORDER BY states.id ASC", (argv[4],))
    _rows = u.fetchall()
    for row in _rows:
        print(row)
