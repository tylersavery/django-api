from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    DestroyModelMixin,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from api.permissions import AllowAny, IsAuthenticated


from .querysets import ALL_USERS_QUERYSET
from .serializers import UserPublicSerializer, UserMeSerializer


# region base
class UserAPIView(GenericAPIView):
    queryset = ALL_USERS_QUERYSET
    serializer_class = UserPublicSerializer
    permission_classes = [AllowAny]

    search_fields = ["name"]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]


class UserMeAPIView(UserAPIView):
    serializer_class = UserMeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# endregion


# region public


class UserListView(ListModelMixin, UserAPIView):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserRetrieveView(RetrieveModelMixin, UserAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# endregion

# region private


class UserMeRetrieveUpdateView(RetrieveModelMixin, UpdateModelMixin, UserMeAPIView):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# endregion
