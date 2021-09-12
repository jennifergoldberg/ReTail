from django.urls import path
from . import views
from .views import Home, PostView, Signup, ProfileView, PostDetail, PostCreate

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('dogs/', PostView.as_view(), name='posts_view'),
  path('accounts/signup/', Signup.as_view(), name='signup'),
  path('accounts/profile/<int:pk>/', ProfileView.as_view(), name='profile_view'),
  path('dogs/<int:pk>/', PostDetail.as_view(), name='post_detail'),
  path('dogs/new/', PostCreate.as_view(), name='post_create')
]