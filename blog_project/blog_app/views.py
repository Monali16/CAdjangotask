from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BlogSerializer,LoginSerializer,SignUpSerializer
from .models import Blog,Login,SignUp
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('title')
    serializer_class = BlogSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all().order_by('username')
    serializer_class = LoginSerializer


class SignUpViewSet(viewsets.ModelViewSet):
    queryset = SignUp.objects.all().order_by('firstname')
    serializer_class = SignUpSerializer
