from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    DestroyModelMixin,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from .querysets import PUBLIC_POSTS_QUERYSET
from .serializers import PostSerializer
from .filters import PostFilter


class PostAPIView(GenericAPIView):
    queryset = PUBLIC_POSTS_QUERYSET
    serializer_class = PostSerializer
    filterset_class = PostFilter

    search_fields = ["owner__name", "title"]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]


class PostListCreateView(ListModelMixin, CreateModelMixin, PostAPIView):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostRetrieveUpdateDestroyView(
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, PostAPIView
):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
