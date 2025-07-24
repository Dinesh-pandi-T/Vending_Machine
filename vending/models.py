from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.quantity})"

class Beverage(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tea_qty = models.PositiveIntegerField(default=10)
    coffee_qty = models.PositiveIntegerField(default=10)
    milk_qty = models.PositiveIntegerField(default=15)
    sugar_qty = models.PositiveIntegerField(default=5)

    tea_price = models.FloatField(default=10.0)
    coffee_price = models.FloatField(default=10.0)
    milk_price = models.FloatField(default=5.0)
    sugar_price = models.FloatField(default=3.0)

    def __str__(self):
        return self.name
