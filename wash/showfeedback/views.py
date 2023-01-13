from django.shortcuts import render
from django.http import HttpResponse
from login.views import login2
from feedback.models import REPROBLEMS
from procedure.models import CLIST
from procedure.models import delivery

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
      if request.method == 'GET':
        ordernum = request.GET.get('ordernum')
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      
      O =CLIST.objects.get(ORDID=ordernum)
      flod=O.FMODE
      dry=O.LMODE
      wash=O.WMODE
      
      print(flod,dry,wash)
      
      if wash=="標準":
         wash="%E6%A8%99%E6%BA%96"
      elif wash == "精緻洗":
         wash="%E7%B2%BE%E7%B7%BB%E6%B4%97"
      elif wash == "柔洗":
         wash="%E6%9F%94%E6%B4%97"
      else:
         wash="%E5%BF%AB%E6%B4%97&"
         
      if dry=="日曬":
         dry="%E6%97%A5%E6%9B%AC"
      elif dry == "低溫烘乾":
         dry="%E4%BD%8E%E6%BA%AB%E7%83%98%E4%B9%BE"
      elif dry == "中溫烘乾":
         dry="%E4%B8%AD%E6%BA%AB%E7%83%98%E4%B9%BE"
      else:
         dry="%E9%AB%98%E6%BA%AB%E7%83%98%E4%B9%BE"
         
      if flod=="不折":
         flod="%E4%B8%8D%E8%A4%B6"
         print("aaa")
      else:
         flod="%E6%A9%9F%E5%99%A8%E4%BA%BA%E6%91%BA%E8%A1%A3"
      
      
      way="%E8%87%AA%E5%8F%96"
      if delivery.objects.filter(ORDID=ordernum):
         way="%E5%A4%96%E9%80%81"
      
      
      return render(request,"feedback.html",locals())
   else:
      return login2(request)