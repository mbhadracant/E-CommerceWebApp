# Generated by Django 2.0.dev20170125212659 on 2017-03-22 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20170306_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product_sub_category',
            new_name='product_subcategory',
        ),
        migrations.AlterField(
            model_name='orders',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Users'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]