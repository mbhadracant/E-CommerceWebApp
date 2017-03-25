# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20170324_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='quantity',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='postcode_name',
            new_name='postcode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_id',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='order_date', max_length=200),
            preserve_default=False,
        ),
    ]
