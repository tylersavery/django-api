from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response


class PageNumberPagination(pagination.PageNumberPagination):

    last_page_strings = ["last"]
    max_page_size = settings.API_MAX_PAGE_SIZE
    page_query_param = "page"
    page_size = settings.API_DEFAULT_PAGE_SIZE
    page_size_query_param = "limit"

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "page": self.page.number,
                "num_pages": self.page.paginator.num_pages,
                "limit": self.page.paginator.per_page,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "results": data,
            }
        )
