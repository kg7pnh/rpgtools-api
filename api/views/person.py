# -*- coding: utf-8 -*-
"""
Defines the Book views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from api.models.person import Person
from api.models.person import Serializer


class ItemView(generics.RetrieveUpdateDestroyAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Person.people.all()
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    '''
    Provides access to the GET request for a list of all game objects.
    '''
    queryset = Person.people.all()
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    '''
     Provides access to the POST request for creating game objects.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Person.people.all()
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        name_prefix = request.data['name_prefix']
        name_first = request.data['name_first']
        name_middle = request.data['name_middle']
        name_last = request.data['name_last']
        name_suffix = request.data['name_suffix']
        id = slugify(name_prefix+" "+
                     name_last+" "+
                     name_first+" "+
                     name_middle+" "+
                     name_suffix) # pylint: disable=redefined-builtin, invalid-name

        queryset = Person.people.filter(id=id)

        if queryset.count() != 0:
            detail = 'A Person entry already exists with the id '+id
            raise serializers.ValidationError(detail)

        return super(CreateView, self).create(request, *args, **kwargs)
