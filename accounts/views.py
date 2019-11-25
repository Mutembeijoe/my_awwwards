from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm


# Create your views here.


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'profile.html'


class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name="signup.html"
    # fields = ('username', 'password1','email', 'telephone', 'bio')
    success_url = reverse_lazy('login')

class UserUpdateView(UpdateView):
    model=CustomUser
    template_name='update_profile.html'
    fields = ('avatar','bio','telephone')
    # success_url= reverse_lazy('profile', args=[user.id])