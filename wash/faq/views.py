from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return render(request,"index.html",locals())
def faq(request):
   return render(request,"faq.html",locals())