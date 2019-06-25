#!/usr/bin/python3

import pymysql
# 127.0.0.1:3306 	
# Open database connection
db = pymysql.connect("localhost","root","root" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("Create Database SuperKids")

# disconnect from server
db.close()