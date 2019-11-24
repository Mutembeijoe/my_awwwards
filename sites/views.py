from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Site

# Create your views here.


class SiteListView(ListView):
    model = Site
    template_name = 'home.html'
