from pyexpat.errors import messages
from django.shortcuts import render
import requests

from login.models import LOGIN

# Create your views here.


#進入view
#建立SACCngrok及自己的serverngrok
SACCngrok="https://10eb-1-34-54-152.jp.ngrok.io"
serverngrok="http://127.0.0.1:8000/login/"
#第一步 登入介面的view，每次重整都會run一次
def login(request):
    return render(request, 'login.html', locals())

def login2(request):
    sum=""
    rand=LOGIN.objects.create()
    # print(rand.FKcheck)
    # print(type(rand.FKcheck))
    url = SACCngrok+'/RESTapiApp/Line_1/?Rbackurl='+serverngrok+'/api2/?fk='+rand.FKcheck
    req=requests.get(url,headers = {'Authorization': 'Token e747f053f1e4ecf0228195b5652e27060e0937bd','ngrok-skip-browser-warning': '7414'})
    print(req.json())
    req_read = req.json()
    print(req_read["Rstate"])
    LOGIN.objects.filter(FKcheck = rand.FKcheck).update(Rstate=req_read["Rstate"])
    firstLogin="https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1657781063&redirect_uri="+SACCngrok+"/LineLoginApp/callback&state="+req_read["Rstate"]+"&scope=profile%20openid%20email&promot=consent&ui_locales=zh-TW?http://example.com/?ngrok-skip-browser-warning=7414"

    return render(request, 'login2.html', locals())
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

    return login2(request,userUID,access_code)

#第三步（非必要，要拿個資才要寫！ 此範例只有拿取line頭貼，若想取得其他資料請print req_read2）
def access(request):
    results=client.objects.filter(PHONE_NUMBER = request.user)
    ac_code=''
    for result in results:
        ac_code = result.AC_CODE
    url2=SACCngrok+'/RESTapiApp/Access/?Raccess_code='+ac_code
    req2=requests.get(url2,headers = {'Authorization': 'Token e747f053f1e4ecf0228195b5652e27060e0937bd','ngrok-skip-browser-warning': '7414'})
    
    req_read2 = req2.json()
    print(type(req2.status_code))
    if (req2.status_code!=200):
        print("================================")
        messages.error(request, '存取權已過期，請重新登入')
        logout(request)
    else:
    
        pic=req_read2["sPictureUrl"]
        print(pic)

        return pic