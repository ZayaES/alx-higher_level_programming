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

    i = 0
    cur = db.cursor()
    state_name = sys.argv[4]
    while(sys.argv[4][i] != ';' and sys.argv[4][i] != ' '):
        if (i == len(sys.argv[4]) - 1):
            break
        i += 1
    query = query_temp.format(state_name)
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
