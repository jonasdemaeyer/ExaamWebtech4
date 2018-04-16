from django.conf.urls.defaults import *

from vieuw import callback

urlpatterns = patterns('',
	url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail');
