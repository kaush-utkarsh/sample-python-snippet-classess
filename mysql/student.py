#!/usr/bin/python3

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
				try:
					user_chv = int(input("Press 1 if you wish to see the group name of this student\n")) 	
					if user_chv is not 1:
						print("wrong value entered")
					else:
						sql = """SELECT GROUP_NAME FROM Student_Group
						WHERE GROUP_ID = '%d'""" % int(rows[0]['GROUP_ID'])
						try:	
							# Execute the SQL command
							cur.execute(sql)
							# Fetch all the rows in a list of lists.
							results = cur.fetchall()
							print(results[0][0])	
						except:
							print("unable to fetch data")		
				except:
					print("wrong value entered")

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
		db.close()
		exit()