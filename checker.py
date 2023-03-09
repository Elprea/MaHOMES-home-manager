import sqlite3


def xzzx(yy, zz, kk):
	conn = sqlite3.connect('MaHomes.db')
	cur = conn.cursor()

	cur.execute("delete from parentAlert")

	conn.commit()
	conn.close()


xzzx("zero", "activate", "five")