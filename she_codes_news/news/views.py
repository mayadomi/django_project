from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views import View
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm, EditStoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date').all()[:4]
        return context
    
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditStoryView(generic.UpdateView):
    model = NewsStory
    form_class = EditStoryForm
    template_name = 'news/editStory.html'
    # success_url = reverse_lazy('news:story', kwargs={'id': self.object.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('news:story', kwargs={'pk': self.kwargs['pk']})

class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')

    # def form_valid(self, form):
    #         form.instance.author = self.request.user
    #         return super().form_valid(form)

class FavoriteStoryView(generic.detail.SingleObjectMixin, View):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get(self, request, *args, **kwargs):

        self.object = self.get_object()

        # Was trying to figure out a way to 'favorite/unfavorite' in the home
        # index page without it redirecting to the story, and only thing that came to mind
        # was to try and find the referring page... thought I could use the templates name but
        # that does what I initally got it to redirect from.... so played and saw that 
        # referrer seemed to work.... pretty sure it's not the best way to do this...but it works.

        if self.request.headers.get('Referer').endswith('/news/'):
            # return to index/home page
            response = reverse_lazy("news:index")
        else:
            # the only other place calling it at the moment is from story details....
            response = reverse_lazy("news:story", kwargs={"pk": self.object.pk})

        if self.object.favorites.filter(id=self.request.user.id):
            self.object.favorites.remove(self.request.user.id)
        else:
            self.object.favorites.add(self.request.user.id)

        return HttpResponseRedirect(response)

