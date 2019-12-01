from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "tfsapp"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # path("index.html", views.IndexView.as_view(), name="index2"),
    path("mens", views.mens, name="mens"),
    path("womens", views.womens, name="womens"),
    path("checkout", views.checkout, name="checkout"),
    path("contact", views.contact, name="contact"),
    path("children", views.children, name="children"),
    path("product/<slug:slug_text>", views.single, name="product"),

]
