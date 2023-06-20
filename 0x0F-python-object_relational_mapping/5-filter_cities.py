#!/usr/bin/python3

"""module to list all cities in a database"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    i = 0
    parameter = sys.argv[4]
    try:
        while (parameter[i] != ';'):
            i += 1
        if (parameter[i + 1]):
            sys.exit()
    except IndexError:
        pass

    try:
        cur.execute("SELECT cities.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = '{}' \
                    ORDER BY cities.id".format(parameter))
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print(str(e))

    print(", ".join([row[0] for row in rows]))
