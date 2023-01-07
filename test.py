import requests

# 資料庫要存的東西有fkcheck每組不可重複 最一開始 Rstate
# 用session做登入註冊 這樣就可以處理他要登入多久
# 
# 我們有需要把GITHUB檔案丟進去五們的專案中嗎 

#全部都用back傳
# 第一次傳送網址 在rebackurl後面加上?fk=123 隨機碼 
# 要自己存state 
# 可以選一個登入就好

# https://access.line.me/oauth2/v2.1/login?returnUri=%2Foauth2%2Fv2.1%2Fauthorize%2Fconsent%3Fresponse_type%3Dcode%26client_id%3D1657781063%26redirect_uri%3Dd9a6-1-34-54-152.jp.ngrok.io%252FLineLoginApp%252Fcallback%26state%3DState-3cf0b526-e36c-4e99-ab58-2ad973a86cc5%26scope%3Dprofile%2Bopenid%2Bemail%26promot%3Dconsent%26ui_locales%3Dzh-TW&loginChannelId=1657781063&loginState=s4ADmfbafCsCOcBbkKzmEA


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
#     'Rstate': 'State-4372ef6c-c233-4e7b-be2e-0c2e574565b0'
# }
# r = requests.get(url,data,headers={'Authorization':'Token e747f053f1e4ecf0228195b5652e27060e0937bd'})
# print(r.json()) 

# 傳Raccess_code 可以收到個資
# url="https://e024-1-34-54-152.jp.ngrok.io/RESTapiApp/Access/"
# data={
#     'Raccess_code': 'Access-9a9d6e17-664f-4677-9c70-98eb287bbda6'
# }
# r = requests.get(url,data,headers={'Authorization':'Token e747f053f1e4ecf0228195b5652e27060e0937bd'})
# print(r.json()) 

# https://0e15-2001-b400-e339-80f8-cdfa-1872-3160-73a7.jp.ngrok.io/admin/RESTapiApp/Line_1/

# 簡訊第1步驟
# SMS_1
# 傳送電話號碼Rphone
# 回傳RSMSis

# url1="https://e024-1-34-54-152.jp.ngrok.io/RESTapiApp/SMS_1/"
# data={
#     'Rphone': '0908098950'
# }
# r = requests.get(url1,data,headers={'Authorization':'Token e747f053f1e4ecf0228195b5652e27060e0937bd'})
# print(r.json()) 

# 簡訊第2步驟

# url2="https://e024-1-34-54-152.jp.ngrok.io/RESTapiApp/SMS_2/"
# data={
#     'RSMSid': 'RSMSid-24bc695b-51ad-43af-9937-e7c7f301509f',
#     'RSMS_code' :'2315', 
#       #手機驗證碼
# }
# r = requests.get(url2,data,headers={'Authorization':'Token e747f053f1e4ecf0228195b5652e27060e0937bd'})
# print(r.json()) 

# 簡訊第三步驟
# url3="https://e024-1-34-54-152.jp.ngrok.io/RESTapiApp/Access/"
# data={
#     'RuserID': 'UserID-59d0094e-48b6-4700-a45b-63ba7e927593',
#     'Raccess_code' :'Access-0c824128-1bc1-41e6-ae88-6ebc8e752ccb'
# }
# r = requests.get(url3,data,headers={'Authorization':'Token e747f053f1e4ecf0228195b5652e27060e0937bd'})
# if r.status_code == 200:
#     print(r.json()) 
# else:
#         print("Error from server: " + str(r.content))
