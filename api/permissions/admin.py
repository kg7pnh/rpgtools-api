"""
Defines admin settings
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAuthenticated):
    """
    Custom permission to only allow owners of an object to edit them.
    If admin access is also needed, IsAdmin should be used with IsTeamMember
    """

    def has_object_permission(self, request, view, obj):
        """
        has_object_permission
        """
        has_permission = False

        if request.method in permissions.SAFE_METHODS:
            has_permission = True

        else:
            user = request.user
            if user.is_staff:
                has_permission = True
        return has_permission
