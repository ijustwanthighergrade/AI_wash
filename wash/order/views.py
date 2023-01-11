from django.shortcuts import render
from django.http import HttpResponse
from login.views import login2
from procedure.models import order
from procedure.models import CLIST

def index(request):
   if 'mem_session' in request.session:
      return render(request,"index.html",locals())
   else:
      return login2(request)
   
def order_view(request):
   if 'mem_session' in request.session:
      
      ordera = order.objects.filter(MEMID=request.session['mem_session'])
      order_list =list(ordera.values())
      
      print(order_list)
      print(len(order_list))
      
      return render(request,"order.html",{
        'order_list': order_list
      })
   else:
      return login2(request)
   