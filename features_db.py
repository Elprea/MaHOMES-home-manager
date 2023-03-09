# create tasks and messages tables

import sqlite3


def add_tasks(content, status, occurence, reward, pid, cid):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	cur.execute("insert into tasks values(?,?,?,?,?,?)",
		(content,status,occurence,reward,pid,cid)
	)

	content = 'You have a new task!'
	cur.execute("insert into childAlert values(?,?)",
		(content, cid)
	)

	conn.commit()
	conn.close()

def add_messages(sender,title, content, status, pid, cid):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	cur.execute("insert into messages values(?,?,?,?,?,?)",
		(sender,title,content,status,pid,cid)
	)

	conn.commit()
	conn.close()

def delete_tasks_parent(pid, rowid):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	# delete happening from parent gui
	cur.execute("delete from tasks where parentID=:parentID and rowid=:rowid",
			{
			"parentID": pid,
			"rowid": rowid
			}
		)

	conn.commit()
	conn.close()

def delete_msg_parent(pid, rowid):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	# delete happening from parent gui
	cur.execute("delete from messages where parentID=:parentID and rowid=:rowid",
			{
			"parentID": pid,
			"rowid": rowid
			}
		)

	conn.commit()
	conn.close()

def complete_tasks_child(cid, rowid):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	# delete happening from child gui
	cur.execute("update tasks set taskStatus='Completed' where childID=:childID and rowid=:rowid",
			{
			"childID": cid,
			"rowid": rowid
			}
		)
	
	# get values ready to transfer to alert table
	cur.execute("select child.firstname, parentID, taskContent from tasks inner join child on tasks.childID=child.childID where child.childID=:childID and tasks.rowid=:rowid",{
		"childID": cid,
		"rowid": rowid
		})
	vals = cur.fetchone()
	content = 'Your child '+str(vals[0])+' has completed the task ['+str(vals[2])+']'
	cur.execute("insert into parentAlert values(?, ?)",
		(content, vals[1])
	)
	
	conn.commit()
	conn.close()

def delete_tasks_child(cid, rowid):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	# get values ready to transfer to alert table
	cur.execute("select child.firstname, parentID, taskContent from tasks inner join child on tasks.childID=child.childID where child.childID=:childID and tasks.rowid=:rowid",{
		"childID": cid,
		"rowid": rowid
		})
	vals = cur.fetchone()
	content = 'Your child '+str(vals[0])+' has evaded the task ['+str(vals[2])+']'
	cur.execute("insert into parentAlert values(?, ?)",
		(content, vals[1])
	)

	# delete happening from child gui
	cur.execute("delete from tasks where childID=:childID and rowid=:rowid",
			{
			"childID": cid,
			"rowid": rowid
			}
		)

	conn.commit()
	conn.close()


def delete_msg_child(cid, rowid):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	# delete happening from child gui
	cur.execute("delete from messages where childID=:childID and rowid=:rowid",
			{
			"childID": cid,
			"rowid": rowid
			}
		)

	conn.commit()
	conn.close()



def parent_alert(content, pid):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	cur.execute("insert into alert values(:content, :pid)",
			{
			"alertContent": content,
			"parentID": pid
			}
		)

	conn.commit()
	conn.close()

def child_alert(content, cid):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	cur.execute("insert into alert values(:content, :cid)",
			{
			"alertContent": content,
			"childID":cid
			}
		)

	conn.commit()
	conn.close()

def add_relationship(pid, cid):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	cur.execute("select * from relationship where parentID=:parentID and childID=:childID",{
			"parentID":pid,
			"childID":cid
		})

	count = 0
	error = 0
	for i in cur.fetchall():
		if i:
			error=1
			break
		count+=1
	if error == 0:
		cur.execute("insert into relationship values(?,?)",
			(pid,cid)
		)

	conn.commit()
	conn.close()