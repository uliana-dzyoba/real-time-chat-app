from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    # username = forms.CharField(max_length=25, required=True,
    #                            widget=forms.TextInput(attrs={'placeholder': '*Username..'}))
    # first_name = forms.CharField(max_length=30, required=True,
    #                              widget=forms.TextInput(attrs={'placeholder': '*Your first name..'}))
    # last_name = forms.CharField(max_length=30, required=True,
    #                             widget=forms.TextInput(attrs={'placeholder': '*Your last name..'}))
    # email = forms.EmailField(max_length=254, required=True,
    #                          widget=forms.EmailInput(attrs={'placeholder': '*Email address..'}))
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'placeholder': '*Password..', 'class': 'password'}))
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..', 'class': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
