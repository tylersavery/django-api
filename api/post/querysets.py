from content.models import Post

ALL_POSTS_QUERYSET = Post.objects.all().exclude(status=Post.Status.REMOVED)
PUBLIC_POSTS_QUERYSET = Post.objects.filter(status=Post.Status.PUBLISHED)
