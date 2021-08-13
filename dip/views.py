from dip.forms import ColForm
from typing import ContextManager
from django.shortcuts import render
from .models import Columnist,Article
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