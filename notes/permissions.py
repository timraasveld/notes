from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permission to only allow owners of an object to CRUD
    """

    def has_object_permission(self, request, view, object):
        # All permissions are only allowed to the owner of the object.
        return object.user == request.user