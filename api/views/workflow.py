# -*- coding: utf-8 -*-
"""
Defines the Workflow views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models.workflow import Workflow
from api.models.workflow import Serializer
from api.permissions.admin import IsAdminOrReadOnly


class ItemView(generics.RetrieveAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    '''    
    queryset = Workflow.objects.all()
    serializer_class = Serializer
    lookup_field = "id"

class ItemEditView(generics.UpdateAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the PATCH and PUT requests for a given ID.
    '''
    permission_classes = (IsAdminUser,)
    queryset = Workflow.objects.all()
    serializer_class = Serializer
    lookup_field = "id"

class ItemDeleteView(generics.DestroyAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the DELETE requests for a given ID.
    '''
    permission_classes = (IsAdminUser,)
    queryset = Workflow.objects.all()
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    '''
    Provides access to the GET request for a list of all Workflow objects.
    '''
    queryset = Workflow.objects.all()
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    '''
     Provides access to the POST request for creating Workflow objects.
    '''
    permission_classes = (IsAdminUser,)
    queryset = Workflow.objects.all()
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        id = slugify(name) # pylint: disable=redefined-builtin, invalid-name

        queryset = Workflow.objects.filter(id=id)

        if queryset.count() != 0:
            detail = 'A Workflow entry already exists with the id '+id
            raise serializers.ValidationError(detail)

        return super(CreateView, self).create(request, *args, **kwargs)
