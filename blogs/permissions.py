from django.utils import timezone
from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):

        def has_permission(self, request, view):
            return request.method == 'GET' or request.user.is_authenticated

        def has_object_permission(self, request, view, obj):

            if request.method == 'GET':
                return obj.owner == request.user or request.user.is_superuser or obj.publication_date <= timezone.now()

            return obj.owner == request.user or request.user.is_superuser
