from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from .models import User, Profile

class NewUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

  def save(self, commit=True):
    user = super(NewUserCreationForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
      user.save()
    return user

class ProfileCreationForm(ModelForm):
  class Meta: 
    model = Profile
    fields = ['location']


GENDER_CHOICES =(
  ("M", "Male"),
  ("F", "Female"),
)

class CreateForm(forms.Form):
  gender = forms.ChoiceField(widget=forms.RadioSelect, choices = GENDER_CHOICES)