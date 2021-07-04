from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm
from .models import Order, Topping, Flour, Sauce
import json
from django.core.serializers.json import DjangoJSONEncoder

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
        flours_json = json.dumps(list(flours), cls=DjangoJSONEncoder)

        sauces = Sauce.objects.all()
        sauces_json = json.dumps(list(sauces), cls=DjangoJSONEncoder)
        context = {}
        order_form = OrderForm()
        context['order_form'] = order_form
        context['flours_json'] = flours_json
        context['sauces_json'] = sauces_json

        return render(request, "pizzaOrder/create_order.html", context)

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
