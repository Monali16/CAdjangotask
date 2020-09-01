from django.urls import path, include
from rest_framework import routers
from . import views
from .views import HomePageView

router = routers.DefaultRouter()
router.register(r'blog', views.BlogViewSet)
router.register(r'Login', views.LoginViewSet)
router.register(r'SignUp', views.SignUpViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api_auth', include('rest_framework.urls', namespace='rest_framework')),
    path('users', views.HomePageView.as_view(), name='home'),
]
