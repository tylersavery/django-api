from rest_framework import serializers
from content.models import Post
from api.user.serializers import UserPublicSerializer


class PostSerializer(serializers.ModelSerializer):

    owner = UserPublicSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "uuid",
            "title",
            "owner",
            "body",
            "status",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "uuid",
            "owner",
            "created_at",
        ]
