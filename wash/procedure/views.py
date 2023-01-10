from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from login.views import login2
from procedure.models import order
from procedure.models import WMODE
from procedure.models import LMODE
from procedure.models import FMODE
from procedure.models import CLIST
from procedure.models import delivery
from procedure.models import shop
from procedure.models import bag
from procedure.models import lock

orderdata = {
   'Take': '',
   'addr': '',
   'bagamount':0,
   'washway':'',
   'dryway':'',
   'flodway':'',
   'specialitem':'',
   'tpoint':'',
   'tprice':'',
   'getdate':'',
   'gettime':'',
   'mphone':'',
   'creditcard':''
}

def wash1(request):
   if 'mem_session' in request.session:

      if not WMODE.objects.exists():
         WMODE.objects.create(WMODE="標準",MONEY=0,POINTS=5,MEMISSIONS=1,TIME=30)
         WMODE.objects.create(WMODE="精緻洗",MONEY=5,POINTS=0,MEMISSIONS=2,TIME=50)
         WMODE.objects.create(WMODE="柔洗",MONEY=5,POINTS=0,MEMISSIONS=2,TIME=40)
         WMODE.objects.create(WMODE="快洗",MONEY=0,POINTS=5,MEMISSIONS=2,TIME=20)

         LMODE.objects.create(LMODE="日曬",MONEY=0,POINTS=5,MEMISSIONS=0,TIME=1440)
         LMODE.objects.create(LMODE="低溫烘乾",MONEY=5,POINTS=0,MEMISSIONS=3,TIME=180)
         LMODE.objects.create(LMODE="中溫烘乾",MONEY=5,POINTS=0,MEMISSIONS=3,TIME=120)
         LMODE.objects.create(LMODE="高溫烘乾",MONEY=5,POINTS=0,MEMISSIONS=3,TIME=60)

         FMODE.objects.create(FMODE="不折",MONEY=0,POINTS=5,MEMISSIONS=0,TIME=0)
         FMODE.objects.create(FMODE="機器人",MONEY=5,POINTS=0,MEMISSIONS=1,TIME=20)
      else:
         pass
      return render(request,"wash1.html",locals())
   else:
      return login2(request)

def wash2(request):
   take=""
   addr=""
   if 'mem_session' in request.session:
      if request.method == 'POST':
         take=request.POST.get('r1')
         addr=request.POST.get('addr')
         
      orderdata['Take'] = take
      orderdata['addr']= addr
      
         
      return render(request,"wash2.html",locals())
   else:
      return login2(request)

def wash3(request):
   if 'mem_session' in request.session:
      if request.method == 'POST':
         bagamount=request.POST.get('bagamount')
         washing=request.POST.get('washing')
         drying=request.POST.get('drying')
         store=request.POST.get('store')
         special=request.POST.get('special')
         
         orderdata['bagamount']=bagamount
         orderdata['washway']=washing
         orderdata['dryway']=drying
         orderdata['flodway']=store
         orderdata['specialitem']=special
      
      print(orderdata)
      return render(request,"wash3.html",locals())
   else:
     return login2(request)

def wash4(request):
   if 'mem_session' in request.session:
      if request.method == 'POST':
         day=request.POST.get('day')
         time=request.POST.get('time')
         
      orderdata['getdate']=day
      orderdata['gettime']=time
      
      print(orderdata)
      return render(request,"wash4.html",locals())
   else:
      return login2(request)

def dealorder(request):
   if 'mem_session' in request.session:
      if request.method == 'POST':
         phone=request.POST.get('phone')
         card=request.POST.get('card')
         
      orderdata['mphone']=phone,
      orderdata['creditcard']=card
   
   
   
   WASH=WMODE.objects.get(WMODE=orderdata['washway'])
   DRY=LMODE.objects.get(LMODE=orderdata['dryway'])
   FOLD=FMODE.objects.get(FMODE=orderdata['flodway'])
   CLIST.objects.create(WMODE=WASH, LMODE=DRY,FMODE=FOLD,BAGNUM=int(orderdata['bagamount']))
   
   
   ord=CLIST.objects.latest('id')
   ORD=ord.ORDID
   shops=shop.objects.get(id=1)
   SHOPS=shops.SHOPID
   delivery.objects.create(ORDID=ORD,SHOPID=SHOPS,PHONE=orderdata['mphone'], ADDRESS=orderdata['addr'])
   
   
   print(orderdata)

   return render(request,"index.html",locals())

def index(request):
   if 'mem_session' in request.session:
         return render(request,"index.html",locals())
   else:
      return login2(request)
   

