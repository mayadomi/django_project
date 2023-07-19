from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        # fields = ['title', 'author', 'pub_date', 'content', 'image_url']
        fields = ['title', 'pub_date', 'content', 'image_url']
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%m/%d/%YT%H:%M:%S',
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'datetime-local'
                }
            ),
        }

class EditStoryForm(ModelForm):
    class Meta:
        model = NewsStory
        # fields = ['title', 'author', 'pub_date', 'content', 'image_url']
        fields = ['title', 'pub_date', 'content', 'image_url']
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%m/%d/%YT%H:%M:%S',
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'datetime-local'
                }
            ),
        }

