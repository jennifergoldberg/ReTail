from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView, View

from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileCreationForm

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

class Signup(View):
    def get(self, request):
        signup_form = UserCreationForm()
        signup_profile_form = ProfileCreationForm()
        context = {"signup_form": signup_form, "signup_profile_form": signup_profile_form}
        return render(request, 'registration/signup.html', context)