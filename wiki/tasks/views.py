from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

tasks =["foo", "bar", "baz"]

def index(request):
    return render(request, "tasks/index.html", {"tasks": tasks})
