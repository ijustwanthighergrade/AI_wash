from django.shortcuts import render
from django.http import HttpResponse
from login.views import login2
from procedure.models import CLIST
from procedure.models import order

def index(request):
   if 'mem_session' in request.session:
         return render(request,"index.html",locals())
   else:
      return login2(request)
   
def detail(request):
   if 'mem_session' in request.session:
      if request.method == 'GET':
         ordid=request.GET.get('ordid')
         
      
      ordera = order.objects.get(ORDID=ordid)
      GPOINT=ordera.GPOINT
      AMOUNT=ordera.AMOUNT
      ORDID=ordera.ORDID
      CDATE=ordera.CDATE
      GPOINT=ordera.GPOINT
      
      clist = CLIST.objects.get(ORDID=ordid)
      ORDID =clist.ORDID
      WMODE =clist.WMODE
      LMODE = clist.LMODE
      FMODE = clist.FMODE
      BAGNUM = clist.BAGNUM
      PRICE = clist.PRICE
      TIME = clist.TIME
      
      return render(request,"more.html",locals())
   else:
      return login2(request)
   
