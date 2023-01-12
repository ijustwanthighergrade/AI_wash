
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
      if not COLOR.objects.filter(MEMID=request.session['mem_session']).exists():
         COLOR.objects.create(MEMID=request.session['mem_session'],WHICHCOLOR="0")
      else:
         pass
      if request.method == 'GET':
         color=request.POST.get('r1')
      
      if color !="":
         COLOR.objects.filter(MEMID=request.session['mem_session']).update(WHICHCOLOR=color)
      return render(request,"index.html",locals())
   else:
      return login2(request)