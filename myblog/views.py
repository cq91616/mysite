#coding : utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Terrence的博客")
    return render(request,'index.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))


def  add2(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))

def top(request):
    return render(request,'_top.html')

def base(request):
    return  render(request,'base.html')