from admin_auto_filters.filters import AutocompleteFilterFactory

from django.utils.translation import gettext_lazy as _

from django.contrib import admin
from content.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at", "updated_at")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("title", "body")
    date_hierarchy = "created_at"
    ordering = ("status", "created_at")
    autocomplete_fields = ("owner",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("body", "is_deleted", "created_at", "updated_at")
    list_filter = ("is_deleted", "created_at", "updated_at")
    search_fields = ("body",)
    date_hierarchy = "created_at"
    ordering = ("is_deleted", "created_at")
    autocomplete_fields = ("owner", "post")
    readonly_fields = ("created_at", "updated_at")
    actions = ["delete_comments"]
