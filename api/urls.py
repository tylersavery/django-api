from django.urls import include, path

urlpatterns = [
    path("post/", include("api.post.urls")),
    # path("comments/", include("api.comment.urls")),
]
