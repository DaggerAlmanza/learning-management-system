from app.models.user_model import UserModel
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'id',
            'username',
            'password',
            'email',
            'name',
            'last_name',
            'is_instructor',
            'is_active',
            'is_staff',
        ]
        read_only_fields = (
            'id',
            'is_active',
            'is_staff',
        )
