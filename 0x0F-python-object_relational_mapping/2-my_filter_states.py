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
    try:
        cur = db.cursor()
        state_name = sys.argv[4]
        query_temp = "SELECT * FROM states WHERE name= '{}' ORDER BY id ASC"
        query = query_temp.format(state_name)
        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:
            print(row)
    except MySQLdb.Error, e:
        try:
            print(e.args[0], e.args[1])
        except IndexError:
            print(str(e))

    cur.close()
    db.close()
