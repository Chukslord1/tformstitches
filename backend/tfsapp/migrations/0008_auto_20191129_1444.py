# Generated by Django 2.2.5 on 2019-11-29 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfsapp', '0007_product_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]