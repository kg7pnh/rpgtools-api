# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_

Returns:
    _type_: _description_
"""
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAuthenticated):
    # TODO: update docstring
    """_summary_

    Args:
        permissions (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Custom permission to only allow owners of an object to edit them.
    # If admin access is also needed, IsAdmin should be used with IsTeamMember

    def has_object_permission(self, request, view, obj):
        # TODO: update docstring
        """_summary_

        Args:
            request (_type_): _description_
            view (_type_): _description_
            obj (_type_): _description_

        Returns:
            _type_: _description_
        """
        has_permission = False

        if request.method in permissions.SAFE_METHODS:
            has_permission = True

        else:
            user = request.user
            if user.is_staff:
                has_permission = True
        return has_permission
