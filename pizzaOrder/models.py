from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Topping(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)

class Sauce(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)

class Flour(models.Model):
    grain = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)

class Pizza(models.Model):
    toppings = models.ManyToManyField("Topping")
    sauce = models.ForeignKey("Sauce", on_delete=models.CASCADE)
    dough_flour = models.ForeignKey("Flour", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)

class Order(models.Model):
    person = models.ForeignKey("Person", on_delete=models.CASCADE)