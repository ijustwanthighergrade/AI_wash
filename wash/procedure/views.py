from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


def wash1(request):
   con = sqlite3.connect("../db.sqlite3")
   cur = con.cursor()
   cur.execute("CREATE TABLE orders(ordernum, way, amounts, wash, dry, fold, special,getday,gettime,address,phone,card)")
   return render(request,"wash1.html",locals())

def wash2(request):
   
   return render(request,"wash2.html",locals())

def wash3(request):
   return render(request,"wash3.html",locals())

def wash4(request):
   return render(request,"wash4.html",locals())

def index(request):
   return render(request,"index.html",locals())

