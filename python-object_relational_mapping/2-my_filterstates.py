#!/usr/bin/python3
"""Files that searches for a specific data from the user"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3],
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY "
                "'{}' ORDER BY id ASC".format(argv[4]))

    rows = cur.fetchall()
    for data in rows:
        print(data)
