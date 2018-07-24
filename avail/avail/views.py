from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

import psycopg2
from .models import MyMobileModel

try:
    conn = psycopg2.connect("dbname=Scraping user=postgres password=anushka1234 port=5433")
    # use our connection values to establish a connection
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # run a SELECT statement - no data in there, but we can try it
    cursor.execute("""SELECT * from mobile_mymobilemodel""")
    rows = cursor.fetchall()
    print(rows)
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)

def home(request):
    return render(request,"homepage.html")
def about(request):
    return render(request,"about.html")
def signin(request):
    return render(request,"sign_in.html")
def categories(request):
    return render(request,"categories.html")
def mobiles(request):
    mobile_list = MyMobileModel.objects.all()[:25]
    print("mobile",mobile_list.values())
    return render("products.html", {'mobiles': mobile_list})

def mobileDetails(request):
    return render(request,"mobiledetails.html")
def Accesories(request):
    return render(request,"products1.html")
def Others(request):
    return render(request,"products2.html")
def samsung(request):
    return render(request,"samsung.html",{'content':['anuska','shrestha']})
def compare(request):
    return render(request,"compare.html")

def custom_response(request):
    import json
    data = [{'name': 'john', 'age': 25},{'name': 'john', 'age': 25}]
    return HttpResponse(json.dumps, content_type='application/json')


