from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def bastian(request):
    return HttpResponse("hi, pfff!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })

def elfert(request,name):
    return render(request, "hello/bastian/elfert.html", {"name":name})