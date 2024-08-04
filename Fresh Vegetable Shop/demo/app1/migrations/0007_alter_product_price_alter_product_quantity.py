# Generated by Django 5.0.6 on 2024-08-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_ordermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='per kg Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(verbose_name='total stock in kg'),
        ),
    ]
