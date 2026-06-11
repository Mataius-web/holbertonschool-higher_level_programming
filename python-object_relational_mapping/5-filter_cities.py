#!/usr/bin/python3
"""Fetches all the cities of a specific state"""
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
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON states.id = cities.state_id "
                "WHERE states.name = %s ORDER BY cities.id ASC", (argv[4],))

    rows = cur.fetchall()

    print(", ".join(row[0] for row in rows))

    cur.close()
    db.close()
