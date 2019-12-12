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

        # user = request.user
        # has_permission = False
        # # Read permissions are allowed to any request,
        # # so we'll always allow GET, HEAD or OPTIONS requests.
        # #if user.is_authenticated and request.method in permissions.SAFE_METHODS:
        # if user.is_authenticated and request.method in permissions.SAFE_METHODS:
        #     has_permission = True

        # elif user.is_staff:
        #     has_permission = True
        has_permission = False

        if request.method in permissions.SAFE_METHODS:
            has_permission = True

        else:
            user = request.user
            if user.is_staff:
                has_permission = True
        return has_permission
