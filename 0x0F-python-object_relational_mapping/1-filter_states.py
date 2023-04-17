#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    cur = db.cursor()
    starting_letter = 'N'
    cur.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        (starting_letter + '%',))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
