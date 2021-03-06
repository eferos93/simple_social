from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms


# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # once someone has signed up successfully, we redirect there when clicking on submit
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
