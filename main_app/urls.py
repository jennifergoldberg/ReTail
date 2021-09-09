from django.urls import path
from . import views
from .views import Home, DogView, Signup, ProfileView, DogDetail

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('dogs/', DogView.as_view(), name='dogs_view'),
  path('accounts/signup/', Signup.as_view(), name='signup'),
  path('accounts/profile/<int:pk>/', ProfileView.as_view(), name='profile_view'),
  path('dogs/<int:pk>/', DogDetail.as_view(), name='dog_detail')
]