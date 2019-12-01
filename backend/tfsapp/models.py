from django.db import models
from datetime import datetime
from django.shortcuts import reverse

from tfsapp.utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length= 50)
    price = models.CharField(max_length= 50)
    discount_price = models.FloatField(blank=True, null=True)
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
    slug = models.SlugField(null=True, blank=True)
    quantity= models.IntegerField(default=1)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("tfsapp:Product", kwargs={
            'slug': self.slug
        })

def slug_save(sender, instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name, instance.slug)

pre_save.connect(slug_save, sender=Product)

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def _str_(self):
        return self.name
    quantity= models.IntegerField(default=1)
    
class Order(models.Model):
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
