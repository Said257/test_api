from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User

# User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'gender', 'date_birth', 'hobby', 'country')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

