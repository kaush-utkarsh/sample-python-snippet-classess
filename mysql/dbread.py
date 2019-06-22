#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","root","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """SELECT * FROM EMPLOYEE \
      WHERE INCOME > '%d'""" % (1000)
try:

   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   # print(results)
   # print(cursor.description)
   # exit()
   field_names = []
   for col in cursor.description:
      field_names.append(col[0])
   rows = []
   for row in results:
      col = {}
      col[field_names[0]] = row[0]
      col[field_names[1]] = row[1]
      col[field_names[2]] = row[2]
      col[field_names[3]] = row[3]
      col[field_names[4]] = row[4]
      rows.append(col)
      # fname = row[0]
      # lname = row[1]
      # age = row[2]
      # sex = row[3]
      # income = row[4]
      # Now print fetched result
      # print ("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % \
      #    (fname, lname, age, sex, income ))
   print(rows)
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()