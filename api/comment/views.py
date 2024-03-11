from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import (
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from .querysets import ALL_COMMENTS_QUERYSET
from .serializers import CommentSerializer, CommentCreateSerializer

from api.permissions import AllowAny, IsAuthenticated, IsCommentOrPostOwner
from content.models import Comment
from api.exceptions import BadRequest


# region base class


class CommentAPIView(GenericAPIView):
    queryset = ALL_COMMENTS_QUERYSET
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    ordering_fields = ["created_at"]
    ordering = ["-created_at"]


# endregion

# region public


class CommentListView(ListModelMixin, CommentAPIView):

    def get(self, request, *args, **kwargs):

        if kwargs.get("uuid"):
            self.queryset = ALL_COMMENTS_QUERYSET.filter(post__uuid=kwargs.get("uuid"))
        elif kwargs.get("pk"):
            self.queryset = ALL_COMMENTS_QUERYSET.filter(post__id=kwargs.get("pk"))
        else:
            raise BadRequest()

        return self.list(request, *args, **kwargs)


# endregion

# region authenticated


class CommentCreateView(CommentAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        owner = serializer.validated_data.get("owner")
        post = serializer.validated_data.get("post")
        body = serializer.validated_data.get("body")

        comment = Comment.objects.create(
            owner=owner,
            post=post,
            body=body,
        )

        return Response(
            CommentSerializer(comment).data,
            status=status.HTTP_201_CREATED,
        )


class CommentRetrieveUpdateDestroyView(
    RetrieveModelMixin, DestroyModelMixin, CommentAPIView
):

    permission_classes = [AllowAny]

    def get_permissions(self):

        if self.request.method == "DELETE":
            self.permission_classes = [IsCommentOrPostOwner]

        return super().get_permissions()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance: Comment):
        instance.is_deleted = True
        instance.save()


# endregion
