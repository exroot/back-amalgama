from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['name', 'email', 'is_admin', 'profile_image', 'date_of_birth']