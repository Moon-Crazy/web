#coding=utf-8
import MySQLdb

conn = MySQLdb.connect(
	#host = 'Py-mysql' ,
	port = 3306 ,
	user = 'root' ,
	passwd = '0909' ,
	db = 'samp_db',
	)

cur = conn.cursor()
#cur.execute('create table student(id int ,name varchar(20),class varchar(30),age varchar(10))')
cur.execute("insert into student values( 3 ,'Jack','3 class 2 year','9')")
cur.close()
conn.commit()
conn.close()
