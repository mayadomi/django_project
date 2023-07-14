# from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ViewAccount(generic.CreateView):
    form_class = CustomUserChangeForm
    template_name = 'users/viewAccount.html'
    success_url = reverse_lazy('view-account')