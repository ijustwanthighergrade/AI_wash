from django.shortcuts import render
from django.http import HttpResponse

from login.views import login2
from login.models import MEMBER

def index(request):
   if 'mem_session' in request.session:
      return render(request,"index.html",locals())
   else:
      return login2(request)
   
def memSet(request):
   if 'mem_session' in request.session:
      mem = MEMBER.objects.get(MEMID=request.session['mem_session'])
      memphone=mem.MEMPHONE
      ADDR=mem.MEMADDR
      CARD=mem.MEMCARD
      return render(request,"memberset.html",locals())
   else:
      return login2(request)
   