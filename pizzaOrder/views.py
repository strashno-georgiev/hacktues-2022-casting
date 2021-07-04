from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import OrderForm, FlourForm, SauceForm, ToppingForm
from .models import Order, Topping, Flour, Sauce
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers


def queryset_to_dicts(queryset):
    models = list(queryset)
    for model in models:
        model = model_to_dict(model)
    return models
# Create your views here.
def index(request):
    return render(request, "pizzaOrder/index.html")

def create_order(request):    
    if(request.method == "POST"):
        form = OrderForm(request.POST)
        if(form.is_valid):
            form.save()
    else:
        flours = Flour.objects.all()
        flour_dicts = serializers.serialize('json', flours, cls=DjangoJSONEncoder)
        
        sauces = Sauce.objects.all()
        sauces_json = serializers.serialize('json', sauces, cls=DjangoJSONEncoder)

        context = {}
        order_form = OrderForm()
        context['order_form'] = order_form
        context['flours_json'] = flour_dicts
        context['sauces_json'] = sauces_json

        return render(request, "pizzaOrder/create_order.html", context)

def add_topping(request):
    if(request.method == "POST"):
        form = ToppingForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect("topping-view")
    return render(request, "pizzaOrder/add_topping.html")

def add_flour(request):
    if(request.method == "POST"):
        form = FlourForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect("flour-view")
    return render(request, "pizzaOrder/add_flour.html")

def add_sauce(request):
    if(request.method == "POST"):
        form = SauceForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect("sauce-view")
    return render(request, "pizzaOrder/add_sauce.html")


def view_toppings(request):
    context = {}
    toppings = Topping.objects.all()
    if(len(toppings) == 0):
        context['none'] = True
    context['toppings'] = toppings
    return render(request, "pizzaOrder/view_topping.html", context)

def view_flours(request):
    context = {}
    flours = Flour.objects.all()
    if(len(flours) == 0):
        context['none'] = True
    context['flours'] = flours
    return render(request, "pizzaOrder/view_flour.html", context)

def view_sauces(request):
    context = {}
    sauces = Sauce.objects.all()
    if(len(sauces) == 0):
        context['none'] = True
    context['sauces'] = sauces
    return render(request, "pizzaOrder/view_sauce.html", context)


def delete_topping(request):
    pass

def delete_flour(request):
    pass

def delete_sauce(request):
    pass
