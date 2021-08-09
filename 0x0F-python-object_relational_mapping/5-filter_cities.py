#!/usr/bin/python3

"""  script that takes in the name of a state as an
     argument and lists all cities of that state
"""
if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    n = MySQLdb.connect(host='localhost', port=3306,
                        user=argv[1], passwd=argv[2], db=argv[3])

    cur = n.cursor()
    cur.execute("SELECT cities.name\
                FROM cities JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    test = ""
    for row in rows:
        test += (row[0] + ", ")
    print(test[0:-2])
