from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from django.template import Template,Context
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
from login.models import MEMBER
import requests

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
   'creditcard':'',
   'usetime': 0,
   'tax': 0,
   
   
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
      
      mem=MEMBER.objects.get(MEMID=request.session['mem_session'])
      memaddr=mem.MEMADDR
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
         
      
      wmode=WMODE.objects.get(WMODE=orderdata['washway'])
      lmode=LMODE.objects.get(LMODE=orderdata['dryway'])
      fmode=FMODE.objects.get(FMODE=orderdata['flodway'])
      
      PRICE = wmode.MONEY + lmode.MONEY + fmode.MONEY + int(orderdata['bagamount']) * 50 + wmode.MEMISSIONS * 3 + lmode.MEMISSIONS * 3 + fmode.MEMISSIONS * 3
      GPOINT = wmode.POINTS + lmode.POINTS + fmode.POINTS+ int(orderdata['bagamount']) * 20
      C_AMOUNT = wmode.MEMISSIONS * 3 + lmode.MEMISSIONS * 3 + fmode.MEMISSIONS * 3
      
      orderdata['tpoint']=GPOINT
      orderdata['tprice']=PRICE
      orderdata['tax']=C_AMOUNT
      
      
      
      
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
      
      orderamount = orderdata['bagamount']
      washway= orderdata['washway']
      dryway= orderdata['dryway']
      flodway= orderdata['flodway']
      specialitem= orderdata['specialitem']
      tpoint= orderdata['tpoint']
      tprice= orderdata['tprice']
      tax=orderdata['tax']
      
      date=orderdata['getdate']
      time=orderdata['gettime']
      takeway=orderdata['Take']
      
      t=""
      if takeway=='外送':
         t=orderdata['addr']
      else:
         t="商家自取"
         
      mem = MEMBER.objects.get(MEMID=request.session['mem_session'])
      phone=mem.MEMPHONE
      card=mem.MEMCARD
      
      
      print(orderdata)
      return render(request,"wash4.html",locals())
   else:
      return login2(request)

def dealorder(request):
   rememberphone=""
   remembercard=""
   if 'mem_session' in request.session:
      if request.method == 'POST':
         phone=request.POST.get('phone')
         card=request.POST.get('card')
         rememberphone=request.POST.get('rememberphone')
         remembercard=request.POST.get('remembercard')
         
      orderdata['mphone']=phone,
      orderdata['creditcard']=card
      
   mem = MEMBER.objects.filter(MEMID=request.session['mem_session'])
   if rememberphone != "":
      mem.update(MEMPHONE=phone)
   if remembercard != "":
      mem.update(MEMCARD=card)
      
   
   
   WASH=WMODE.objects.get(WMODE=orderdata['washway'])
   DRY=LMODE.objects.get(LMODE=orderdata['dryway'])
   FOLD=FMODE.objects.get(FMODE=orderdata['flodway'])
   CLIST.objects.create(WMODE=WASH, LMODE=DRY,FMODE=FOLD,BAGNUM=int(orderdata['bagamount']))
   
   
   ord=CLIST.objects.latest('id')
   ORD=ord.ORDID
   
   order.objects.filter(ORDID=ORD).update(MEMID=request.session['mem_session'])
   shops=shop.objects.get(id=1)
   SHOPS=shops.SHOPID
   
   datechange=orderdata['getdate']+" "+orderdata['gettime']
   datetime.strptime(datechange,'%Y-%m-%d %H:%S')
   if(orderdata['Take']=="外送"):
      delivery.objects.create(ORDID=ORD,SHOPID=SHOPS,PHONE=orderdata['mphone'], ADDRESS=orderdata['addr'],GDATE=datechange)
      
   # a=order.objects.get(ORDID=ORD)
   # res = requests.get("http://127.0.0.1:5000/add", json = {
   #    "ORDID": a.ORDID,
   #    "MEMID": a.MEMID,
   #    "CDATE": a.CDATE.strftime("%Y-%m-%d %H:%M"),
   #    "GPOINT": a.GPOINT,
   #    "AMOUNT": a.AMOUNT,
   #    "APPID": a.APPID
   # })
   
   print(orderdata)

   return render(request,"index.html",locals())

def index(request):
   if 'mem_session' in request.session:
         return render(request,"index.html",locals())
   else:
      return login2(request)
   

