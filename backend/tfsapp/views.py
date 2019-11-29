from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView

# Create your views here.

def index(request):

    Products = Product.objects.all()

    return render(request, "index.html")

def mens(request):

    context = {
     'Products': Product.objects.all().filter(category ="Men")
    }

    return render(request, "mens.html", context)

def womens(request):
    return render(request, "womens.html")

def children(request):
    return render(request, "children.html")

def contact(request):
    return render(request, "contact.html")

def checkout(request):
    return render(request, "checkout.html")

def single(request):
    context = {
     'Products': Product.objects.all()
    }

    return render(request, "single.html", context)



class ProductDetailView(DetailView):
    model = Product
    template_name = "single.html"
