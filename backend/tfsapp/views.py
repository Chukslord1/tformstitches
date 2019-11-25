from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def mens(request):
    return render(request, "mens.html")

def womens(request):
    return render(request, "womens.html")

def single(request):
    return render(request, "single.html")

def contact(request):
    return render(request, "contact.html")

def checkout(request):
    return render(request, "checkout.html")
