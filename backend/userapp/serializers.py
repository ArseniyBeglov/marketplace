from rest_framework import serializers
from .models import MyUser

class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password', 'fio', 'birthday', 'sex', 'about', 'is_seller')
