from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return render(request,"index.html",locals())
def showfeedback(request):
   return render(request,"feedback.html",locals())