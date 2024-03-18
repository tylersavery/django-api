from rest_framework import serializers
from access.models import User


class UserPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "uuid",
            "name",
            "bio",
        ]


class UserMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "uuid",
            "name",
            "bio",
            "email",
        ]
        read_only_fields = [
            "id",
            "uuid",
            "email",
        ]
