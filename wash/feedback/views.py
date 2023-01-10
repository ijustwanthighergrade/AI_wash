from django.shortcuts import render
from django.http import HttpResponse
from login.views import login2

def feedback(request):
   if 'mem_session' in request.session:
      
      return render(request,"return.html",locals())
   else:
      return login2(request)

def index(request):
   if 'mem_session' in request.session:
         return render(request,"index.html",locals())
   else:
      return login2(request)

