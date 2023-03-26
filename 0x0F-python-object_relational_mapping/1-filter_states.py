#!/usr/bin/python3
"""
This script lists all states with a name starting with N
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
        Access db and print states
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                   ORDER BY states.id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
