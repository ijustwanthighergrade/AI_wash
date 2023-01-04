from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return render(request,"index.html",locals())
def order(request):
   return render(request,"order.html",locals())