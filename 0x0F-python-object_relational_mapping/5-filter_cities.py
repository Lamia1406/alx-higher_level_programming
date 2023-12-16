#!/usr/bin/python3
""" This script takes in the name of a state as an argument and
    lists all cities of that state
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities WHERE state_id IN\
                   (SELECT id FROM states WHERE name = %s)\
                   ORDER BY id", (sys.argv[4],))
    results = []
    for row in cursor.fetchall():
        results.append(row[0])
    print(*results, sep=", ")
    cursor.close()
    db.close()
