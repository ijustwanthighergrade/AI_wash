from pyexpat.errors import messages
from django.shortcuts import render
import requests

from login.models import LOGIN
from login.models import MEMBER

# Create your views here.


#進入view
#建立SACCngrok及自己的serverngrok
SACCngrok="https://10eb-1-34-54-152.jp.ngrok.io"
serverngrok="http://127.0.0.1:8000/"
#第二步
def api2(request):
    if request.method == 'GET':
        fknum = request.GET.get('fk')
        nomatter=LOGIN.objects.filter(FKcheck = fknum)
        sum=''
        for i in nomatter:
            sum=i.Rstate
    url = SACCngrok+'/RESTapiApp/Line_2/?Rstate='+sum
    req=requests.get(url,headers = {'Authorization': 'Token e747f053f1e4ecf0228195b5652e27060e0937bd','ngrok-skip-browser-warning': '7414'})
    req_read = req.json()
    print(req_read)
    userUID=req_read["RuserID"]
    access_code=req_read["Raccess_code"]
    print(req_read["Raccess_code"])
    LOGIN.objects.filter(FKcheck = fknum).update(Raccesscode=access_code)
    if(MEMBER.objects.filter(MEMID__exact = userUID)): 
        if 'mem_session' in request.session:
            try:
                del request.session['mem_session']
            except:
                pass
        request.session['mem_session'] = userUID
        request.session.modified = True
        request.session.set_expiry(60*30) #存在20分鐘
    else:
        MEMBER.objects.create(MEMID=userUID)
        request.session['mem_session'] = userUID
        request.session.modified = True
        request.session.set_expiry(60*30) #存在20分鐘
        
    MEMBER.objects.filter(MEMID = userUID).update(ACCESS=access_code)
    print(request.session['mem_session'])
    return render(request, 'index.html', locals())
    
def api1(request):
    if request.method == 'GET':
        fknum = request.GET.get('fk')
        nomatter=LOGIN.objects.filter(FKcheck = fknum)
        sum=''
        for i in nomatter:
            sum=i.Rstate
    url = SACCngrok+'/RESTapiApp/SMS_2/?RSMSid='+sum
    req=requests.get(url,headers = {'Authorization': 'Token e747f053f1e4ecf0228195b5652e27060e0937bd','ngrok-skip-browser-warning': '7414'})
    req_read = req.json()
    print(req_read)
    userUID=req_read["RuserID"]
    access_code=req_read["Raccess_code"]
    print(req_read["Raccess_code"])
    LOGIN.objects.filter(FKcheck = fknum).update(Raccesscode=access_code)
    if(MEMBER.objects.filter(MEMID__exact = userUID)): 
        if 'mem_session' in request.session:
            try:
                del request.session['mem_session']
            except:
                pass
        request.session['mem_session'] = userUID
        request.session.modified = True
        request.session.set_expiry(60*30) #存在20分鐘
    else:
        MEMBER.objects.create(MEMID=userUID)
        request.session['mem_session'] = userUID
        request.session.modified = True
        request.session.set_expiry(60*30) #存在20分鐘
        
    MEMBER.objects.filter(MEMID = userUID).update(ACCESS=access_code)
    print(request.session['mem_session'])
    return render(request, 'index.html', locals())