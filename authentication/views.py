from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic.edit import FormView
from .forms import SignUpForm


class SignUpFormView(FormView):
    template_name = 'authentication/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
