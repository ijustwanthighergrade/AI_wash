# AI_wash
系統分析期末專案

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
原先wash下方settings.py要設定東西 但我設定完了
因此之後要設定的只有 
1.你複製的urls.py 
2.wash資料夾下的urls.py 
3.每個html裡面插入的css/js/images要用 {% static "位址"%}取代掉 可以參考index.html
ex:{% static "css/aaa.css"%}{% static "images/aaa.jpg"%}


#參考資料#
1.https://www.maxlist.xyz/2018/12/31/python_django/#%E4%BF%AE%E6%94%B9Demo%E8%B3%87%E6%96%99%E5%A4%BE%E5%85%A7%E7%9A%84urlspy%EF%BC%9A
2.https://yanwei-liu.medium.com/python-django%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E4%B8%80-%E5%9F%BA%E6%9C%AC%E7%92%B0%E5%A2%83-c3d5d1727d53



## p.s. 可能會遇到的問題##
1.跑虛擬環境時可能會遇到
https://learn.microsoft.com/zh-tw/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3
這裡面的問題，先去vscode裝PowerShell再重開VSCODE應該就沒事了，有事再自己想辦法歐

2.跑網站時下 python manage.py runserver
但跑server時沒辦法在終端機下指令 按ctrl+c取消server執行

