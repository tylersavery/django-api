from django.urls import path

from .views import PostListCreateView, PostRetrieveUpdateDestroyView, PostMeListView

urlpatterns = [
    path("", PostListCreateView.as_view()),
    path("me/", PostMeListView.as_view()),
    path("<uuid:uuid>/", PostRetrieveUpdateDestroyView.as_view(lookup_field="uuid")),
    path("<int:pk>/", PostRetrieveUpdateDestroyView.as_view()),
]
