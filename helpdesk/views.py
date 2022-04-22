from multiprocessing import context
import re
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from helpdesk.models import Ticket
from datetime import date



# consts
categories = {'transaction':"medium",'accounts':'medium','FD':'low','demat':'high','other':'other'}

def Home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    context = {
        'tickets': Ticket.objects.filter(author=request.user),
    }
    if request.user.is_staff:
         context = {'tickets': Ticket.objects.all()}       
    context['categories'] = categories
    return render(request, 'home.html',context=context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        # if user is authenticated
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            context= {'case':False}
            return render(request,'login.html',context)
    context= {'case':True}
    return render(request,'login.html',context)

def Logout(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    logout(request)
    return redirect('/')




def Raise(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method =="POST":
        vals = {
        "subject" : request.POST.get('subject'),
        "description" : request.POST.get('description'),
        "category" :request.POST.get('category'),
        "status" : 'open',
        "author" : request.user,
        "date" : date.today(),
        "priority": request.POST.get('priority')}   

        newTicket = Ticket(**vals)
        newTicket.save()
        return redirect('/')
    context= {"categories":categories}
    return render(request, 'raise.html',context=context)


def TicketID(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        ticket = Ticket.objects.get(id=id)
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        ticket.status = status
        ticket.priority = priority
        ticket.save()
        return redirect('/')

    id = request.GET.get('id','')
    context  = {'categories':categories,
                'ticket':Ticket.objects.get(id=id)}
    prArr = ['high','medium','low']
    stArr = ['open','active','closed']
    if request.user.is_staff:
        prArr.remove(context['ticket'].priority)
        prArr.append(context['ticket'].priority)
        stArr.remove(context['ticket'].status)
        stArr.append(context['ticket'].status)
        context['prArr'] = prArr
        context['stArr'] = stArr
    return render(request, 'ticket.html',context=context)

