#coding=utf-8
from django.conf.urls.defaults import *
#from view import current_datetime,hello,hours_ahead,template_datetime,dir_datetime,html_datetime,current_url_view_good,display_meta,model_meta,search_form
from book_sql import book_list
from linshi import Thanks,cs_disange,method_splitter,some_page_get,some_page_post,wcs_s
#from view import search,contact,setEmail,thanks

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('view',
                       ('^$','hello'),
                       ('^current_time/$','current_datetime'),
                       ('^current_time(\d{1,2})/$','hours_ahead'),
                       ('^template_datetime/$','template_datetime'),
                       ('^html_datetime/$','html_datetime'),
                       ('^dir_datetime/$','dir_datetime'),
                       ('^book_list/$',book_list),
                       (r'^admin/',include(admin.site.urls)),
                       ('^page/$','current_url_view_good'),
                       ('^meta/$','display_meta'),
                       ('^model_meta','model_meta'),
                       (r'^search-form/$','search_form'),
                       ('^search/$','search'),
                       ('^contact/$','contact'),
                       ('^setEmail/$','setEmail'),
                       ('^thanks/$','thanks'),
                       ('^linshi/(?P<thanks>\w+)/$',Thanks), #命名组传递参数
                       ('^(?P<thanks>xiao\w+)/$',cs_disange,{'name':'No Thanks.html'}), #使用第三个参数
                       ('^(?P<thanks>[^xiao]\w+)/$',cs_disange,{'name':'thanks.html'}), #使用第三个参数
                       ('^@@/$',cs_disange,{'name':'No Thanks.html','thanks':'suru cuowu'}),#伪造捕捉的URLconf值
                       ('^@somepage/$',method_splitter,{'GET':some_page_get,'POST':some_page_post}),
                       #('^wcs_s/$',wcs_s),
                       #('^current_time/',include('wcs_s'))

)


