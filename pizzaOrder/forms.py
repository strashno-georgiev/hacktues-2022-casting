from django import forms
from .models import Flour, Topping, Pizza, Order, Sauce
  
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "address",
            "last_name"
        ]

class FlourForm(forms.ModelForm):
  
    class Meta:
        model = Flour
  
        fields = [
            "name",
            "description"
        ]

class SauceForm(forms.ModelForm):
  
    class Meta:
        model = Sauce
  
        fields = [
            "name",
            "description"
        ]

class ToppingForm(forms.ModelForm):
  
    class Meta:
        model = Topping
  
        fields = [
            "name",
            "description"
        ]

class PizzaForm(forms.ModelForm):
  
    class Meta:
        model = Pizza
  
        fields = [
            "dough_flour",
            "sauce",
            "toppings"
        ]
