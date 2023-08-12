from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS)
