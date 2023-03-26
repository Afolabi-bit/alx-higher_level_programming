#!/usr/bin/python3
"""
This script lists all states from the database
hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main":
    """
        Access db and print states
    """
    args = sys.argv[1:]
    db = MySQLdb.connect(
        host="localhost", user=args[0], port=3306, passwd=args[1], db=args[2])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for state in states:
        print(state)
