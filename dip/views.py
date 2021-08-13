from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from dip.forms import ColForm
from typing import ContextManager
from django.shortcuts import render
from .models import Columnist,Article
from .forms import UserFormOmercik
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request,'dip/home.html')


def index(request):
    q = Columnist.objects.all()
    context = {
        'data':q,
    }
    return render (request, 'dip/index.html',context)

def articles(request,colid):
    x = Columnist.objects.get(pk=colid)
    q = Article.objects.filter(article_writer = x)
    context = {
        'data1':x,
        'data2':q,
    }
    return render(request,'dip/articles.html',context)

def articleDetail(request,arid):
    q = Article.objects.get(pk=arid)
    context = {
        'data':q,
    }
    return render (request,'dip/article_detail.html',context)

def articleIndex(request):
    q = Article.objects.all()
    context = {
        'data':q,
    }
    return render(request,'dip/article_index.html',context)


def newColumnist(request):
    if request.method =="POST":
        form = ColForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = ColForm()
    context = {
        'data':form
    }
    return render(request,'dip/new_columnist.html',context)


def register(request):
    if request.method == "POST":
        omer_osman_form = UserFormOmercik(request.POST)
        if omer_osman_form.is_valid():
            omer_osman_form.save()
            return home(request)
    else:
        omer_osman_form = UserFormOmercik()
    
    context = {
        'data':omer_osman_form,
    }

    return render(request,'dip/register.html',context)

def userList(request):
    q = User.objects.all()
    context ={
        'data':q,
    }
    return render(request,'dip/userlist.html',context)


def login(request):
    if request.method == "POST":
        q = AuthenticationForm()
    context = {
        'data':q,
    }

    return render(request,'registration/login.html',context)