# Generated by Django 2.2.5 on 2019-11-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfsapp', '0005_order_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='test-product'),
            preserve_default=False,
        ),
    ]
