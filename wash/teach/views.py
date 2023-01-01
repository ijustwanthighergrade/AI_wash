from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return render(request,"index.html",locals())

def teach(request):
   return render(request,"teaching.html",locals())
