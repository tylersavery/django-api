from content.models import Post
from django_filters import FilterSet, NumberFilter


class PostFilter(FilterSet):
    owner = NumberFilter(field_name="owner")

    class Meta:
        model = Post
        fields = ["owner"]
