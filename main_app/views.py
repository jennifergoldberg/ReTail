from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileCreationForm
from .models import User, Post, Comment

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
    def post(request):
        if request.method == 'POST':
            signup_form = UserCreationForm()
            signup_profile_form = ProfileCreationForm()
        if signup_form.is_valid():
            user = signup_form.save()
            profile = signup_profile_form.save()
            profile.user = user
            user.save()
            profile.save()
            login(request, user)
            return redirect('profile_view')
        else:
            context = {"signup_form": signup_form, "signup_profile_form": signup_profile_form}
            return render(request, 'registration/signup.html', context)



class ProfileView(TemplateView):
    template_name = 'profile_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DogDetail(DetailView):
    model = Post
    template_name = 'dog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context