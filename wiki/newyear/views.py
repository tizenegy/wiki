from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    now = datetime.now()
    if now.month == 1 and now.day == 1:
        answer = ""
    else:
        answer = "not "
    return render(request, "newyear/index.html", {
        "newyear": answer
    })

def yourmum(request):
    return render(request, "newyear/yourmum.html")

def hismum(request, name):
    return render(request, "newyear/hismum.html", {"name":name})

def lisa(request, name):
    return render(request, "newyear/lisa.html", {"name":name})