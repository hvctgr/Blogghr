from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        from users.api import UserDetailAPI

        if request.method == 'POST' or request.user.is_superuser:
            return True

        return request.user.is_authenticated and isinstance(view, UserDetailAPI)

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj
