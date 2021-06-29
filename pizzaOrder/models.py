from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Topping(models.Model):
    name = models.CharField(max_length=45)
    taste = models.CharField(max_length=45)

class Pizza(models.Model):
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    toppings = models.ManyToManyField("Topping")