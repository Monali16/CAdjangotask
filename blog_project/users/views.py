from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
