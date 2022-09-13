from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import SignUpForm, UserForm, UserProfileForm


class SignUpFormView(FormView):
    template_name = 'authentication/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect("authentication:profile")
    else:
        default_pfp = settings.MEDIA_URL + 'images/default-avatar.jpg'
        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "authentication/profile.html", {"user_form": user_form, "user_profile_form": user_profile_form,
                                                           "dpfp": default_pfp})
