from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title


class Login(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class SignUp(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    retype_password = models.CharField(max_length=10)

    def __str__(self):
        return self.firstname
