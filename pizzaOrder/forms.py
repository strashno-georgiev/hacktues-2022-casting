from django import forms
from .models import Person, Flour, Topping, Pizza
  
  
class PersonForm(forms.ModelForm):
  
    class Meta:
        model = Person
  
        fields = [
            "first_name",
            "last_name",
            "address"
        ]

class FlourForm(forms.ModelForm):
  
    class Meta:
        model = Flour
  
        fields = [
            "grain",
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
