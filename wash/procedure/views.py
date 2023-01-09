from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


def wash1(request):
    if request.method == 'GET':
       
       return render(request,"wash1.html",locals())

def wash2(request):
    if request.method == 'GET':
   
       return render(request,"wash2.html",locals())

def wash3(request):
    if request.method == 'GET':
      return render(request,"wash3.html",locals())

def wash4(request):
   return render(request,"wash4.html",locals())

def index(request):
   return render(request,"index.html",locals())

