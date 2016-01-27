from forms import ContactForm

f = ContactForm()
print f
print f['subject']

f = ContactForm({'subject':'Hello','email':'qqccni@163.com','message':'Nice site!'})
f.is_bound