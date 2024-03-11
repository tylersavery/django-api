from content.models import Comment

ALL_COMMENTS_QUERYSET = Comment.objects.filter(is_deleted=False)
