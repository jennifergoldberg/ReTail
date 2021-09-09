from django import forms
from django.forms.models import ModelForm
from .models import Profile


class ProfileCreationForm(ModelForm):
  class Meta: 
    model = Profile
    fields = ['location']