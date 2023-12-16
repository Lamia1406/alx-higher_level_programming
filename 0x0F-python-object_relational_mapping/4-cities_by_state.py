#!/usr/bin/python3
""" This script lists all cities ordered by id in ascending order"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities, states WHERE cities.state_id = states.id\
                   ORDER BY id")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
