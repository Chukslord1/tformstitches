# Generated by Django 2.2.5 on 2019-11-29 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfsapp', '0009_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
