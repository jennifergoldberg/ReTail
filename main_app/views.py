from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserCreationForm, ProfileCreationForm
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
        signup_user_form = NewUserCreationForm()
        signup_profile_form = ProfileCreationForm()
        context = {"signup_user_form": signup_user_form, "signup_profile_form": signup_profile_form}
        return render(request, 'registration/signup.html', context)
    def post(self, request):
            signup_user_form = NewUserCreationForm(request.POST)
            signup_profile_form = ProfileCreationForm(request.POST)
            if signup_user_form.is_valid() and signup_profile_form.is_valid():
                user = signup_user_form.save()
                profile = signup_profile_form.save()
                # assign user to profile
                profile.user = user
                profile.save()
                return redirect('registration/login.html')
            else:
                context = {"signup_user_form": signup_user_form, "signup_profile_form": signup_profile_form}
                return render(request, 'registration/signup.html', context)

# class Signup(View):
#     def get(self, request):
#         # signup_form = UserCreationForm()
#         signup_user_form = NewUserCreationForm()
#         signup_profile_form = ProfileCreationForm()
#         # context = {"signup_form": signup_form, "signup_user_form": signup_user_form, "signup_profile_form": signup_profile_form}
#         # return render(request, 'registration/signup.html', context)
#         context = {"signup_user_form": signup_user_form, "signup_profile_form": signup_profile_form}
#         return render(request, 'registration/signup.html', context)
#     def post(request):
#             new_user_form = NewUserCreationForm(request.POST), ProfileCreationForm(request.POST)
#             # signup_form = UserCreationForm(request.POST)
#             # signup_user_form = NewUserCreationForm()
#             # signup_profile_form = ProfileCreationForm()
#             if new_user_form.is_valid():
#                 user = new_user_form.save()
#                 profile = new_user_form.save()
#                 # new_user = signup_user_form.save()
#                 # profile = signup_profile_form.save()
#                 profile.user = user
#                 # user.save()
#                 # profile.save()
#                 login(request, user)
#                 return redirect('profile_view')
#             else:
#                 # context = {"signup_form": signup_form, "signup_profile_form": signup_profile_form}
#                 # return render(request, 'registration/signup.html', context)
#                 context = {"new_user_form": new_user_form}
#                 return render(request, 'registration/signup.html', context)

class Login(LoginView):
    def get_success_url(self):
        url = self.get_redirect_url()
        return url('profile_view', kwargs={'pk': self.request.user.pk})

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