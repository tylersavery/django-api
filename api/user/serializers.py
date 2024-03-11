from rest_framework import serializers
from access.models import User


class UserPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "name",
            "bio",
        ]
