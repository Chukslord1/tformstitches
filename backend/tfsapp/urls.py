from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index2"),
    path("mens.html", views.mens, name="mens"),
    path("womens.html", views.womens, name="womens"),
    path("checkout.html", views.checkout, name="checkout"),
    path("contact.html", views.contact, name="contact"),
    path("single.html", views.single, name="single"),
]
