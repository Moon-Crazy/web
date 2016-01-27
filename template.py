from django.template import Template ,Context
from django.conf import settings
settings.configure()

t = Template('''{% if today %}
					<p>Welcome to the weekend!</p>
				{% endif %}''')
c = Context({'today':True})
print t.render(c)

tt = Template('''{% if athlete_list and coach_list %}
	                  <p>Both athltes and coches are available.</p>
	             {% else %}
	                  <p> Get back work!</p>
	          	 {% endif %}''')
cc = Context({'athlete_list':True})
#del cc['athlete_list']
#print cc
cc['coach_list'] = True
print tt.render(cc)


for_t = Template('''{% for a in a_list %}
	<li>{{a.upper}}</li>
	{% endfor %}''')
for_c = Context({'a_list':['a','b','c']})
print for_t.render(for_c)

ck_t = Template('{% if a %}{%for c in a%}<p>{{c}}</p>{%endfor%}{%else%}<p>empty</p>{%endif%}')
ck_c = Context({'a':None})
print ck_t.render(ck_c)

em_t = Template('{% for i in a %} <p>{{i}}{{forloop.counter}}</p> {% empty %} <p>empty</p> {% endfor %}')
em_c = Context({'a':['a','b','c','d']})
print em_t.render(em_c)

last_t = Template('{% for link in links %}{{link}}{% if not forloop.last %} | {% endif %}{% endfor %}')
last_c = Context({'links':['link1','link2','link3','link4']})
print last_t.render(last_c)

d_t = Template('{% for p in places %}{{ p }}{% if not forloop.last %},{% endif %}{% endfor %}')
d_c = Context({'places':['one','two','three']})
print d_t.render(d_c)

parent_t = Template('''
	{% for country in countries %}
	<table>
	{% for city in country.city_list %}
		<tr>
		<td>Country #{{forloop.parentloop.couter}}</td>
		<td>City #{{ forloop.counter }}</td>
		<td>{{ city }}</td>
		</tr>
	{% endfor %}
	</talbe>
	{% endfor %}
	''')
parent_c = Context({'countries':{'city_list':1}})
print parent_t.render(parent_c)

ifequal_t = Template('{% ifequal user currentuser %}Welcome{% else %}No Welcom{# This is comment #}{% endifequal %}')
ifequal_c = Context({'user':'aaa'})
ifequal_c['currentuser'] = 'aa'
print ifequal_t.render(ifequal_c)


