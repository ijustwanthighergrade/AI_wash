from pyexpat.errors import messages
from django.shortcuts import render
import requests

from login.models import LOGIN
from login.models import MEMBER

# Create your views here.


#進入view
#建立SACCngrok及自己的serverngrok
SACCngrok="https://10eb-1-34-54-152.jp.ngrok.io"
serverngrok="https://81e7-58-115-108-180.jp.ngrok.io"
#第一步 登入介面的view，每次重整都會run一次

# def login(request):
#     to =serverngrok+"/api1"
#     return render(request, 'login.html', locals())

# def api1(request):
#     fknum=''
#     if request.method == 'GET':
#         rand=LOGIN.objects.create()
#         fknum = request.GET.get('Rphone')
#         rand.FKcheck=fknum # 店畫存fk
        
#     r1_r=""
#     url1=SACCngrok+'/RESTapiApp/SMS_1/?Rphone='+fknum  
#     r1=requests.get(url1,headers = {'Authorization': 'Token e747f053f1e4ecf0228195b5652e27060e0937bd','ngrok-skip-browser-warning': '7414'})
    
#     noregster=""
#     noregster=r1['detail']
#     r1_r = r1['RSMSid']

#     return loginsms(request,r1_r)

# def loginsms(request,smsid):
#     url = SACCngrok+'/RESTapiApp/SMS_2/?RSMSid='+smsid
#     data={
#         'RSMSid': smsid,
#         'RSMS_code': checkcode, 
#     }
#     req=requests.get(url,data,headers = {'Authorization': 'Token e747f053f1e4ecf0228195b5652e27060e0937bd','ngrok-skip-browser-warning': '7414'})
#     req_read = req.json()
#     print(req_read)
#     userUID=req_read["RuserID"]
#     access_code=req_read["Raccess_code"]
#     print(req_read["Raccess_code"])
#     LOGIN.objects.filter(FKcheck = fknum).update(Raccesscode=access_code)
#     if(MEMBER.objects.filter(MEMID__exact = userUID)): 
#         if 'mem_session' in request.session:
#             try:
#                 del request.session['mem_session']
#             except:
#                 pass
#         request.session['mem_session'] = userUID
#         request.session.modified = True
#         request.session.set_expiry(60*30) #存在20分鐘
#     else:
#         MEMBER.objects.create(MEMID=userUID)
#         request.session['mem_session'] = userUID
#         request.session.modified = True
#         request.session.set_expiry(60*30) #存在20分鐘
        
#     MEMBER.objects.filter(MEMID = userUID).update(ACCESS=access_code)
#     print(request.session['mem_session'])
#     return render(request, 'index2.html', locals())

def login2(request):
    sum=""
    state1=""
    rand=LOGIN.objects.create()
    # print(rand.FKcheck)
    # print(type(rand.FKcheck))
    url = SACCngrok+'/RESTapiApp/Line_1/?Rbackurl='+serverngrok+'/api2/?fk='+rand.FKcheck
    req=requests.get(url,headers = {'Authorization': 'Token e747f053f1e4ecf0228195b5652e27060e0937bd','ngrok-skip-browser-warning': '7414'})
    print(req.json())
    req_read = req.json()
    print(req_read["Rstate"])
    state1=req_read["Rstate"]
    
    LOGIN.objects.filter(FKcheck = rand.FKcheck).update(Rstate=state1)
        
    firstLogin="https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1657781063&redirect_uri="+SACCngrok+"/LineLoginApp/callback&state="+req_read["Rstate"]+"&scope=profile%20openid%20email&promot=consent&ui_locales=zh-TW?http://example.com/?ngrok-skip-browser-warning=7414"
    
    # print(firstLogin)
    return render(request, 'startbtn.html', locals())
# 前端登入按鈕：<a href="{{ firstLogin }}"><button type="button" class="btn btn-outline-success">使用line登入</button></a>


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

# def Login_and_AddSession(request):
#     會員編號 = request.GET.get('會員編號')
#     if '會員編號' in request.session:
#         try:
#             del request.session['session標籤名稱']
#         except:
#             pass
#     request.session['session標籤名稱'] = 會員編號
#     request.session.modified = True
#     request.session.set_expiry(60*20) #存在20分鐘
#     return HttpResponseRedirect('inside.html')

#第三步（非必要，要拿個資才要寫！ 此範例只有拿取line頭貼，若想取得其他資料請print req_read2）
# def access(request):
#     results=client.objects.filter(PHONE_NUMBER = request.user)
#     ac_code=''
#     for result in results:
#         ac_code = result.AC_CODE
#     url2=SACCngrok+'/RESTapiApp/Access/?Raccess_code='+ac_code
#     req2=requests.get(url2,headers = {'Authorization': 'Token e747f053f1e4ecf0228195b5652e27060e0937bd','ngrok-skip-browser-warning': '7414'})
    
#     req_read2 = req2.json()
#     print(type(req2.status_code))
#     if (req2.status_code!=200):
#         print("================================")
#         messages.error(request, '存取權已過期，請重新登入')
#         logout(request)
#     else:
    
#         pic=req_read2["sPictureUrl"]
#         print(pic)

#         return pic