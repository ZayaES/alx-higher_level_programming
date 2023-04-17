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
    state = sys.argv[4]
    query_temp = (
        """SELECT cities.name
        FROM cities JOIN states ON states.id=cities.state_id
        AND states.name = '{}'
        ORDER BY cities.id ASC"""
    )
    query = query_temp.format(state)
    cur.execute(query)

    i = 0
    output = ""
    try:
        rows = cur.fetchall()
        for row in rows:
            if (i < len(rows) - 1):
                output += "{}, ".format(row[0])
                i += 1
        output += row[0]
        print(output)
    except Exception:
        pass

    cur.close()
    db.close()
