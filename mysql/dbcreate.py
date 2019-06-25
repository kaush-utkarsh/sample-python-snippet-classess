#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","root","SuperKids" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# # Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE Student (
S_NAME  CHAR(20) NOT NULL,
SUPERPOWER  CHAR(20),
GROUP_ID INT NOT NULL,
ROLL_NUMBER INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY (ROLL_NUMBER)
)"""

cursor.execute(sql)

sql = """CREATE TABLE Student_Group (
Group_NAME  CHAR(20) NOT NULL,
Group_Theme  CHAR(20),
GROUP_ID INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY (GROUP_ID)
)"""

cursor.execute(sql)

# disconnect from server
db.close()