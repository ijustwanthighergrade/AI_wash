from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return render(request,"index.html",locals())
def complain(request):
   return render(request,"complain.html",locals())
