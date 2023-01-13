from django.shortcuts import render
from django.http import HttpResponse
from login.views import login2
from feedback.models import REPROBLEMS
from member.models import COLOR

def index(request):
   if 'mem_session' in request.session:
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      return render(request,"index.html",locals())
   else:
      return login2(request)
   
def complain(request):
   prob_list=""
   if 'mem_session' in request.session:
      prob = REPROBLEMS.objects.filter(MEMID=request.session['mem_session'])
      prob_list =list(prob.values())
      print(prob_list)
      # print(prob_list[1]['PID'])
      print(len(prob_list))
      mycolor=COLOR.objects.get(MEMID=request.session['mem_session']).WHICHCOLOR
      print(mycolor)
      if prob_list != "":
         return render(request,"complain.html",{
         'prob_list': prob_list,
         'mycolor':mycolor
      })
      else:
         return render(request,"complain.html",{
         'mycolor':mycolor
      })
   else:
      return login2(request)
