# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("account_login")
    template_name = "account/signup.html"


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Your dashboard view code goes here
    return render(request, 'dashboard.html')

def profile(request):
    if request.user.is_authenticated:
        # User is already logged in, redirect them to the appropriate page
        return render(request, 'dashboard/dashboard.html')

 

    else:
        

        return render(request, 'accounts/login.html')


from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("account_login")
    template_name = "accounts/signup.html"