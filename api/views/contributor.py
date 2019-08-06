# -*- coding: utf-8 -*-
"""
Defines the GameSystem views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from api.models.contributor import Contributor
from api.models.contributor import Serializer


class ItemView(generics.RetrieveAPIView): #.RetrieveUpdateDestroyAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Contributor.contributors.all()
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    '''
    Provides access to the GET request for a list of all game objects.
    '''
    queryset = Contributor.contributors.all()
    serializer_class = Serializer