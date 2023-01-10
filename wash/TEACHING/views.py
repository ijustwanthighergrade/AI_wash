from django.shortcuts import render
from django.http import HttpResponse
from login.views import login2

def index(request):
   if 'mem_session' in request.session:
         return render(request,"index.html",locals())
   else:
      return login2(request)

def teach(request):
   if 'mem_session' in request.session:
         return render(request,"teaching.html",locals())
   else:
      return login2(request)
