# Generated by Django 2.1.5 on 2019-03-15 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_auto_20190315_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartinfo',
            name='price_currency',
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='totalprice_currency',
        ),
        migrations.RemoveField(
            model_name='productsinfo',
            name='price_currency',
        ),
        migrations.AlterField(
            model_name='cartinfo',
            name='price',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='totalprice',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='productsinfo',
            name='price',
            field=models.PositiveIntegerField(default=20),
        ),
    ]
