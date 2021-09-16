from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateForm, NewUserCreationForm, ProfileCreationForm
from .models import User, Post, Comment, Profile

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class PostView(TemplateView):
    template_name = 'posts_view.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        breed = self.request.GET.get("breed")
        dog_name = self.request.GET.get("dog_name")

        if breed != None or dog_name != None:
            context["breed"] = Post.objects.filter(breed__icontains=breed)        
            context["dog_name"] = Post.objects.filter(dog_name__icontains=dog_name) 
        else:
            context['posts'] = Post.objects.all()
        return context

    # def post(self, request):
    #         if request.method == "POST":
    #             searched = request.POST['searched']
    #             posts = Post.objects.filter(name__icontains=searched)
    #             users = User.objects.annotate(full_name=Concat('first_name', V(' '), 'last_name')).\
    #                 filter(full_name__icontains=searched)
    #             return render(request, 'search.html', {'searched': searched, 'hikes': hikes, 'users': users})
    #         else: 
    #             return render(request, "search.html", {}) 

class Signup(View):
    def get(self, request):
        signup_user_form = NewUserCreationForm()
        signup_profile_form = ProfileCreationForm()
        context = {"signup_user_form": signup_user_form, "signup_profile_form": signup_profile_form}
        return render(request, 'registration/signup.html', context)
    def post(self, request):
            signup_user_form = NewUserCreationForm(request.POST)
            signup_profile_form = ProfileCreationForm(request.POST)
            if signup_user_form.is_valid():
                user = signup_user_form.save()
                profile = Profile(user=user)
                # profile.user = user
                profile.save()
                print(f"==== {profile} ===")
                login(request, user)
                return redirect('login')
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

class ProfileDetail(DetailView):
    template_name = 'profile_detail.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['posts'] = Post.objects.all()
        context['profiles'] = Profile.objects.all()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostCreate(CreateView):
    template_name = 'post_create.html'
    model = Post
    fields = ['dog_name', 'image', 'image_two', 'image_three', 'bio', 'color', 'gender', 'friendly', 'kids', 'age', 'breed', 'size', 'health', 'active', 'house_trained', 'available']
    form = CreateForm()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostUpdate(UpdateView):
    template_name = 'post_update.html'
    model = Post
    fields = ['dog_name', 'image', 'image_two', 'image_three', 'bio', 'color', 'gender', 'friendly', 'kids', 'age', 'breed', 'size', 'health', 'active', 'house_trained', 'available']

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse('profile_detail', kwargs={'pk':user_id})

class ProfileUpdate(UpdateView):
    template_name = 'profile_update.html'
    model = Profile
    fields = ['avatar', 'bio', 'location', 'org_name', 'verified']

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse('profile_detail', kwargs={'pk':user_id})

