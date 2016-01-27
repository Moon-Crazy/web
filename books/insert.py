#coding=utf-8
#测试插入数据
from books.models import Publisher

p1 = Publisher(name='Apress',address='2855 Telegraph Avenu',
	city='Berkeley',state_province='CA',country='U.S.A',
	website='http;//www.apress.com')

p1.save()

publisher_list = Publisher.objects.all()
publisher_list

print publisher_list