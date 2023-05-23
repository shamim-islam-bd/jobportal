from django.contrib.auth.models import User
from rest_framework import serializers

# make here pass hash password


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'password']
        
        extra_kwargs = {
            'first_name': {'required': True, 'allow_blank': False},
            'last_name': {'required': True, 'allow_blank': False},
            'email': {'required': True, 'allow_blank': False},
            'password': {'write_only': True, 'required': True, 'min_length': 4},
        }
        
        

class UserSerializer(serializers.ModelSerializer):
    resume = serializers.CharField(source='userprofile.resume', allow_blank=True, required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'resume']
        
        extra_kwargs = {
            'username': {'required': False}
        }