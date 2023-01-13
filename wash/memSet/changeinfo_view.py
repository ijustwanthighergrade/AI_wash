from django.shortcuts import render
from django.http import HttpResponse
from login.views import login2
from login.models import MEMBER
from member.models import COLOR

def changeinfo(request):
    if 'mem_session' in request.session:
        changephone=""
        changeaddr=""
        changecard=""
        memc=MEMBER.objects.filter(MEMID=request.session['mem_session'])
        if request.method == 'GET':
            changephone = request.GET.get('phone')
            changeaddr = request.GET.get('addr')
            changecard = request.GET.get('card')
        print(changephone,changeaddr,changecard)
        if changephone != "":
            memc.update(MEMPHONE=changephone)
        if changeaddr != "":
            memc.update(MEMADDR=changeaddr)
        if changecard != "":
            memc.update(MEMCARD=changecard)
        mem = MEMBER.objects.get(MEMID=request.session['mem_session'])
        memphone=mem.MEMPHONE
        ADDR=mem.MEMADDR
        CARD=mem.MEMCARD
        mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
        print(mycolor)
        return render(request,"index.html",locals())
    else:
        return login2(request)