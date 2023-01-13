from pyexpat.errors import messages
from django.shortcuts import render
import requests

from login.models import LOGIN
from login.models import MEMBER
from member.models import COLOR

from login.models import AGREE
from login.views import login2
# Create your views here.


#進入view
#建立SACCngrok及自己的serverngrok
SACCngrok="https://10eb-1-34-54-152.jp.ngrok.io"
serverngrok="https://5d32-58-115-108-180.jp.ngrok.io"
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
    
    if not COLOR.objects.filter(MEMID=request.session['mem_session']).exists():
        COLOR.objects.create(MEMID=request.session['mem_session'],WHICHCOLOR=0)
    else:
        pass
    mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
    print(mycolor)
        
    MEMBER.objects.filter(MEMID = userUID).update(ACCESS=access_code)
    print(request.session['mem_session'])
    
    if AGREE.objects.filter(MEMID=request.session['mem_session']).exists():
        return render(request, 'index.html', locals())
    else:
        return render(request, 'signup.html', locals())
    
    
    
    
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


def yesitsignup(request):
    if 'mem_session' in request.session:
        
        mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
        print(mycolor)
        yes=""
        if request.method == 'GET':
            yes=request.GET.get('yes')
        if yes != "":    
            AGREE.objects.create(MEMID=request.session['mem_session'])
        return render(request, 'index.html', locals())
    else:
        return login2(request)