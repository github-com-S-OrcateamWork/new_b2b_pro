# Generated by Django 4.1.7 on 2023-08-09 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
