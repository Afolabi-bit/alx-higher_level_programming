#!/usr/bin/python3
# This script lists all states from the database
# hbtn_0e_0_usa

import MySQLdb
import sys

if __name__ == "__main":
	args = sys.argv[1:]
	db = MySQLdb.connect(user="root", passwd="", db="hbtn_0e_0_usa")
	cursor = db.cursor()

	cursor.execute("SELECT * FROM states")
	states = cursor.fetchall()
	print(states)
