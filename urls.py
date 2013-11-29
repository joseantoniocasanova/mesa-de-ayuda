from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from mesa.views import index
admin.autodiscover()

urlpatterns = patterns('', 
	url(r'^administrador/',include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'helpdesk.views.home', name='home'),
    # url(r'^helpdesk/', include('helpdesk.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^',include('helpdesk.apps.home.urls')),	   
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
)
