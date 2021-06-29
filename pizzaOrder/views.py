from pizzaApp.pizzaOrder.models import Person
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonForm
from .models import Person
# Create your views here.
def index(request):
    return render(request, "pizzaOrder/index.html")

def create_user(request):
    if(request.method == "POST"):
        form = PersonForm(request.POST)
        if(form.is_valid):
            form.save()
    else:
        context = {}
        form = PersonForm()
        context['form'] = form
        return render(request, "pizzaOrder/create_user.html", context)

def create_pizza(request):
    pass

def create_topping(request):
    pass

def create_flour(request):
    pass

def create_sauce(request):
    pass


def view_toppings(request):
    pass

def view_flours(request):
    pass

def view_sauces(request):
    pass


def delete_topping(request):
    pass

def delete_flour(request):
    pass

def delete_sauce(request):
    pass
