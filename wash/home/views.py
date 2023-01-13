from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# https://ithelp.ithome.com.tw/articles/10158250
from login.views import login2
from member.models import COLOR

def index(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"index.html",locals())
   else:
      return login2(request)
def wash1(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"wash1.html",locals())
   else:
      return login2(request)
def map(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"map.html",locals())
   else:
      return login2(request)

def feedback(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"return.html",locals())
   else:
      return login2(request)

def faq(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"faq.html",locals())
   else:
      return login2(request)

def friend(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"friend.html",locals())
   else:
      return login2(request)

def member(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"member.html",locals())
   else:
      return login2(request)

def teach(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"teaching.html",locals())
   else:
      return login2(request)

