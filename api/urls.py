from django.urls import include, path

urlpatterns = [
    path("auth/", include("api.auth.urls")),
    path("post/", include("api.post.urls")),
    path("comment/", include("api.comment.urls")),
]
