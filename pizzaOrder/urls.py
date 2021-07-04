"""pizzaApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('new-order/', views.create_order, name="create-order"),
    path('flours/', views.view_flours, name="flour-view"),
    path('sauces/', views.view_sauces, name="sauce-view"),
    path('toppings/', views.view_toppings, name="topping-view"),
    path('new-flour/', views.add_flour, name="add-flour"),
    path('new-sauce/', views.add_sauce, name="add-sauce"),
    path('new-topping/', views.add_topping, name="add-topping"),
    path('delete-flour/<int:pk>', views.delete_flour, name="delete-flour"),
    path('delete-sauce/<int:pk>', views.delete_sauce, name="delete-sauce"),
    path('delete-topping/<int:pk>', views.delete_topping, name="delete-topping"),
    path('delete-order/<int:pk>', views.delete_order, name="delete-order"),
    path('update-flour/<int:pk>', views.update_flour, name="update-flour"),
    path('update-sauce/<int:pk>', views.update_sauce, name="update-sauce"),
    path('update-topping/<int:pk>', views.update_topping, name="update-topping"),




]
