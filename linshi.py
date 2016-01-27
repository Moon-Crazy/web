#coding=utf-8
#小测试文件

from django.shortcuts import render_to_response #打开网页HTML
from django.http import Http404,HttpResponseRedirect

def Thanks(request,thanks):   #命名组传递参数
	return render_to_response('thanks.html',{'thanks':thanks})

def cs_disange(request,thanks,name):#url使用第三个参数
	return render_to_response(name,{'thanks':thanks})

def method_splitter(request,GET=None,POST=None):
	if request.method == 'GET' and 'GET' is not None:
		return GET(request)
	elif requet.method == 'POST' and 'POST' is not None:
		return POST(request)
	raise Http404

def some_page_get(request):
	assert request.method == 'GET'
	#do_smoething_for_get()
	return render_to_response('page.html')

def some_page_post(request):
	assert request.method == 'POST'
	#do_something_for_post()
	return render_to_response('/someurl/')

def wcs_s(request):
	return render_to_response('wcs.html')

