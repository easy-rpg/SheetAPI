from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Permissions are only allowed to the owner of the personagem
        return obj.owner == request.user


class IsOwnerOrRead(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # Edit permissions are only allowed to the owner of the personagem
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user
