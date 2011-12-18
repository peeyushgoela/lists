# Create your views here.
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse, Http404

def index(request):
##    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    p="hi"
    return render_to_response("index.html",{'p':p})
##render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})


##Create your views here.
##from django.http import HttpResponse
##
##def index(request):
##    return HttpResponse("DID IT!!!YEAH.")
