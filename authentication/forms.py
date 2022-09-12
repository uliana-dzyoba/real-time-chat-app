from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", 'email',)


class UserProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('bio', 'phone_number', 'profile_pic')
