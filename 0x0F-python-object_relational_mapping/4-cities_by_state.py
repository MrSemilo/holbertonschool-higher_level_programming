#!/usr/bin/python3

""" write a script that takes in arguments and displays
    all values in the states table of hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    n = MySQLdb.connect(host='localhost', port=3306,
                        user=argv[1], passwd=argv[2], db=argv[3])

    r = n.cursor()
    r.execute("SELECT cities.id , cities.name, states.name\
              FROM cities JOIN states ON cities.state_id = states.id")
    _rows = r.fetchall()
    for row in _rows:
        print(row)
