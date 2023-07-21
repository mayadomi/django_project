# from django.shortcuts import render

# Create your views here.

from typing import Any, Dict
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from news.models import NewsStory
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class StoriesList(generic.ListView):
    model = NewsStory

class ViewAccount(generic.CreateView):
    form_class = CustomUserChangeForm
    template_name = 'users/viewAccount.html'
    success_url = reverse_lazy('view-account')

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

        context['user_stories'] = NewsStory.objects.filter(author_id__exact=self.request.user.id)
        
        users = CustomUser.objects.get(id__exact=self.request.user.id)
        context['my_favorites'] = users.favorites.all()

        return context

