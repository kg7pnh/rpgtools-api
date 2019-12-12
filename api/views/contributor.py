# -*- coding: utf-8 -*-
"""
Defines the Contributor views
"""
from rest_framework import generics
from api.models.contributor import Contributor
from api.serializers.contributor import Serializer

class ItemView(generics.RetrieveAPIView): #.RetrieveUpdateDestroyAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    """
    queryset = Contributor.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    """
    Provides access to the GET request for a list of all game objects.
    """
    queryset = Contributor.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
