from django.db import models

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)

class Sauce(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200, blank=True)

class Flour(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, blank=True)

class Pizza(models.Model):
    toppings = models.ManyToManyField("Topping", blank=True)
    sauce = models.ForeignKey("Sauce", to_field="name", default="tomato", on_delete=models.CASCADE)
    dough_flour = models.ForeignKey("Flour", to_field="name", default="white", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)

class Order(models.Model):
    address = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)