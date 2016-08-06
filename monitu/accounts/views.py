from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

from registration.backends.default.views import RegistrationView
from .forms import RegisterForm


@login_required
def home(request):
    return render(request, 'home.html', {})


class RegisterView(RegistrationView):
    form_class = RegisterForm
    context = None

