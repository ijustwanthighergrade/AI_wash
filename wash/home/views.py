from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# https://ithelp.ithome.com.tw/articles/10158250
from login.views import login2

def index(request):
   if 'mem_session' in request.session:
      return render(request,"index.html",locals())
   else:
      return login2(request)
def wash1(request):
   return render(request,"wash1.html",locals())
def map(request):
   return render(request,"map.html",locals())
def feedback(request):
   return render(request,"return.html",locals())
def faq(request):
   return render(request,"faq.html",locals())
def friend(request):
   return render(request,"friend.html",locals())
def member(request):
   return render(request,"member.html",locals())
def teach(request):
   return render(request,"teaching.html",locals())

