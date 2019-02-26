# Generated by Django 2.1.5 on 2019-02-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_auto_20190225_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameofprod', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('size', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
    ]
