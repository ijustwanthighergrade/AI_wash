
from django.shortcuts import render
from django.http import HttpResponse
from pyexpat.errors import messages
import requests
from procedure.models import order
from login.models import MEMBER
from login.views import login2
from member.models import COLOR

def colorchange(request):
   if 'mem_session' in request.session:
      color=""
      
      if request.method == 'GET':
         color=request.GET.get('color')
      
      if color !="":
         COLOR.objects.filter(MEMID=request.session['mem_session']).update(WHICHCOLOR=color)
      return render(request,"index.html",locals())
   else:
      return login2(request)