from rest_framework.permissions import BasePermission


class IsProviderPermission(BasePermission):
    def has_permission(self, request, view):
            return True