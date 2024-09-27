from django.shortcuts import render
from django.views import generic
from .models import Item

# Create your views here.
class ItemList(generic.ListView):
    model = Item