from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return render(request,"index.html",locals())
def detail(request):
   return render(request,"more.html",locals())
