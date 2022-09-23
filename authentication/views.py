from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from .forms import SignUpForm, UserForm, UserProfileForm


default_pfp = 'authentication/images/default-avatar.jpg'

class SignUpFormView(FormView):
    template_name = 'authentication/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class ProfileDetailView(DetailView):
    template_name = 'authentication/profile.html'
    context_object_name = 'user'
    model = User

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dpfp'] = default_pfp
        return context


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect(request.path)
    else:
        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "authentication/update_profile.html", {"user_form": user_form, "user_profile_form": user_profile_form,
                                                           "dpfp": default_pfp})