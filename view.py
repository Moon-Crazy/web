from django.http import HttpResponse ,Http404
from django.template import Template,Context
from django.template.loader import get_template
import datetime
from django.shortcuts import render_to_response
from books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
def hello(request):
    return HttpResponse('Hello world')


def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>'% now
    return HttpResponse(html)

def hours_ahead(request,offset):
 	try:
 		offset = int(offset)
 	except ValueError:
 		raise Heep404()
 	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
 	html = '<html><body>In %s hour(s) ,it will be %s.</body></html>'%(offset,dt)
 	return HttpResponse(html)

def template_datetime(request):
	now = datetime.datetime.now()
	t = Template('<html><body>It is now {{ current_datetime }}.</body></html>')
	html = t.render(Context({'current_datetime':now}))
	return HttpResponse(html)
def html_datetime(request):
	now = datetime.datetime.now()
	fp = open('mytemplate.html')
	t = Template(fp.read())
	fp.close()
	html = t.render(Context({'current_date':now}))
	return HttpResponse(html)

def dir_datetime(request):
	now = datetime.datetime.now()
	t = get_template('mytemplate.html')
	html = t.render(Context({'current_date':now}))
	return HttpResponse(html)

def model_meta(request):
	t = get_template('meta.html')
	html = t.render(Context({'values':request.META.items()}))
	return HttpResponse(html)

def current_url_view_good(request):
	return HttpResponse('''
		Welcome to the page at %s . \n 
		The host is %s.'''% (request.path,request.get_host()))

def display_meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k , v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,v))
	return HttpResponse('<table>%s</table>'%'\n'.join(html))

def  search_form(request):
	return render_to_response('search_form.html')
'''
def search(request):
	if 'q' in request.GET:
		message = 'You searched for: %r' % request.GET['q']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)
'''
'''
def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		books = Book.objects.filter(title__icontains=q)
		return render_to_response('search_results.html',
			{'books':books,'query':q})
	else:
		return render_to_response('search_form.html',{'error':True})
		#return HttpResponse('Pleasea submit a search term.')

'''

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html',
				{'books':books,'query':q})
	return render_to_response('search_form.html',
		{'errors':errors})
	
def contact(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject',''):
			errors.append('Enter a subject.')
		if not request.POST.get('message',''):
			errors.append('Enter a message.')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid e-mail address.')
		if not errors:
			send_mail(
				request.POST['subject'],
				request.POST['message'],'qqccni@163.com',['gscchen@163.com','744073202@qq.com'],fail_silently=True)
			return render_to_response('thanks.html')
		#else:
			#return render_to_response('cs.html')
	return render_to_response('contact_form.html',
		{'errors':errors})

def setEmail(request):
	if request.method == 'POST':

		send_mail('subject','this is the message of mail','qqccni@163.com',['gscchen@163.com','744073202@qq.com'],fail_silently=True)

		return HttpResponse(u'fsyjcg')
	return render_to_response('contact_form.html')

def thanks(request):
	return render_to_response('thanks.html')

