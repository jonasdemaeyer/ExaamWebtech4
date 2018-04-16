# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def callback(request):

    verification_code = request.GET.get('verification_code')
    userid = request.GET.get('userid')

    context = {
        'verification_code': verification_code,
        'userid': verification_url,
    }

    return render_to_response('callback.html', context, context_instance=RequestContext(request))