from rest_framework.permissions import BasePermission


class APIPermission(BasePermission):
    allow_read_only = False

    @staticmethod
    def is_safe(request):
        return request.method in ["GET", "HEAD", "OPTIONS"]


class AllowAny(APIPermission):
    def has_permission(self, request, view):
        return True


class IsAdmin(APIPermission):
    def has_permission(self, request, view):
        return request.user and getattr(request.user, "is_admin", False)


class IsAuthenticated(APIPermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
