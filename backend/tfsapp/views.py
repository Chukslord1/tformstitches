from django.shortcuts import render, get_object_or_404
from .models import Product, OrderProduct, Order
from django.views.generic import ListView, DetailView

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

class IndexView(ListView):
    model = Product
    template_name = "index.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "single.html"

def add_to_cart(request, slug):
    Products = get_object_or_404(Product, slug=slug)
    Order_Products = OrderProducts.objects.create(Products=Products)
    order = Order.objects,filter(ordered=False)
