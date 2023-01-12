
from django.shortcuts import render
from django.http import HttpResponse
from pyexpat.errors import messages
import requests
from procedure.models import order
from login.models import MEMBER
from login.views import login2

def index(request):
   return render(request,"index.html",locals())