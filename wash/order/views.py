from django.shortcuts import render
from django.http import HttpResponse
from login.views import login2
from procedure.models import order
from procedure.models import CLIST
from member.models import COLOR

def index(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"index.html",locals())
   else:
      return login2(request)
   
def order_view(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      
      ordera = order.objects.filter(MEMID=request.session['mem_session'])
      order_list =list(ordera.values())
      
      print(order_list)
      print(len(order_list))
      
      return render(request,"order.html",{
        'order_list': order_list,
        'mycolor':mycolor
      })
   else:
      return login2(request)
   