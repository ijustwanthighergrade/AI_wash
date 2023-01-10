from django.shortcuts import render
from django.http import HttpResponse
from login.views import login2

from datetime import datetime
from feedback.models import REPROBLEMS

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


def addproblems(request):
   if 'mem_session' in request.session:
      if request.method == 'POST':
         orderid= request.POST.get('orderid')
         comments= request.POST.get('comments')
         type=request.POST.get('type')
         print(orderid)
         time = datetime.now() #取得現在時間
         
         if not REPROBLEMS.objects.exists():
            REPROBLEMS.objects.create(
               PID= "001",
               MEMID =request.session['mem_session'],
               ORDID = orderid,  
               PTYPE = type,
               PTIME = time.strftime("%Y-%m-%d"),
               PDISC = comments,
            ).save()
         else:
            
            i = REPROBLEMS.objects.count()+1
            ordid = f"{i:03d}"
               
            REPROBLEMS.objects.create(
               PID= ordid,
               MEMID =request.session['mem_session'],
               ORDID = orderid,  
               PTYPE = type,
               PTIME = time.strftime("%Y-%m-%d"),
               PDISC = comments,
            ).save()
            
      return render(request,"index.html",locals())
   else:
      return login2(request)