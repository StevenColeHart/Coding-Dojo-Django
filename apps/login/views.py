# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
import bcrypt
from .models import *

def index(request) :
   
    return render(request, 'login/index.html')
   
def register(request) :
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=password,birth_day=request.POST['birth_day'])
        user.save()
        print user
        request.session['current_user'] = User.objects.filter(email=request.POST['email'])[0].id
        return redirect('/success')


def login(request) :
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['current_user'] =  User.objects.filter(email=request.POST['email'])[0].id

        return redirect('/success')

def success(request):
    if "current_user" not in request.session:
        return redirect('/')
    this_user=User.objects.get(id=request.session['current_user'])
    context = {
        'user' : User.objects.get(id=request.session['current_user']),
        'quotes': Quote.objects.all().exclude(favorites=this_user),
        'myfavs': Quote.objects.all().filter(favorites=this_user)
        
        # *******************
        # were giving the name courses the value of the course model database so you can pass it to the template so that the html can use.
        # ***********
    }
    return render(request, 'login/success.html', context)

def add(request):
    return render(request, 'login/add.html')

def logout(request):
    del request.session["current_user"]
    return redirect('/')

def user(request,id):
    current_user=User.objects.get(id=id)
    context = {
        "quotes" : Quote.objects.all().filter(quote_creator=current_user),
        "creator" : User.objects.get(id=id),
        "total_quotes" : Quote.objects.all().filter(quote_creator=current_user).count()
    }
    return render(request, "login/user.html", context)

def new(request):
    if request.method== 'POST':
        errors = Quote.objects.Course_validator(request.POST)
        if len(errors):
            for error in errors:
                messages.error(request, error)
            return redirect('/success')
        quote_author=request.POST['quote_author']
        quote_message=request.POST['quote_message']
        quote_creator=User.objects.get(id=request.session['current_user'])
        Quote.objects.create(quote_author=quote_author,quote_message=quote_message,quote_creator=quote_creator)
        print request.POST
    return redirect('/success')

def fav(request, id):
    name = User.objects.get(id=request.session["current_user"])
    quote = Quote.objects.get(id=id)
    name.favorites.add(quote)
    return redirect("/success")

def drop(request,id):
    name=User.objects.get(id=request.session["current_user"])
    quote = Quote.objects.get(id=id)
    name.favorites.remove(quote)
    return redirect("/success") 