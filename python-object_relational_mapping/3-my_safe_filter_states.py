#!/usr/bin/python3
"""Searches a specific data from a user, this one is safe from SQL injection"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3],
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s "
                "ORDER BY id ASC", (argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
