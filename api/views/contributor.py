# -*- coding: utf-8 -*-
# TODO: update docstring
"""Defines the Contributor views
"""
from rest_framework import generics
from api.models.contributor import Contributor
from api.serializers.contributor import Serializer


class ItemView(generics.RetrieveAPIView):
    # TODO: update docstring
    """Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    """
    queryset = Contributor.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ListView(generics.ListAPIView):
    # TODO: update docstring
    """Provides access to the GET request for a list of all contributor objects.
    """
    queryset = Contributor.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
