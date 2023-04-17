#!/usr/bin/python3
import MySQLdb
import sys

# Check if correct number of command line arguments are provided
if len(sys.argv) != 4:
    print("Usage: python script.py <username> <password> <database>")
    sys.exit(1)

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

cur = db.cursor()
starting_letter = 'N'
cur.execute(
    "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", (starting_letter + '%',)
)
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
db.close()

