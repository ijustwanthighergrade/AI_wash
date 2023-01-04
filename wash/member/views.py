from django.shortcuts import render
from django.http import HttpResponse


def index(request):
   return render(request,"index.html",locals())
def member(request):
   return render(request,"member.html",locals())