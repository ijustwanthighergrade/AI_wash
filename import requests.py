import requests

# with open("r.json") as f:
#     # 讀取 JSON 檔案
#     p = json.load(f)
#     # 查看整個 JSON 資料解析後的結果
#     print("p =", p)
#     # 取得 name 的值
#     print("name =", p["name"])
#     # 取得 skill 的值
#     print("skill =", p["skill"])

# myDict = {
#     "fk":123,
#     "Rstate": "",
#     "RuserID": "",
#     "Raccess_code": ""
# }

# 資料庫要存的東西有fkcheck每組不可重複 最一開始 Rstate
# 用session做登入註冊 這樣就可以處理他要登入多久

#全部都用back傳
# 第一次傳送網址 在rebackurl後面加上?fk=123 隨機碼 
# 要自己存state 
# 可以選一個登入就好
SACCngrok="https://10eb-1-34-54-152.jp.ngrok.io"

# https://access.line.me/oauth2/v2.1/authorize/consent?
# response_type=code&
# client_id=1657781063&
# redirect_uri=https://e024-1-34-54-152.jp.ngrok.io%2F
# LineLoginApp%2F
# callback&
# state=State-723fd84c-ab57-4852-9980-e8f4d578f6a0&
# scope=profile+openid+email&
# promot=consent&ui_locales=zh-TW

# https://access.line.me/oauth2/v2.1/login?
# returnUri=%2Foauth2%2Fv2.1%2Fauthorize%2Fconsent%3Fresponse_type%3Dcode%26client_id%3D1657781063%26
# redirect_uri%3Dhttps://e024-1-34-54-152.jp.ngrok.io%252FLineLoginApp%252F
# callback%26
# state%3DState-cffea23a-471f-455f-9d33-723b3a05c02a
# scope%3Dprofile%2Bopenid%2Bemail%26promot%3Dconsent%26ui_locales%3Dzh-TW&
# loginChannelId=1657781063&
# loginState=s4ADmfbafCsCOcBbkKzmEA


#{'Authorization': 'Token e747f053f1e4ecf0228195b5652e27060e0937bd'} 類似密鑰的東西 從dbmanageapp 後台新增

# Line_1的功能是：跳轉回頁面
# 你發送Rbackurl
# 伺服器會傳送Rstate回來 state是一次性的如果失敗要從line1再開一次

# url="https://e024-1-34-54-152.jp.ngrok.io/RESTapiApp/Line_1/"
# data={
#     'Rbackurl': '我的網址'
# }
# r = requests.get(url,data,headers={'Authorization':'Token e747f053f1e4ecf0228195b5652e27060e0937bd'})
# print(r.json()) 

# line_2:
# 用戶傳送Rstate
# 伺服器回傳RuserID跟Raccess_code
# 發送requset的code

# url="https://e024-1-34-54-152.jp.ngrok.io/RESTapiApp/Line_2/"
# data={
#     # 'Rstate': 'LINE1傳的Rstate'
#     'Rstate': 'State-723fd84c-ab57-4852-9980-e8f4d578f6a0'
# }
# r = requests.get(url,data,headers={'Authorization':'Token e747f053f1e4ecf0228195b5652e27060e0937bd'})
# print(r.json()) 

# 傳Raccess_code 可以收到個資

# url="https://e024-1-34-54-152.jp.ngrok.io/RESTapiApp/Access/"
# data={
#     'Raccess_code': 'Access-ed9a32c4-8f5d-4e71-8dfb-a5a32454ccdf'
# }
# r = requests.get(url,data,headers={'Authorization':'Token e747f053f1e4ecf0228195b5652e27060e0937bd'})
# print(r.json()) 

# https://0e15-2001-b400-e339-80f8-cdfa-1872-3160-73a7.jp.ngrok.io/admin/RESTapiApp/Line_1/

# 簡訊第1步驟
# SMS_1
# 傳送電話號碼Rphone
# 回傳RSMSis

url1=SACCngrok+"/RESTapiApp/SMS_1/"
data={
    'Rphone': '0908098950'
}
r = requests.get(url1,data,headers={'Authorization':'Token e747f053f1e4ecf0228195b5652e27060e0937bd'})
print(r.json()) 

# 簡訊第2步驟

# url2="https://e024-1-34-54-152.jp.ngrok.io/RESTapiApp/SMS_2/"
# data={
#     'RSMSid': 'RSMSid-a5187086-3b81-41fc-a01c-48c99c0d4a82',
#     'RSMS_code' :'0328', 
#       #手機驗證碼
# }
# r = requests.get(url2,data,headers={'Authorization':'Token e747f053f1e4ecf0228195b5652e27060e0937bd'})
# print(r.json()) 

# 簡訊第三步驟
# url3="https://e024-1-34-54-152.jp.ngrok.io/RESTapiApp/Access/"
# data={
#     'RuserID': 'UserID-872c93a1-25bf-487f-a8bb-60f43e509335',
#     'Raccess_code' :'Access-f15bd58e-5b7d-497a-9911-162090bcaf27'
# }
# r = requests.get(url3,data,headers={'Authorization':'Token e747f053f1e4ecf0228195b5652e27060e0937bd'})
# if r.status_code == 200:
#     print(r.json()) 
# else:
#         print("Error from server: " + str(r.content))
