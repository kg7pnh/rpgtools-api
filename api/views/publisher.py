# -*- coding: utf-8 -*-
"""
Defines the Publisher views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from api.models.publisher import Publisher
from api.models.publisher import Serializer


class ItemView(generics.RetrieveUpdateDestroyAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Publisher.publishers.all()
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    '''
    Provides access to the GET request for a list of all game objects.
    '''
    queryset = Publisher.publishers.all()
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    '''
     Provides access to the POST request for creating game objects.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Publisher.publishers.all()
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        id = slugify(name) # pylint: disable=redefined-builtin, invalid-name

        queryset = Publisher.publishers.filter(id=id)

        if queryset.count() != 0:
            detail = 'A Publisher entry already exists with the id '+id
            raise serializers.ValidationError(detail)

        return super(CreateView, self).create(request, *args, **kwargs)
