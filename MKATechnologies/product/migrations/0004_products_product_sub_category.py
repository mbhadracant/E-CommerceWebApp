# Generated by Django 2.0.dev20170125212659 on 2017-03-06 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20170301_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_sub_category',
            field=models.CharField(default='GAMEING', max_length=200),
            preserve_default=False,
        ),
    ]
