#!/usr/bin/python3

import pymysql, random

# Open database connection
db = pymysql.connect("localhost","root","root","randnums" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

for i in range(1,201):
	rn = random.randint(1,200)
	# Prepare SQL query to INSERT a record into the database.
	sql = """INSERT INTO numb(id,val) VALUES ("""+str(i)+""","""+str(rn)+""")"""

	# Execute the SQL command
	cursor.execute(sql)
	# Commit your changes in the database
	db.commit()

coun = 0
li = []
while coun<11:
	try:
		inp = int(input("Enter a number between 1 to 200"))
		if inp>0 and inp<201:
			li.append(str(inp))
			coun +=1
		else:
			print("enter valid num")
	except:
		print("enter valid num")
		continue
placeholder = ','.join(li)
sql = "Select * from numb where id IN ("+placeholder+")"
# print(sql)
col = {}


print(sql)
# Execute the SQL command
cursor.execute(sql)
# Fetch all the rows in a list of lists.
results = cursor.fetchall()	
print(results)
if len(results) is 0:
	print("\n No Data Found \n")
else:
	for row in results:
		col[row[0]] = row[1]

db.close()
di = dict()
for i in range(1,11):
	di[i]=int(li[i])+col[int(li[i])]
print(di)