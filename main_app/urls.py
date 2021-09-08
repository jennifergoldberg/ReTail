from django.urls import path
from . import views
from .views import Home, DogView, Signup

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('dogs/', DogView.as_view(), name='dogs_view'),
  path('accounts/signup', Signup.as_view(), name='signup'),
]