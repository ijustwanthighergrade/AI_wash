from django.shortcuts import render
from django.http import HttpResponse
from login.views import login2
from feedback.models import REPROBLEMS

from member.models import COLOR
def index(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"index.html",locals())
   else:
      return login2(request)
   
def showfeedback(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"feedback.html",locals())
   else:
      return login2(request)