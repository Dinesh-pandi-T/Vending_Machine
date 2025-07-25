# Generated by Django 5.2.1 on 2025-05-22 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending', '0003_beverage_coffee_price_beverage_coffee_qty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage',
            name='coffee_price',
            field=models.FloatField(default=10.0),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='coffee_qty',
            field=models.PositiveIntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='milk_price',
            field=models.FloatField(default=5.0),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='milk_qty',
            field=models.PositiveIntegerField(default=300),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='sugar_price',
            field=models.FloatField(default=3.0),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='sugar_qty',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='tea_price',
            field=models.FloatField(default=10.0),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='tea_qty',
            field=models.PositiveIntegerField(default=200),
        ),
    ]
