# register database - add values to table 
import sqlite3

# check for id duplicate
def verify_id(role, uid):
	global conn
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	if role=="Parent":
		cur.execute("select * from parent where parentID=?", (uid,))
		if not cur.fetchone():
			return 1

	elif role=="Child":
		cur.execute("select * from child where childID=?", (uid,))
		if not cur.fetchone():
			return 1
	else:
		return 0

	conn.commit()
	conn.close()

# check for username duplicate
def check_username(role, username):
	global conn
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	if role=="Parent":
		cur.execute("select * from parent where username=:username", {"username": username})
		if cur.fetchone():
			return 1
		elif cur.execute("select * from child where username=:username", {"username": username}):
			if cur.fetchone():
				return 1
	elif role=="Child":
		cur.execute("select * from child where username=:username", {"username": username})
		if cur.fetchone():
			return 1
		elif cur.execute("select * from parent where username=:username", {"username": username}):
			if cur.fetchone():
				return 1
	else:
		return 0

	conn.commit()
	conn.close()

# insert values to parent table
def register_parent(pid, username, password, fname, lname, gender, dob, address, contact):
	global conn
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	cur.execute("""
		create table if not exists parent(
			parentID int primary key,
			username text,
			password text,
			firstName text,
			lastName text,
			gender text,
			dob text,
			address text,
			contact int
		)"""
	)

	cur.execute("insert into parent values(?,?,?,?,?,?,?,?,?)",
		(pid, username, password, fname, lname, gender, dob, address, contact)
	)

	conn.commit()
	conn.close()

# insert values to child table
def register_child(cid, username, password, fname, lname, gender, dob, address, contact):
	global conn
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	cur.execute("""
		create table if not exists child(
			childID int primary key,
			username text,
			password text,
			firstName text,
			lastName text,
			gender text,
			dob text,
			address text,
			contact int
		)"""
	)

	cur.execute("insert into child values(?,?,?,?,?,?,?,?,?)",
		(cid, username, password, fname, lname, gender, dob, address, contact)
	)

	conn.commit()
	conn.close()

