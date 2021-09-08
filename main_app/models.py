from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField, TextField, BooleanField
from django.contrib.auth.models import User

# Create your models here.


class Profile(Model):
  user = models.OneToOneField(User, on_delete=CASCADE, related_name='profile')
  avatar = TextField(max_length=500, blank=True)
  bio = TextField(max_length=2500, blank=True)
  location = TextField(max_length=500)
  org_name = TextField(max_length=500, blank=True)
  verified = BooleanField(default=False)

  def __str__(self):
    return self.user.username


class Post(Model):
  user = models.ForeignKey(User, on_delete=CASCADE, related_name='post')
  dog_name = TextField(max_length=500, blank=False)
  image = TextField(max_length=500, blank=False)
  image_two = TextField(max_length=500, blank=True)
  image_three = TextField(max_length=500, blank=True)
  bio = TextField(max_length=2500, blank=False)
  color = TextField(max_length=500, blank=True)
  gender = TextField(max_length=500, blank=True)
  friendly = TextField(max_length=500, blank=True)
  kids = TextField(max_length=500, blank=True)
  age = TextField(max_length=500, blank=True)
  breed = TextField(max_length=500, blank=True)
  size = TextField(max_length=500, blank=True)
  health = TextField(max_length=500, blank=True)
  active = TextField(max_length=500, blank=True)
  house_trained = BooleanField(default=False, blank=True)
  available = BooleanField(default=False, blank=False)
  created_at = DateTimeField(auto_now=False, auto_now_add=False)

  def __str__(self):
    return self.dog_name

  class Meta: 
    ordering = ['created_at']


class Comment(Model):
  user = models.ForeignKey(User, on_delete=CASCADE, related_name='comment')
  post = models.ForeignKey(Post, on_delete=CASCADE, related_name='comment')
  content = TextField(max_length=2500)
  created_at = DateTimeField(auto_now=False, auto_now_add=False)

  def __str__(self):
    return self.title

  class Meta: 
    ordering = ['created_at']