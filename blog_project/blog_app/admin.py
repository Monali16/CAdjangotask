from django.contrib import admin
from . models import Blog, Login, SignUp

# Register your models here.
admin.site.register(Blog)
admin.site.register(Login)
admin.site.register(SignUp)
