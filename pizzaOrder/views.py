from django.db.models.query import QuerySet
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import OrderForm, FlourForm, SauceForm, ToppingForm
from .models import Order, Topping, Flour, Sauce, Pizza
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
    orders = Order.objects.all()
    context = {}
    pizzas = {}
    if(len(orders) == 0):
        context['none'] = True
    for order in orders:
        order_key = str(order.id)
        pizzas[order_key] = []
        pizzas[order_key].append(order)
        pizzas[order_key].append(Pizza.objects.filter(order__id=order.id))
    context['orders'] = pizzas
    return render(request, "pizzaOrder/index.html", context)

def create_order(request):    
    if(request.method == "POST"):
        form = OrderForm(request.POST['address'], request.POST['last_name'])
        if(form.is_valid):
            new_order = Order(address=request.POST['address'], last_name=request.POST['last_name'])
            new_order.save()
            pizza_count = (len(request.POST) - 3) // 3
            for i in range(1, pizza_count+1):
                dough_flour = Flour.objects.get(id=request.POST["dough_flour" + str(i)])
                sauce = Sauce.objects.get(id=request.POST["sauce" + str(i)])
                new_pizza = Pizza(sauce=sauce, dough_flour=dough_flour, order=new_order)
                new_pizza.save()
                print("\nrequest.POST on toppings is:\n" + request.POST['toppings1[]'])

                for topping_id in request.POST.getlist('toppings' + str(i) + "[]"):
                    new_pizza.toppings.add(topping_id)

            return redirect("home")
    else:
        def objects_to_json(objects):
            json = serializers.serialize('json', objects, cls=DjangoJSONEncoder)
            return json
        
        context = {}
        order_form = OrderForm()
        context['order_form'] = order_form
        context['flours_json'] = objects_to_json(Flour.objects.all())
        context['sauces_json'] = objects_to_json(Sauce.objects.all())
        context['toppings_json'] = objects_to_json(Topping.objects.all())


        return render(request, "pizzaOrder/create_order.html", context)
def delete_order(request, pk):

    order = Order.objects.get(id=pk)
    if(request.method == "POST"):
        order.delete()
        return redirect("home")
    context = {}
    context['order'] = order
    return render(request, "pizzaOrder/delete_order.html", context)

    
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


def delete_topping(request, pk):
    topping = Topping.objects.get(id=pk)
    if(request.method == "POST"):
        topping.delete()
        return redirect("topping-view")
    context = {}
    context['topping'] = topping
    return render(request, "pizzaOrder/delete_topping.html", context)

def delete_flour(request, pk):
    flour = Flour.objects.get(id=pk)
    if(request.method == "POST"):
        flour.delete()
        return redirect("flour-view")
    context = {}
    context['flour'] = flour
    return render(request, "pizzaOrder/delete_flour.html", context)

def delete_sauce(request, pk):
    sauce = Sauce.objects.get(id=pk)
    if(request.method == "POST"):
        sauce.delete()
        return redirect("sauce-view")
    context = {}
    context['sauce'] = sauce
    return render(request, "pizzaOrder/delete_sauce.html", context)

def update_topping(request, pk):
    topping = Topping.objects.get(id=pk)
    if(request.method == "POST"):
        form = ToppingForm(request.POST)
        if(form.is_valid):
            topping.name = request.POST['name']
            topping.description = request.POST['description']
            topping.save()
            return redirect("topping-view")
    context = {}
    context['topping'] = topping
    return render(request, "pizzaOrder/update_topping.html", context)

def update_flour(request, pk):
    flour = Flour.objects.get(id=pk)
    if(request.method == "POST"):
        form = FlourForm(request.POST)
        if(form.is_valid):
            flour.name = request.POST['name']
            flour.description = request.POST['description']
            flour.save()
            return redirect("flour-view")
    context = {}
    context['flour'] = flour
    return render(request, "pizzaOrder/update_flour.html", context)

def update_sauce(request, pk):
    sauce = Sauce.objects.get(id=pk)
    if(request.method == "POST"):
        form = SauceForm(request.POST)
        if(form.is_valid):
            sauce.name = request.POST['name']
            sauce.description = request.POST['description']
            sauce.save()
            return redirect("sauce-view")
    context = {}
    context['sauce'] = sauce
    return render(request, "pizzaOrder/update_sauce.html", context)
