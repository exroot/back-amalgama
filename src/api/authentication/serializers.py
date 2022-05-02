from rest_framework import serializers
from src.api.users.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.http import JsonResponse
from django.contrib import auth

class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""
    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
        error_messages={
            "min_length": "Password should be at least {min_length} characters"
        }
    )

    date_of_birth = serializers.CharField(
        required=True
    )
    
    name = serializers.CharField(
        required=True
    )

    profile_image = serializers.CharField(
        required=True
    )

    class Meta:
        model = User
        fields = ['email', 'password', 'date_of_birth', 'profile_image', 'name']

    def validate(self, value):
        # validate data
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    """
    Logs in a user,
    creates an access token
    access token is short lived
    """
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(required=False)
    profile_image = serializers.CharField(required=False)
    date_of_birth = serializers.CharField(required=False)
    is_admin = serializers.BooleanField(required=False)
    password = serializers.CharField(max_length=128, write_only=True)
    tokens = serializers.SerializerMethodField()
    def get_tokens(self, user):
        return {
            'refresh': user.token()['refresh'],
            'access': user.token()['access']
        }

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = auth.authenticate(email=email.lower(), password=password)
        if user is None:
            raise AuthenticationFailed(
                'Incorrect email password combination,check and try again', 401
            )
        return user

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    device_token = serializers.CharField(required=False)

    def validate(self, attrs):
        self.token = attrs['refresh_token']
        self.device_token = attrs.get('device_token', None)
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except Exception as e:
            raise AuthenticationFailed('The refresh token is invalid', 401)