#!/usr/bin/python3
# Get all states
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], port=3306
        )
    cur = db.cursor()
    cur.execute('SELECT cities.name FROM cities INNER JOIN states\
                ON cities.state_id = states.id WHERE states.name = (%s)\
                ORDER BY cities.id ASC;', [sys.argv[4]])
    rows = cur.fetchall()
    for i in range(len(rows)):
        print(rows[i][0], end="")
        if i < len(rows) - 1:
                print(', ', end="")
    print('')
