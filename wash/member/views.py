from django.shortcuts import render
from django.http import HttpResponse
from pyexpat.errors import messages
import requests
from procedure.models import order
from login.models import MEMBER
from login.views import login2

SACCngrok="https://10eb-1-34-54-152.jp.ngrok.io"
serverngrok="http://127.0.0.1:8000/"

def index(request):
   return render(request,"index.html",locals())

def member(request):
   if 'mem_session' in request.session:
      print(request.session['mem_session'])
      results=MEMBER.objects.filter(MEMID = request.session['mem_session'])
      ac_code=''
      for result in results:
         ac_code = result.ACCESS
      url2=SACCngrok+'/RESTapiApp/Access/?Raccess_code='+ac_code
      req2=requests.get(url2,headers = {'Authorization': 'Token e747f053f1e4ecf0228195b5652e27060e0937bd','ngrok-skip-browser-warning': '7414'})
      
      req_read2 = req2.json()
      print(req_read2)
      if (req2.status_code!=200):
         print("================================")
         #   messages.error(request, '存取權已過期，請重新登入')
         logout(request)
      else:
         pic=req_read2["sPictureUrl"]
         nickname=req_read2["sNickName"]
         print(pic)
      return render(request,"member.html",locals())
   else:
      return login2(request)
       
    
def color(request):
   if 'mem_session' in request.session:
      howmuch=order.objects.filter(MEMID=request.session['mem_session']).count()
      print(howmuch)
      
      return render(request,"color.html",locals())
   else:
      return login2(request)
   
def logout(request):
   
   del request.session['mem_session']
   return render(request,"startbtn.html",locals())