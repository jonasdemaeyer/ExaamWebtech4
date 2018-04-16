from django.conf.urls.defaults import *

from vieuw import callback

urlpatterns = patterns('',
	url(r'callback$' view= callback, name= 'callback');
