from rest_framework.permissions import BasePermission

from content.models import Comment


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


class IsOwner(APIPermission):
    def has_object_permission(self, request, view, obj):
        return request.user and obj.owner == request.user


class IsCommentOrPostOwner(IsOwner):
    def has_object_permission(self, request, view, obj: Comment):
        is_comment_owner = super().has_object_permission(request, view, obj)
        is_post_owner = super().has_object_permission(request, view, obj.post)

        return is_comment_owner or is_post_owner
