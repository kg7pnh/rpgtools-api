# -*- coding: utf-8 -*-
"""
Defines the Publisher views
"""
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models.publisher import Publisher
from api.models.publisher import Serializer

class ItemView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Publisher.publishers.all()
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    '''
    Provides access to the GET request for a list of all publisher objects.
    '''
    queryset = Publisher.publishers.all()
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    '''
    Provides access to the POST request for creating publisher objects.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Publisher.publishers.all()
    serializer_class = Serializer
