from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic.edit import FormView
from .forms import SignUpForm


class SignUpFormView(FormView):
    template_name = 'authentication/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#
#             login(request, user)
#
#             return redirect('frontpage')
#     else:
#         form = SignUpForm()
#
#     return render(request, 'core/signup.html', {'form': form})