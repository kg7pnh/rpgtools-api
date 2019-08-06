# -*- coding: utf-8 -*-
"""
Defines the Book views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from api.models.organization import Organization
from api.models.organization import Serializer


class ItemView(generics.RetrieveUpdateDestroyAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Organization.organizations.all()
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    '''
    Provides access to the GET request for a list of all game objects.
    '''
    queryset = Organization.organizations.all()
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    '''
    Provides access to the POST request for creating game objects.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Organization.organizations.all()
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        '''
        create
        '''
        id = slugify(request.data['name']) # pylint: disable=redefined-builtin, invalid-name

        queryset = Organization.organizations.filter(id=id)

        if queryset.count() != 0:
            detail = 'A Organization entry already exists with the id '+id
            raise serializers.ValidationError(detail)

        return super(CreateView, self).create(request, *args, **kwargs)
