from rest_framework import serializers

from content.models import Comment
from api.user.serializers import UserPublicSerializer
from api.post.querysets import PUBLIC_POSTS_QUERYSET


class CommentSerializer(serializers.ModelSerializer):

    owner = UserPublicSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "uuid",
            "owner",
            "body",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "uuid",
            "owner",
            "created_at",
        ]


class CommentCreateSerializer(serializers.Serializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.SlugRelatedField(
        slug_field="uuid", queryset=PUBLIC_POSTS_QUERYSET
    )
    body = serializers.CharField()
