#!/usr/bin/python3

"""Module that lists all states in database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = ("SELECT * FROM `states` WHERE `name` LIKE %s ORDER BY id")
    parameter = ("N%", )
    try:
        cur.execute(query, parameter)
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print(str(e))

    for row in rows:
        print(row)
