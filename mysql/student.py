
#!/usr/bin/python3

# 1. Input Student
# 2. if group id non existent then we will ask to enter new group id between the range 1 to 5.

import pymysql

def create_student(cur,dab):
	sname = input("\nEnter student name\n")
	spower = input("\nEnter super powers\n")
	while(True):
		try:
			groupid = int(input("\nEnter group id\n"))
			sql = """SELECT * FROM Student_Group
			WHERE GROUP_ID = '%d'""" % (groupid)
			try:	
				# Execute the SQL command
				cur.execute(sql)
				# Fetch all the rows in a list of lists.
				results = cur.fetchall()	
				if len(results) is 0:
					print("\nNo such group, enter value again.\n")
					continue
				else:
					break
			except:
				continue
		except:
			continue
		break
	# print(sname,spower,groupid)

	sql = """INSERT INTO Student(S_NAME,
	SUPERPOWER, GROUP_ID)
	VALUES ('"""+sname+"""', '"""+spower+"""', """+str(groupid)+""")"""
	try:
		# Execute the SQL command
		cur.execute(sql)
		# Commit your changes in the database
		dab.commit()
	except:
		# Rollback in case there is any error
		dab.rollback()

def view_students(cur,dab):
	sql = """SELECT * FROM Student
			WHERE 1"""
	try:	
		# Execute the SQL command
		cur.execute(sql)
		# Fetch all the rows in a list of lists.
		results = cur.fetchall()	
		if len(results) is 0:
			print("\n No Data Found \n")
		else:
			field_names = []
			for col in cur.description:
				field_names.append(col[0])
			rows = []
			for row in results:
				col = {}
				col[field_names[0]] = row[0]
				col[field_names[1]] = row[1]
				col[field_names[2]] = row[2]
				col[field_names[3]] = row[3]
				rows.append(col)
			print(rows)
	except:
		print("\nUnable to fetch. Try Again\n")

def select_student(cur,dab):
	while(True):
		try:
			rollnum = int(input("\nEnter student roll number\n"))
			sql = """SELECT * FROM Student
			WHERE ROLL_NUMBER = '%d'""" % (rollnum)
			try:	
				# Execute the SQL command
				cur.execute(sql)
				# Fetch all the rows in a list of lists.
				results = cur.fetchall()	
				if len(results) is 0:
					print("\nNo such student, enter value again.\n")
					continue
				else:
					field_names = []
					for col in cur.description:
						field_names.append(col[0])
					print(field_names)
					rows = []
					print(results)
					for row in results:
						col = {}
						col[field_names[0]] = row[0]
						col[field_names[1]] = row[1]
						col[field_names[2]] = row[2]
						col[field_names[3]] = row[3]
						rows.append(col)
					print(rows)
				break
			except:
				continue
		except:
			continue
		break
	pass

# Open database connection
db = pymysql.connect("localhost","root","root","SuperKids" )
# prepare a cursor object using cursor() method
cursor = db.cursor()


while(True):
	try:
		user_ch = int(input("\nEnter your choice:\n 1. Create New Student, \n 2. View Students \n 3. Select a Student \n 4. Terminate Program\n"))
	except:
		print("\nEnter valid inputs \n")
		continue
	if user_ch is 1:
		create_student(cursor,db)
	elif user_ch is 2:
		view_students(cursor,db)
	elif user_ch is 3:
		select_student(cursor,db)
	else:
		exit()



# # Prepare SQL query to INSERT a record into the database.
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#    LAST_NAME, AGE, SEX, INCOME)
#    VALUES ('Mc', 'Mahon', 20, 'M', 2000)"""
# try:
#    # Execute the SQL command
#    cursor.execute(sql)
#    # Commit your changes in the database
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()

# # disconnect from server
# db.close()
