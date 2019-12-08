# -*- coding: utf-8 -*-
"""
Defines the Publisher views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models.publisher import Publisher
from api.models.publisher import Serializer
from api.models.publisher import PublisherHistorySerializer
from api.permissions.admin import IsAdminOrReadOnly


class ItemView(generics.RetrieveAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    '''    
    queryset = Publisher.objects.all()
    serializer_class = Serializer
    lookup_field = "id"

class ItemEditView(generics.UpdateAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the PATCH and PUT requests for a given ID.
    '''
    permission_classes = (IsAdminUser,)
    queryset = Publisher.objects.all()
    serializer_class = Serializer
    lookup_field = "id"

class ItemDeleteView(generics.DestroyAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the DELETE requests for a given ID.
    '''
    permission_classes = (IsAdminUser,)
    queryset = Publisher.objects.all()
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    '''
    Provides access to the GET request for a list of all Publisher objects.
    '''
    queryset = Publisher.objects.all()
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    '''
     Provides access to the POST request for creating Publisher objects.
    '''
    permission_classes = (IsAdminUser,)
    queryset = Publisher.objects.all()
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        id = slugify(name) # pylint: disable=redefined-builtin, invalid-name

        queryset = Publisher.objects.filter(id=id)

        if queryset.count() != 0:
            detail = 'A Publisher entry already exists with the id '+id
            raise serializers.ValidationError(detail)

        return super(CreateView, self).create(request, *args, **kwargs)

class PublisherHistoryView(generics.RetrieveAPIView):
    """Get org history by name"""
    serializer_class = PublisherHistorySerializer
    queryset = Publisher.objects.all()
    lookup_field = "id"
