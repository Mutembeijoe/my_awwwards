from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import CustomUser

# Create your views here.


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'profile.html'


class UserCreateView(CreateView):
    model = CustomUser
    template_name="signup.html"
    fields = ('username', 'email', 'telephone', 'bio')