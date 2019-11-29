from django.db import models
from datetime import datetime
from django.shortcuts import reverse

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length= 50)
    price = models.CharField(max_length= 50)
    description = models.TextField(max_length= 500)
    size = models.CharField(max_length= 6)
    sex = (
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Children', 'Children')

    )
    category = models.CharField(max_length = 100, choices = sex)
    image_front = models.ImageField()
    image_back = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("tfsapp: Product", kwargs={
        'slug': self.slug
        })

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

class Order(models.Model):
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
