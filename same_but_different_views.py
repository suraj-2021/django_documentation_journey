from django.shortcuts import render

def my_view(request):
    return render(request,"appname/home.html", {"Greeting":"Hello"})


#Less popular way of writing view
from django.http import HttpResponse
from django.template import loader

def my_view(request):
    t = loader.get_template("appname/home.html")
    c = {"Greeting": "Hello"}

    return HttpResponse(t.render(c,request))
