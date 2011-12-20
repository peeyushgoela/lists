# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from todo_lists.models import List, User
from todo_lists.forms import *

def index(request):
    if 'id' in request.session:
        return HttpResponseRedirect('/todo_lists/home/')
##    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    p="hi"
    return render_to_response("index.html",{'p':p})
##render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

@csrf_exempt
def login(request):
    if "id" in request.session:
        return HttpResponseRedirect('/todo_lists/home/')

    if request.method=='POST':
        form=login_form(request.POST)

        if form.is_valid():
            cd=form.cleaned_data
            p=User.objects.filter(username=cd['username'])
            if p:
                if p[0].password==cd['password']:
                    request.session["id"]=p[0].id
                    return HttpResponseRedirect('/todo_lists/home/')

            return HttpResponse("Invalid User")
            
    else:
        form=login_form();
            
    return render_to_response("login.html",{'form':form})

@csrf_exempt
def signup(request):
    if "id" in request.session:
        return HttpResponseRedirect('/todo_lists/home')
    if request.method=='POST':
        form=signup_form(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            p=User(username=cd['username'],password=cd['password'],email=cd['email'])
            p.save()
            return HttpResponseRedirect('/todo_lists/')
    else:
        form=signup_form();
            
    return render_to_response("signup.html",{'form':form})

def home(request):
    if "id" in request.session:
        p=List.objects.filter(user_id=request.session["id"])
        return render_to_response('home.html',{'lists':p})
    else:
        return HttpResponseRedirct("/todo_lists/")

def logout(request):
    if "id" in request.session:
        del request.session["id"]

    return HttpResponseRedirect('/todo_lists/')

@csrf_exempt
def edit(request,list_id):
    if "id" in request.session:
        if request.method=='POST':
            form=edittask_form(request.POST)
            if form.is_valid():
                cd=form.cleaned_data
                p=List.objects.get(pk=list_id)
                if cd['is_complete']:
                    ic=1
                else:
                    ic=0
                p.item=cd['item']
                p.isComplete=ic
                p.priority=cd['priority']
                p.save()
                return HttpResponseRedirect('/todo_lists/home')
        else:
            p=List.objects.get(pk=list_id)
            if p.isComplete:
                ic=True
            else:
                ic=False
            form=edittask_form(initial={'item':p.item, 'priority':p.priority, 'is_complete':ic});
            return render_to_response("edit_task.html",{'form':form,'list_id':list_id})
    else:
        return HttpResponseRedirect('/todo_lists/')

    return HttpResponse('SOme Error occurred')

def delete_task(request, list_id):
    s="deleting "+list_id 
    return HttpResponse(s)


@csrf_exempt
def add_task(request):
    if "id" in request.session:
        if request.method=='POST':
            form=addtask_form(request.POST)
            if form.is_valid():
                cd=form.cleaned_data
                p=User.objects.get(pk=request.session["id"])
                p.list_set.create(item=cd['item'],priority=cd['priority'],isComplete=0)
                return HttpResponseRedirect('/todo_lists/home')
        else:
            form=addtask_form();
            return render_to_response("add_task.html",{'form':form})
    else:
        return HttpResponseRedirect('/todo_lists/')
        
##Create your views here.
##from django.http import HttpResponse
##
##def index(request):
##    return HttpResponse("DID IT!!!YEAH.")
