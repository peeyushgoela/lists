# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse, Http404
from todo_lists.models import List, User

def index(request):
##    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    p="hi"
    return render_to_response("index.html",{'p':p})
##render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

def login(request):
    return HttpResponse("inside login page")

@csrf_exempt
def signup(request):
    return render_to_response("signup.html")

def home(request):
    return HttpResponse("inside home page")

def logout(request):
    return HttpResponse("inside logout page")

@csrf_exempt
def signup_function(request):
    User.save(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
    ##p=User(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
    ##p.save()
    return HttpResponse("saved:)")


##Create your views here.
##from django.http import HttpResponse
##
##def index(request):
##    return HttpResponse("DID IT!!!YEAH.")
