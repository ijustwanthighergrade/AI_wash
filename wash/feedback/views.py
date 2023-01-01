from django.shortcuts import render
from django.http import HttpResponse

def feedback(request):
   return render(request,"return.html",locals())

def index(request):
   return render(request,"index.html",locals())

