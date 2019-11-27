# Generated by Django 2.2.5 on 2019-11-25 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('price', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('image_front', models.ImageField(upload_to='')),
                ('image_back', models.ImageField(upload_to='')),
            ],
        ),
    ]