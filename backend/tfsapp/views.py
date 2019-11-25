from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def mens(request):
    return render(request, "mens.html")
