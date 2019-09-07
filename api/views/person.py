# -*- coding: utf-8 -*-
"""
Defines the Book views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models.person import Person
from api.models.person import concat_name
from api.models.person import Serializer
from api.permissions.admin import IsAdminOrReadOnly


class ItemView(generics.RetrieveAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    '''    
    queryset = Person.objects.all()
    serializer_class = Serializer
    lookup_field = "id"

class ItemEditView(generics.UpdateAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the PATCH and PUT requests for a given ID.
    '''
    permission_classes = (IsAdminUser,)
    queryset = Person.objects.all()
    serializer_class = Serializer
    lookup_field = "id"

class ItemDeleteView(generics.DestroyAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the DELETE requests for a given ID.
    '''
    permission_classes = (IsAdminUser,)
    queryset = Person.objects.all()
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    '''
    Provides access to the GET request for a list of all Person objects.
    '''
    queryset = Person.objects.all()
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    '''
     Provides access to the POST request for creating Person objects.
    '''
    permission_classes = (IsAdminUser,)
    queryset = Person.objects.all()
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        name_prefix = ""
        if request.data['name_prefix']:
            name_prefix = request.data['name_prefix']
        name_first = request.data['name_first']
        name_middle = ""
        if request.data['name_middle']:
            name_middle = request.data['name_middle']
        name_last = request.data['name_last']
        name_suffix = ""
        if  request.data['name_suffix']:
            name_suffix = request.data['name_suffix']
        name = concat_name(name_prefix,
                           name_last,
                           name_first,
                           name_middle,
                           name_suffix)
        request.data['name'] = name

        id = slugify(name) # pylint: disable=redefined-builtin, invalid-name

        queryset = Person.objects.filter(id=id)

        if queryset.count() != 0:
            detail = 'A Person entry already exists with the id '+id
            raise serializers.ValidationError(detail)

        return super(CreateView, self).create(request, *args, **kwargs)
