from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from login.views import login2


def wash1(request):
   if 'mem_session' in request.session:
      return render(request,"wash1.html",locals())
   else:
      return login2(request)

def wash2(request):
  # if 'mem_session' in request.session:
      #if request.method == 'GET':
   
         return render(request,"wash2.html",locals())
   #else:
      #return login2(request)

def wash3(request):
   #if 'mem_session' in request.session:
      #if request.method == 'GET':
   
         return render(request,"wash3.html",locals())
   #else:
     # return login2(request)

def wash4(request):
   #if 'mem_session' in request.session:
      #if request.method == 'GET':
   
         #return render(request,"wash4.html",locals())
   #else:
      #return login2(request)

def index(request):
   if 'mem_session' in request.session:
         return render(request,"index.html",locals())
   else:
      return login2(request)
   

