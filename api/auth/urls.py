from django.urls import include, path

urlpatterns = [
    path("token/", include("api.auth.token.urls")),
]
