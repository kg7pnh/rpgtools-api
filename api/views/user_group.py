# -*- coding: utf-8 -*-
# TODO: update docstring
"""Defines the user and group views
"""
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers.user_group import UserSerializer
from api.serializers.user_group import GroupSerializer
from api.permissions.admin import IsAdminOrReadOnly


class UserViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    # TODO: update docstring
    """API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = User.objects.all()  # pylint: disable=bad-option-value
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    # TODO: update docstring
    """API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Group.objects.all()  # pylint: disable=no-member
    serializer_class = GroupSerializer
