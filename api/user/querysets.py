from access.models import User


ALL_USERS_QUERYSET = User.objects.filter(is_active=True)
