from django.shortcuts import render
from django.http import HttpResponse

def wash1(request):
   return render(request,"wash1.html",locals())

def wash2(request):
   return render(request,"wash2.html",locals())

def index(request):
   return render(request,"index.html",locals())
