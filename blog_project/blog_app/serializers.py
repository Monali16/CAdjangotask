from rest_framework import serializers
from . models import Blog, Login, SignUp


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('title','description')


class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"


class SignUpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SignUp
        fields = "__all__"
