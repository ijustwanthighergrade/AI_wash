# AI_wash
系統分析期末專案

前端注意事項(請直接在templates的html中更改)
1.請幫我在每個頁面的開頭都加上{% load static %}
2.css的部份請改成下列這種形式
ex:<link href="{% static "css/add.css" %}" rel="stylesheet">
3.圖片的部份請改成下列這種形式
ex:<img class ="logo" src="{% static "images/logo.jpg" %}">
4.url的部分請依照下面後端注意事項的第一個英文改{% url '對應的英文' %}
ex:<a href="{% url 'wash1' %}"><div  class="text3" id="small">開始洗衣</div></a>   

每個html裡面插入的css/js/images要用 {% static "位址"%}取代掉 可以參考index.html
ex:{% static "css/aaa.css"%}{% static "images/aaa.jpg"%}
而跳轉頁面原先只要herf="xxx.html" 
現在要把xxx.html改成 {% url 'url.py設定的name' %} ex:{% url 'index' %}

app的urls 16個頁面 不包括sinup.html和add.html
index           連接的是   index.html       .
teach           連接的是   teaching.html    .
wash1           連接的是   wash1.html       .
wash2           連接的是   wash2.html
wash3           連接的是   wash3.html
wash4           連接的是   wash4.html
map             連接的是   map.html         .
faq             連接的是   faq.html         .
friend          連接的是   friend.html      .
member          連接的是   member.html      .
memSet          連接的是   memberset.html   .
order           連接的是   order.html       .
detail          連接的是   more.html        .
complain        連接的是   complain.html    .
showfeedback    連接的是   feedback.html    .
feedback        連接的是   return.html      .

app資料夾內容
home            主頁
procedure       洗衣流程1

後端注意事項
##一、安裝與建置環境##
1.python
https://ithelp.ithome.com.tw/articles/10210071
2.django
https://ithelp.ithome.com.tw/articles/10199575

##django登入/登出##
https://ithelp.ithome.com.tw/articles/10206063

##二、用python開網頁##
比如開了新的app叫做home它裡面不會產生出urls.py
要複製一個wash資料夾裡的urls.py丟到home資料夾裡面
wash下方的settings.py要設定東西
至少有以下這些，可能有漏的就再看一下參考資料，真的不行就push上來給我看
1.你複製的urls.py 
2.該專案產生的views.py
3.settings.py INSTALLED_APPS 每新增一個app都要把app名稱寫上去
4.wash資料夾下的urls.py urlpatterns

#參考資料#
1.https://www.maxlist.xyz/2018/12/31/python_django/#%E4%BF%AE%E6%94%B9Demo%E8%B3%87%E6%96%99%E5%A4%BE%E5%85%A7%E7%9A%84urlspy%EF%BC%9A
2.https://yanwei-liu.medium.com/python-django%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E4%B8%80-%E5%9F%BA%E6%9C%AC%E7%92%B0%E5%A2%83-c3d5d1727d53
3.https://www.twblogs.net/a/5d845cf2bd9eee532700039f



## p.s. 可能會遇到的問題##
1.跑虛擬環境時可能會遇到
https://learn.microsoft.com/zh-tw/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3
這裡面的問題，先去vscode裝PowerShell再重開VSCODE應該就沒事了，有事再自己想辦法歐

2.跑網站時下 python manage.py runserver
但跑server時沒辦法在終端機下指令 按ctrl+c取消server執行

