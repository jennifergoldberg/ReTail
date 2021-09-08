from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DogView(TemplateView):
    template_name = 'dogs_view.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context