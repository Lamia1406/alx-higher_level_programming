#!/usr/bin/python3
""" This script takes in an argument and displays all values
    in the states table where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}'\
                   ORDER BY id".format(sys.argv[4]))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
