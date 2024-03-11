from django.urls import path

from .views import (
    PostListCreateView,
    PostRetrieveView,
    PostMeListView,
    PostMeRetrieveUpdateDestroyView,
)

from api.comment.views import CommentListView

urlpatterns = [
    path("", PostListCreateView.as_view()),
    path("me/", PostMeListView.as_view()),
    path("<uuid:uuid>/", PostRetrieveView.as_view(lookup_field="uuid")),
    path("<int:pk>/", PostRetrieveView.as_view()),
    path(
        "me/<uuid:uuid>/", PostMeRetrieveUpdateDestroyView.as_view(lookup_field="uuid")
    ),
    path("me/<int:pk>/", PostMeRetrieveUpdateDestroyView.as_view()),
    path("<uuid:uuid>/comment/", CommentListView.as_view()),
    path("<int:pk>/comment/", CommentListView.as_view()),
]
