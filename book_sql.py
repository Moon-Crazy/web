from django.shortcuts import render_to_response
import MySQLdb

def book_list(request):
	db = MySQLdb.connect(
		user='root',
		db='samp_db',
		passwd='0909',
		host='localhost'
		)
	cursor = db.cursor()
	cursor.execute('select name from student order by name')
	names = [row[0] for row in cursor.fetchall()]
	db.close()
	return render_to_response('book_list.html',{'names':names})
