from django.db.models import Q
from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError
from uuid import uuid4


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(max_length=80, min_length=8, required=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, max_length=80, min_length=8,
                                      required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        account = User(username=self.validated_data['username'])
        username = self.validated_data['username']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        specialchar = ['$', '@', '#', '%']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        if User.objects.filter(username=account).exists():
            raise serializers.ValidationError({'message': 'User Already exists '})
        if len(password) < 8:
            raise serializers.ValidationError({'message': 'Password length should be a minimum of characters'})
        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError({'message': 'Password at least one numerical digit.'})
        if not any(char.islower() for char in password):
            raise serializers.ValidationError({'message': 'Password at least one lowercase character'})
        if not any(char.isupper() for char in password):
            raise serializers.ValidationError({'message': 'Password at least one uppercase character'})
        if not any(char in specialchar for char in password):
            raise serializers.ValidationError({'message': 'Password at least one Special Character'})
        else:
            account.set_password(username)
            account.set_password(password)
            account.save()
            raise serializers.ValidationError({'message': 'Registration successfully'})
