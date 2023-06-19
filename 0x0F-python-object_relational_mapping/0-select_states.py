#!/usr/bin/python3

"""Module that lists all states in database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM states")
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        pass

    for row in rows:
        print(row)
