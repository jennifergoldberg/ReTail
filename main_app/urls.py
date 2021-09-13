from django.urls import path
from . import views
from .views import Home, PostView, ProfileDetail, Signup, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('dogs/', PostView.as_view(), name='posts_view'),
  path('accounts/signup/', Signup.as_view(), name='signup'),
  path('accounts/profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
  path('dogs/<int:pk>/', PostDetail.as_view(), name='post_detail'),
  path('dogs/new/', PostCreate.as_view(), name='post_create'),
  path('dogs/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
  path('dogs/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

]