from django.shortcuts import render
from django.http import HttpResponse
from login.views import login2

from datetime import datetime
from feedback.models import REPROBLEMS
from procedure.models import order
from member.models import COLOR

def feedback(request):
   if 'mem_session' in request.session:
      ordera = order.objects.filter(MEMID=request.session['mem_session'])
      orderlist=list(ordera.values())
      print(orderlist)
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      
      return render(request,"return.html",{
        'orderlist': orderlist,
         'mycolor':mycolor
      })
   else:
      return login2(request)

def index(request):
   if 'mem_session' in request.session:
      
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"index.html",locals())
   else:
      return login2(request)

