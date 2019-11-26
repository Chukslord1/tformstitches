from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("", include("tfsapp.urls", namespace="tfsapp")),
    path('admin/', admin.site.urls),
]
