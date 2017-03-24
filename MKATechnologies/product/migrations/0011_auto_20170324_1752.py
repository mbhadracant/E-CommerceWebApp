# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_link',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_short_name',
            field=models.CharField(max_length=40),
        ),
    ]
