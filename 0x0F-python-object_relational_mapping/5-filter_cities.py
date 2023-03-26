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

    cursor.execute("SELECT c.id, c.name, s.name FROM cities as c\
                    inner join states as s\
                    ON c.state_id = s.id\
                    WHERE s.name = %s", (sys.argv[4],))
    cities = cursor.fetchall()
    for c in cities:
        print(c)
    cursor.close()
    db.close()
