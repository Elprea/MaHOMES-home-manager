# main database - create tables

import sqlite3

def main():
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	# create database tables
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
		)""")

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
		)""")

	cur.execute("""
		create table if not exists relationship(
			parentID int,
			childID int,
			foreign key(parentID) references parent(parentID),
			foreign key(childID) references student(childID)
		)""")

	cur.execute("""
		create table if not exists tasks(
			taskContent text,
			taskStatus text,
			taskOccurence text,
			taskReward text,
			parentID int,
			childID int,
			foreign key(parentID) references parent(parentID),
			foreign key(childID) references student(childID)
		)""")

	cur.execute("""
		create table if not exists messages(
			msgSender text,
			msgTitle text,
			msgContent text,
			msgStatus text,
			parentID int,
			childID int,
			foreign key(parentID) references parent(parentID),
			foreign key(childID) references student(childID)
		)""")

	cur.execute("""
		create table if not exists parentAlert(
			alertContent text,
			parentID int,
			foreign key(parentID) references parent(parentID)
		)""")

	cur.execute("""
		create table if not exists childAlert(
			alertContent text,
			childID int,
			foreign key(childID) references student(childID)
		)""")


	conn.commit()
	conn.close()

if __name__ == "__main__":
	main()
